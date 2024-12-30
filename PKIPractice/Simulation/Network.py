from typing import Union

# Relative pathing from project package
import sys
from os.path import abspath, dirname

script_dir = dirname(abspath(__file__))

if script_dir in ['PKI_Practice', 'app']:
    sys.path.append(abspath('PKIPractice'))
elif script_dir == 'PKIPractice':
    sys.path.append(abspath(script_dir))
else:
    sys.path.append(abspath('..'))

from PKIPractice.Simulation.Holder import Holder


class PKINetwork:
    def __init__(self, name: str, auto_config: Union[dict, None], manual_config: Union[dict, None]) -> None:
        # Unique identifier
        self.network_name = name

        # Network counts
        self.network_level_count: int = auto_config['level_count']
        self.network_count_by_level: list[int] = auto_config['count_by_level']
        self.network_total_count: int = 0

        # Environment variables
        self.env_uid_hash: str = auto_config['uid_hash']
        self.env_sig_hash: str = auto_config['sig_hash']
        self.env_encrypt_alg: dict = auto_config['encrypt_alg']
        self.env_revoc_probs: list[float] = auto_config['revoc_probs']
        self.env_cert_valid_durs: list[str] = auto_config['cert_valid_durs']
        self.env_cache_durs: list[str] = auto_config['cache_durs']
        self.env_cooldown_durs: list[str] = auto_config['cooldown_durs']
        self.env_timeout_durs: list[str] = auto_config['timeout_durs']

        # Network hierarchy
        self.network = {}
        self.network_log = []

        # Manual configuration
        for key, value in manual_config.items():
            self.add_to_network(key, value, auto_config)

    def add_to_network(self, holder_name: str, holder_man_config: dict, auto_config: dict) -> None:
        self.network[holder_name] = 'Holder'
