"""
Module used for defining the network class and it's functionality.
"""

from typing import Union, List

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
    Placeholder docuscript. Will be used to direct communications between holders.
    """
    def __init__(self, network: dict):
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
        Placeholder
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
