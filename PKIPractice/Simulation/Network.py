"""
Module used for defining the network class and it's functionality.
"""

from typing import Union, List, Dict

# Relative pathing from project root
import sys
from os.path import abspath, dirname, join

script_dir = dirname(abspath(__file__))

if script_dir in ['PKI_Practice', 'PKI Practice', 'app']:
    sys.path.append(abspath(script_dir))
elif script_dir == 'PKIPractice':
    sys.path.append(abspath(join(script_dir, '..')))
else:
    sys.path.append(abspath(join(script_dir, '../..')))

from PKIPractice.Simulation.Holder import PKIHolder


class PKIHub:
    """
    The "infrastructure" of the network. Will be used to direct communications between holders.

    Attributes:
        mirror_store (dict): The "mirror" of the environment hierarchy in literal name.
        loc_store (dict): The location of every holder in the environment.
        send_store (dict): Where to send information for each holder, split into sending "up" or "down" the PKI
            hierarchy.
    """
    def __init__(self, network: Dict[int, List[PKIHolder]]):
        # Create a mirror of network and location store
        self.mirror_store: dict = {}
        self.loc_store: dict = {}  # Sender = key, Receiver = value

        for level, holders in network.items():
            self.mirror_store[level] = []
            for holder in holders:
                # Add the name of the holder to the store
                self.mirror_store[level].append(holder.get_name())

                # Add the location of the holder
                self.loc_store[holder.get_name()] = (level, len(self.mirror_store[level]) - 1)

                # Set the hub for the holder
                holder.set_hub_conn(self)

        # Use mirror store to decide who to send things to.
        self.send_store: dict = {'up': {}, 'down': {}}
        for level, names in self.mirror_store.items():
            # Skip first level
            if level == 1:
                continue

            prev_level = self.mirror_store[level-1]
            prev_level_index = 0
            PREV_LEVEL_MAX = len(prev_level)

            for holder_name in self.mirror_store[level]:
                # Record where the holder will send the message to
                self.send_store['up'][holder_name] = prev_level[prev_level_index]

                # Record where the receiver can send the message back
                if prev_level[prev_level_index] in self.send_store['down'].keys():
                    self.send_store['down'][prev_level[prev_level_index]].append(holder_name)
                else:
                    self.send_store['down'][prev_level[prev_level_index]] = [holder_name]

                prev_level_index += 1
                if prev_level_index == PREV_LEVEL_MAX:
                    prev_level_index = 0

    def forward_message(self):
        """Placeholder"""
        ...


class PKINetwork:
    """
    Placeholder docuscript.
    """
    def __init__(self, name: str, auto_config: Union[dict, None], manual_config: Union[dict, None]) -> None:
        # Unique identifier
        self.network_name: str = name

        # Network counts
        self.network_level_count: int = auto_config['level_count']
        self.network_count_by_level: List[int] = auto_config['count_by_level']
        self.network_total_count: int = 0

        # Environment variables
        self.env_uid_hash: str = auto_config['uid_hash']
        self.env_sig_hash: str = auto_config['sig_hash']
        self.env_encrypt_alg: dict = auto_config['encrypt_alg']
        self.env_revoc_probs: List[float] = auto_config['revoc_probs']
        self.env_cert_valid_durs: List[str] = auto_config['cert_valid_durs']
        self.env_cache_durs: List[str] = auto_config['cache_durs']
        self.env_cooldown_durs: List[str] = auto_config['cooldown_durs']
        self.env_timeout_durs: List[str] = auto_config['timeout_durs']

        # Network hierarchy
        self.network: dict = {}
        for i in range(self.network_level_count):
            self.network[i+1] = []

        self.network_log: List[str] = []

        # Log events that have already happened
        self.log_event(f'Network {self.network_name} created.')
        self.log_event('Environmental variables set.')
        self.log_event('Empty network hierarchy created.')
        self.log_event('Network log created and started.')

        # Manual configuration
        if manual_config is not None:
            for holder_name, holder_config in manual_config.items():
                result: bool = self.add_to_network(holder_name, holder_config, auto_config)
                if result:
                    self.log_event(f'Holder {holder_name} added to network.')
                else:
                    self.log_event(f'Invalid location configuration. {holder_name} was ignored.')

        # Filling in gaps
        auto_holder_count = 1
        for i in range(len(self.network_count_by_level)):
            while len(self.network[i+1]) < self.network_count_by_level[i]:
                self.add_to_network(
                    f'holder_l{i+1}_c{auto_holder_count}',
                    {'location': {'level': i+1}},
                    auto_config
                )
                self.log_event(f'Gap found. Filler Holder #{auto_holder_count} at level {i+1} added to network.')
                auto_holder_count += 1

        # Network hub
        self.network_hub = PKIHub(self.network)
        self.log_event('Network hub and connection information created.')
    
    def log_event(self, message: str) -> None:
        """
        Takes a message, prints it, and saves it to network log.

        Args:
            message: str - String value to save.
        """

        print(message)
        self.network_log.append(message)

    def add_to_network(self, holder_name: str, holder_config: dict, auto_config: dict) -> bool:
        """
        Takes a given holder name, holder configuration dictionary, and auto_config elements and creates a holder.
        Adds the holder to the growing network.

        Args:
            holder_name: str - The name of the manually created holder.
            holder_config: dict - The configuration settings of the holder.
            auto_config: dict - The configuration settings of the environment.

        Returns:
            bool - Success status on operation.
        """

        # Check if location is valid
        proper_keys: bool = all(
            isinstance(holder_config['location'][key], int) for key in holder_config['location'].keys()
        )
        enough_keys: bool = len(holder_config['location'].keys()) == 1

        if not proper_keys or not enough_keys:
            print(f'Invalid location configuration. {holder_name} configuration will be ignored.')
            return False

        # Create holder
        holder: PKIHolder = PKIHolder(holder_name, holder_config, auto_config)

        # Add holder to network
        level = holder_config['location']['level']
        self.network[level].append(holder)

        return True
