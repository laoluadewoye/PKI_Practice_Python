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

from PKIPractice.Utilities.DataclassUtils import *
from PKIPractice.Utilities.EnumUtils import auto_fill_types


class Holder:
    def __init__(self, holder_name: str, holder_config: dict, auto_config: dict):
        # Name of holder
        self.holder_name: str = holder_name

        level = holder_config['location']['level']

        # Environment information
        has_env_overrides = 'env_overrides' in holder_config.keys()
        if has_env_overrides and 'uid_hash' in holder_config['env_overrides'].keys():
            uid_hash = holder_config['env_overrides']['uid_hash']
        else:
            uid_hash = auto_config['uid_hash']

        if has_env_overrides and 'sig_hash' in holder_config['env_overrides'].keys():
            sig_hash = holder_config['env_overrides']['sig_hash']
        else:
            sig_hash = auto_config['sig_hash']

        if has_env_overrides and 'encrypt_alg' in holder_config['env_overrides'].keys():
            encrypt_alg = holder_config['env_overrides']['encrypt_alg']
        else:
            encrypt_alg = auto_config['encrypt_alg']

        if has_env_overrides and 'revoc_prob' in holder_config['env_overrides'].keys():
            revoc_prob = holder_config['env_overrides']['revoc_prob']
        else:
            revoc_prob = auto_config['revoc_probs'][level-1]

        if has_env_overrides and 'cert_valid_dur' in holder_config['env_overrides'].keys():
            cert_valid_dur = holder_config['env_overrides']['cert_valid_dur']
        else:
            cert_valid_dur = auto_config['cert_valid_durs'][level-1]

        if has_env_overrides and 'cache_dur' in holder_config['env_overrides'].keys():
            cache_dur = holder_config['env_overrides']['cache_dur']
        else:
            cache_dur = auto_config['cache_durs'][level-1]

        if has_env_overrides and 'cooldown_dur' in holder_config['env_overrides'].keys():
            cooldown_dur = holder_config['env_overrides']['cooldown_dur']
        else:
            cooldown_dur = auto_config['cooldown_durs'][level-1]

        if has_env_overrides and 'timeout_dur' in holder_config['env_overrides'].keys():
            timeout_dur = holder_config['env_overrides']['timeout_dur']
        else:
            timeout_dur = auto_config['timeout_durs'][level-1]

        self.env_info: HOLDER_ENV_INFO = HOLDER_ENV_INFO(
            level=level, uid_hash=uid_hash, sig_hash=sig_hash, encrypt_alg=encrypt_alg, revoc_prob=revoc_prob,
            cert_valid_dur=cert_valid_dur, cache_dur=cache_dur, cooldown_dur=cooldown_dur, timeout_dur=timeout_dur
        )

        # Type information
        type_fill = [['', '', ''], ['', '', '', ''], ['', ''], ['']]
        has_holder_type = 'holder_type_info' in holder_config.keys()

        if level == 1:
            type_fill[3][0] = 'root_auth'
        elif level < auto_config['level_count']:
            type_fill[3][0] = 'inter_auth'
        else:
            type_fill[3][0] = 'not_auth'

        if has_holder_type:
            for key in holder_config['holder_type_info'].keys():
                if key == 'hardware_type':
                    type_fill[0][0] = holder_config['holder_type_info']['hardware_type']
                elif key == 'hardware_subtype':
                    type_fill[0][1] = holder_config['holder_type_info']['hardware_subtype']
                elif key == 'hardware_brand':
                    type_fill[0][2] = holder_config['holder_type_info']['hardware_brand']
                elif key == 'os_category':
                    type_fill[1][0] = holder_config['holder_type_info']['os_category']
                elif key == 'os_subcategory':
                    type_fill[1][1] = holder_config['holder_type_info']['os_subcategory']
                elif key == 'os_dist':
                    type_fill[1][2] = holder_config['holder_type_info']['os_dist']
                elif key == 'os_subdist':
                    type_fill[1][3] = holder_config['holder_type_info']['os_subdist']
                elif key == 'account_type':
                    type_fill[2][0] = holder_config['holder_type_info']['account_type']
                elif key == 'account_subtype':
                    type_fill[2][1] = holder_config['holder_type_info']['account_subtype']
                elif key == 'ca_status':
                    type_fill[3][0] = holder_config['holder_type_info']['ca_status']

        type_fill = auto_fill_types(type_fill)
        print(type_fill)
