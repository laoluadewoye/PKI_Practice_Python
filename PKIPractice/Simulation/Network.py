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

from PKIPractice.Simulation.Holder import Holder


class PKINetwork:
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
        self.network_log: List[str] = []

        # Log events that have already happened
        self.network_log.append(f'Network {self.network_name} created.')
        self.network_log.append('Environmental variables set.')
        self.network_log.append('Empty network hierarchy created.')
        self.network_log.append('Network log created and started.')

        # Manual configuration
        if manual_config is not None:
            for holder_name, holder_config in manual_config.items():
                self.add_to_network(holder_name, holder_config, auto_config)

    def add_to_network(self, holder_name: str, holder_config: dict, auto_config: dict) -> None:
        print(holder_name)

        # Check if location is valid
        proper_keys = all(
            isinstance(holder_config['location'][key], int) for key in holder_config['location'].keys()
        )
        enough_keys = len(holder_config['location'].keys()) == 2

        if proper_keys and enough_keys:
            ...
        else:
            print(f'Invalid location configuration. {holder_name} configuration will be ignored.')

        # Create holder
        holder: Holder = Holder(holder_name, holder_config, auto_config)
