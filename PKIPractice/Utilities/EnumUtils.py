"""
This file contains enums used in the program along with functions to retrieve information.
"""

from enum import Enum
from typing import Union, List, Tuple
import random
import copy


class SUPPORTED_HASH_ALGS(Enum):
    """
    This class contains all supported hash algorithms.
    It is used in both the autoconfiguration and manual configuration to set hashing algorithms.
    """
    SHA224 = 'sha224'
    SHA256 = 'sha256'
    SHA384 = 'sha384'
    SHA512 = 'sha512'
    SHA3_224 = 'sha3_224'
    SHA3_256 = 'sha3_256'
    SHA3_384 = 'sha3_384'
    SHA3_512 = 'sha3_512'
    BLAKE2B = 'blake2b'
    BLAKE2S = 'blake2s'


class SUPPORTED_ENCRYPT_ALGS(Enum):
    """
    This class contains all supported encryption algorithms.
    It is used in both the autoconfiguration and manual configuration to set encryption algorithms.
    """
    RSA = 'rsa'
    ECC = 'ecc'


class SUPPORTED_ECC_CURVES(Enum):
    """
    This class contains all supported curves for eliptic curve cryptography.
    It is used in both the autoconfiguration and manual configuration to set the curve for ECC.
    """
    SECP256R1 = 'secp256r1'
    SECP384R1 = 'secp384r1'
    SECP521R1 = 'secp521r1'
    SECP224R1 = 'secp224r1'
    SECP192R1 = 'secp192r1'
    SECP256K1 = 'secp256k1'


class COMMON_CA(Enum):
    NOT_AUTH = 'not_auth'
    INTER_AUTH = 'inter_auth'
    ROOT_AUTH = 'root_auth'


class COMMON_USERS(Enum):
    """
    This class contains all supported user types by default.
    It is used in the manual configuration file to specify user types.
    """
    GUEST = 'guest'
    PERSONAL = 'personal'
    ENTERPRISE = 'enterprise'


class COMMON_ADMINS(Enum):
    """
    This class contains all supported admin types by default.
    It is used in the manual configuration file to specify admin types.
    """
    DOMAIN_ADMIN = 'domain_admin'
    SCHEMA_ADMIN = 'schema_admin'
    SERVER_ADMIN = 'server_admin'
    NETWORK_ADMIN = 'network_admin'
    CLOUD_ADMIN = 'cloud_admin'
    DATABASE_ADMIN = 'database_admin'
    AUDITOR = 'auditor'


class COMMON_ACCOUNTS(Enum):
    """
    This class contains all supported account types by default.
    It is used in the manual configuration file to specify account types.
    """
    USER = 'user'
    ADMIN = 'admin'
    SYSTEM = 'system'


class COMMON_WINDOWS(Enum):
    """
    This class contains all supported Windows versions by default.
    It is used in the manual configuration file to specify Windows versions.
    """
    WINDOWS_2000 = ('professional', 'server', 'advanced_server', 'datacenter_server')
    WINDOWS_XP = ('home', 'professional')
    WINDOWS_VISTA = ('starter', 'home_basic', 'home_premium', 'business', 'enterprise', 'ultimate')
    WINDOWS_7 = ('starter', 'home_basic', 'home_premium', 'business', 'enterprise', 'ultimate')
    WINDOWS_8 = ('home', 'pro', 'enterprise')
    WINDOWS_10 = ('home', 'pro', 'educational', 'enterprise')
    WINDOWS_11 = ('home', 'pro', 'educational', 'enterprise')


class COMMON_WINDOWS_SERVER(Enum):
    """
    This class contains all supported Windows Server versions by default.
    It is used in the manual configuration file to specify Windows Server versions.
    """
    WINDOWS_SERVER_2003 = ('web', 'standard', 'enterprise', 'datacenter')
    WINDOWS_SERVER_2008 = ('web', 'standard', 'enterprise', 'datacenter', 'itanium', 'foundation', 'hpc')
    WINDOWS_SERVER_2012 = ('foundation', 'essentials', 'standard', 'datacenter')
    WINDOWS_SERVER_2016 = ('standard', 'datacenter')
    WINDOWS_SERVER_2019 = ('standard', 'datacenter')
    WINDOWS_SERVER_2022 = ('standard', 'datacenter', 'datacenter_azure')


class COMMON_MICROSOFT(Enum):
    """
    This class contains all supported Microsoft products by default.
    It is used in the manual configuration file to specify Microsoft products.
    """
    WINDOWS = 'windows'
    WINDOWS_SERVER = 'windows_server'


class COMMON_LINUX(Enum):
    """
    This class contains all supported Linux distributions by default.
    It is used in the manual configuration file to specify Linux distributions.
    """
    DEBIAN = ('debian', 'linux_mint', 'kali_linux', 'raspberry_pi', 'mx_linux', 'debian')
    RED_HAT = ('red_hat', 'fedora', 'cent_os')
    ARCH_LINUX = 'arch_linux'
    GENTOO = 'gentoo'
    SUSE = ('suse_linux_enterprise', 'open_suse')
    ALPINE = 'alpine'
    NIX_OS = 'nix_os'
    QUBES_OS = 'qubes_os'
    UBUNTU_SERVER = 'ubuntu_server'


class COMMON_BSD(Enum):
    """
    This class contains all supported BSD distributions by default.
    It is used in the manual configuration file to specify BSD distributions.
    """
    FREE_BSD = 'free_bsd'
    OPEN_BSD = 'open_bsd'
    NET_BSD = 'net_bsd'


class COMMON_MAC_OS_X(Enum):
    """
    This class contains all supported Mac OS X versions by default.
    It is used in the manual configuration file to specify Mac OS X versions.
    """
    LEOPARD = 'leopard'
    SNOW_LEOPARD = 'snow_leopard'
    LION = 'lion'
    MOUNTAIN_LION = 'mountain_lion'
    MAVERICKS = 'mavericks'
    YOSEMITE = 'yosemite'
    EL_CAPITAN = 'el_capitan'
    SIERRA = 'sierra'
    HIGH_SIERRA = 'high_sierra'
    MOJAVE = 'mojave'
    CATALINA = 'catalina'
    BIG_SUR = 'big_sur'
    MONTEREY = 'monterey'
    VENTURA = 'ventura'
    SONOMA = 'sonoma'
    SEQUOIA = 'sequoia'


class COMMON_UNIX(Enum):
    """
    This class contains all supported Unix flavors by default.
    It is used in the manual configuration file to specify Unix flavors.
    """
    LINUX = 'linux'
    BSD = 'bsd'
    SOLARIS = 'solaris'
    MAC_OS_X = 'mac_os_x'


class COMMON_MOBILE(Enum):
    """
    This class contains all supported mobile operating system families by default.
    It is used in the manual configuration file to specify mobile operating system families.
    """
    IOS = 'ios'
    ANDROID = (
        'android_nougat', 'android_oreo', 'android_pie', 'android_10', 'android_11', 'android_12',
        'android_13', 'android_14', 'android_15', 'android_16'
    )


class COMMON_ROUTING(Enum):
    """
    This class contains all supported routing platforms by default.
    It is used in the manual configuration file to specify routing platforms.
    """
    ONIE = 'onie'
    ONL = 'onl'
    OPX = 'opx'
    DNOS = 'dnos'
    JUNOS = 'junos'
    FBOSS = 'fboss'
    SONIC = 'sonic'
    ARUBA_OS = 'aruba_os'
    CISCO_IOS = 'cisco_ios'
    NEXUS_NOS = 'nexus_nos'
    OPENWRT = 'openwrt'


class COMMON_OS(Enum):
    """
    This class contains all supported operating system types by default.
    It is used in the manual configuration file to specify operating system types.
    """
    MICROSOFT = 'microsoft'
    UNIX = 'unix'
    MOBILE = 'mobile'
    ROUTING = 'routing'


class COMMON_ENDPOINT(Enum):
    """
    This class contains all supported endpoint hardware manufacturers by default.
    It is used in the manual configuration file to specify endpoint hardware manufacturers.
    """
    DESKTOP = ('hewlett_packard', 'acer', 'dell', 'lenovo', 'toshiba', 'ibm', 'fujitsu', 'nec', 'apple')
    LAPTOP = ('samsung', 'razer', 'microsoft', 'msi', 'asus', 'acer', 'dell', 'lenovo', 'hewlett_packard', 'apple')
    PHONE = ('samsung', 'apple', 'huawei', 'sony', 'google', 'microsoft', 'toshiba', 'dell')
    SERVER = ('dell', 'hewlett_packard', 'supermicro', 'inspur', 'lenovo', 'huawei', 'ibm', 'fukitsu', 'cisco')
    IOT = (
        'advantech', 'raspberry_pi', 'arudino', 'nvidia', 'beagleboard',
        'udoo', 'onlogic', 'kontron', 'arbor', 'axiomtek'
    )


class COMMON_NETWORK(Enum):
    """
    This class contains all supported network hardware manufacturers by default.
    It is used in the manual configuration file to specify network hardware manufacturers.
    """
    ROUTER = ('cisco', 'peplink', 'advantech', 'netgear', 'tp_link')
    SWITCH = ('anchor', 'honeywell', 'philips', 'siemens', 'cisco', 'hpl')
    ACCESS_POINT = ('cisco', 'fortinet', 'netgear', 'zyxel', 'tp_link', 'engenius')


class COMMON_APPLIANCE(Enum):
    """
    This class contains all supported appliance hardware manufacturers by default.
    It is used in the manual configuration file to specify appliance hardware manufacturers.
    """
    FIREWALL = ('bitdefender', 'cisco', 'fortinet', 'palo_alto', 'netgate', 'watchguard', 'sonicwall')
    UTM_DEVICE = ('sonicwall', 'fortigate', 'barracuda', 'juniper', 'trellix', 'palo_alto')


class COMMON_PERIPHERALS(Enum):
    """
    This class contains all supported peripheral hardware manufacturers by default.
    It is used in the manual configuration file to specify peripheral hardware manufacturers.
    """
    USB_KEY = ('samsung', 'sandisk', 'corsiar', 'kingston', 'pny')
    SMART_CARD = ('thales', 'nxp', 'cardlogix', 'infineon')
    EXTERNAL_STORAGE = ('seagate', 'western_digital', 'sandisk', 'transcend', 'lacie')


class COMMON_HARDWARE(Enum):
    """
    This class contains all supported hardware types by default.
    It is used in the manual configuration file to specify hardware types.
    """
    ENDPOINT = 'endpoint'
    NETWORK = 'network'
    APPLIANCE = 'appliance'
    PERIPHERAL = 'peripheral'


def has_value(enum_class, value: str) -> bool:
    """
    Check if a given value exists in the specified enum class.

    Args:
        enum_class: The enum class to check.
        value (str): The value to check.

    Returns:
        bool: True if the value exists in the enum class, False otherwise.
    """

    for item in enum_class:
        if isinstance(item.value, tuple):
            for v in item.value:
                if value == v.lower().replace(' ', '_').replace('-', '_'):
                    return True
        else:
            if value == item.value.lower().replace(' ', '_').replace('-', '_'):
                return True

    return False


def get_all_items(enum_class, verbose: bool = False) -> Union[dict, list]:
    """
    Return the versions of an enum class.
    If verbose is True, return the versions as a dictionary with names and values.
    If verbose is False, return the versions as a list with names only.

    Args:
        enum_class: The enum class to get the versions from.
        verbose (bool): If True, return the versions as a dictionary with names and values.
                        If False, return the versions as a list with names only.

    Returns:
        Union[dict, list]: The versions of the enum class.
    """

    if verbose:
        return {item.name: item.value for item in enum_class}
    else:
        return [item.name for item in enum_class]


def pass_rule_check(cur_settings: list) -> bool:
    """
    An arbitrary set of rule checks to make sure the random generation is at least realistic.

    Args:
        cur_settings (list): The current settings.

    Returns:
        bool: True if the current value passes the rule check, False otherwise.
    """

    h_type = cur_settings[0][0]
    h_subtype = cur_settings[0][1]
    os_type = cur_settings[1][0]
    os_subtype = cur_settings[1][1]
    os_dist = cur_settings[1][2]
    a_type = cur_settings[2][0]
    ca_type = cur_settings[3][0]

    # Hardware based rules
    # If a device type is a networking device, it can only use routing OSes and Unix OSes that are not Mac OS X
    network_is_routing = h_type == 'network' and os_type in ['routing', '']

    network_is_unix = h_type == 'network' and os_type in ['unix', '']
    unix_network_not_mac = network_is_unix and os_subtype != 'mac_os_x'

    if h_type == 'network' and not (network_is_routing or unix_network_not_mac):
        return False

    # If a device endpoint type is an IoT device, it can only use Unix OSes that are not Mac OS X
    iot_is_unix = h_subtype == 'iot' and os_type in ['unix', '']
    unix_iot_not_mac = iot_is_unix and os_subtype != 'mac_os_x'
    if h_subtype == 'iot' and not unix_iot_not_mac:
        return False

    # If a device endpoint type is a phone, it can only use mobile operating systems
    phone_is_mobile = h_subtype == 'phone' and os_type in ['mobile', '']
    if h_subtype == 'phone' and not phone_is_mobile:
        return False

    # If a device endpoint type is a server, it can only use Windows Server OSes and Unix OSes that are not Mac OS X
    server_is_microsoft = h_subtype == 'server' and os_type in ['microsoft', '']
    ms_server_is_ws = server_is_microsoft and os_subtype in ['windows_server', '']

    server_is_unix = h_subtype == 'server' and os_type in ['unix', '']
    unix_server_not_mac = server_is_unix and os_subtype != 'mac_os_x'

    if h_subtype == 'server' and not (ms_server_is_ws or unix_server_not_mac):
        return False

    # If a device endpoint type is a laptop or desktop it can't use a mobile OS
    laptop_or_desktop = h_subtype == 'laptop' or h_subtype == 'desktop'
    lap_desk_not_mobile = laptop_or_desktop and os_type != 'mobile'
    if laptop_or_desktop and not lap_desk_not_mobile:
        return False

    # Software based rules
    # If Windows Server OS it has to be a system or admin account
    ws_is_system_or_admin = os_subtype == 'windows_server' and a_type in ['system', 'admin', '']
    if os_subtype == 'windows_server' and not ws_is_system_or_admin:
        return False

    # If Ubuntu Server OS it has to be a system or admin account
    us_is_system_or_admin = os_dist == 'ubuntu_server' and a_type in ['system', 'admin', '']
    if os_dist == 'ubuntu_server' and not us_is_system_or_admin:
        return False

    # Appliances and Peripherals have to be a system account
    app_or_peri = h_type == 'appliance' or h_type == 'peripheral'
    app_peri_is_system = app_or_peri and a_type in ['system', '']
    if app_or_peri and not app_peri_is_system:
        return False

    # CA based rules
    # If Not a Server it cannot be a certificate authority
    is_ca = ca_type in ['inter_auth', 'root_auth']
    ca_is_endpoint = is_ca and h_type in ['endpoint', '']
    ca_is_server = is_ca and h_subtype in ['server', '']
    if is_ca and not (ca_is_endpoint and ca_is_server):
        return False

    return True


def check_exceptions(cur_settings: list) -> list:
    """
    Pre-emptively fills out the settings if it runs into an exception rule.

    Args:
        cur_settings (list): The current settings.

    Returns:
        list: The pre-filled list if needed.
    """

    h_type = cur_settings[0][0]
    os_type = cur_settings[1][0]
    os_subtype = cur_settings[1][1]
    os_dist = cur_settings[1][2]
    a_type = cur_settings[2][0]

    # Hardware exceptions
    # If an appliance or peripheral, the all OS types should be the specific brand followed by "_os"
    if h_type in ['appliance', 'peripheral']:
        cur_settings[1][0] = cur_settings[0][2] + '_os'
        cur_settings[1][1] = cur_settings[0][2] + '_os'
        cur_settings[1][2] = cur_settings[0][2] + '_os'
        cur_settings[1][3] = cur_settings[0][2] + '_os'

    # Software exceptions
    # If not windows, windows-server, suse, red-hat, or debian dist, then OS subdist should be the OS dist.
    os_is_microsoft = os_type == 'microsoft'
    linux_os_has_subdist = os_dist in ['suse', 'red_hat', 'debian']

    if not (os_is_microsoft or linux_os_has_subdist):
        cur_settings[1][3] = os_dist

    # If a routing os, mobile-ios, or solaris, then all OS types should be the routing os or ios
    if os_type == 'routing' or os_subtype == 'ios' or os_subtype == 'solaris':
        cur_settings[1][2] = os_subtype
        cur_settings[1][3] = os_subtype

    # Account exceptions
    # If system, then the account subtype should be system
    if a_type == 'system':
        cur_settings[2][1] = a_type

    return cur_settings


def check_enum_value(outer_index: int, inner_index: int, cur_settings: list,
                     key: str, value: Union[tuple, str], parent: bool = False) -> tuple:
    """
    Decision Tree to check the values of the chosen enum given the enum key and the value(s).

    Args:
        outer_index (int): The index of the outer list.
        inner_index (int): The index of the inner list.
        cur_settings (list): The current settings list.
        key (str): The chosen key from the returned enum dictionary.
        value (Union[tuple, str]): The values of the chosen key.
        parent (bool): Whether a parent was used to get here.

    Returns:
        tuple: A tuple of-
            If the tested value was validated.
            A list of the current settings regardless of modification.
    """

    # Set variables
    temp_settings = copy.deepcopy(cur_settings)
    new_value_unvalidated = True

    # Set the inner index for the check
    if parent:
        local_inner_index = inner_index - 1
    else:
        local_inner_index = inner_index

    # Check if the value is a tuple and work accordingly
    if isinstance(value, tuple):
        # Create a list to go through
        end_options = list(value)
        using_end_options = True

        # Try options in list
        while end_options and using_end_options:
            # Set options
            temp_settings[outer_index][local_inner_index] = key.lower()

            end_option_index = random.randint(0, len(end_options) - 1)
            temp_settings[outer_index][local_inner_index + 1] = end_options[end_option_index]

            # Check if temporary settings passes the rule check
            if pass_rule_check(temp_settings):
                cur_settings = temp_settings
                using_end_options = False
                new_value_unvalidated = False

            # Remove used option
            del end_options[end_option_index]
            print(end_options)
    else:
        temp_settings[outer_index][local_inner_index] = value

        # Check if temporary settings passes the rule check
        if pass_rule_check(temp_settings):
            cur_settings = temp_settings
            new_value_unvalidated = False

    return new_value_unvalidated, cur_settings


def update_settings(outer_index: int, inner_index: int, cur_settings: list) -> list:
    """
    Updates the settings list based on the current information being looked at.

    Args:
        outer_index (int): The index of the outer list.
        inner_index (int): The index of the inner list.
        cur_settings (list): The current settings list.

    Returns:
        list: The updated settings list.
    """

    enum_switch_known: dict = {
        'endpoint': COMMON_ENDPOINT,
        'network': COMMON_NETWORK,
        'appliance': COMMON_APPLIANCE,
        'peripheral': COMMON_PERIPHERALS,
        'routing': COMMON_ROUTING,
        'mobile': COMMON_MOBILE,
        'unix': COMMON_UNIX,
        'microsoft': COMMON_MICROSOFT,
        'windows': COMMON_WINDOWS,
        'windows_server': COMMON_WINDOWS_SERVER,
        'bsd': COMMON_BSD,
        'linux': COMMON_LINUX,
        'mac_os_x': COMMON_MAC_OS_X,
        'admin': COMMON_ADMINS,
        'user': COMMON_USERS
    }

    enum_switch_unknown: dict = {
        0: {
            0: [COMMON_HARDWARE],
            1: [COMMON_PERIPHERALS, COMMON_APPLIANCE, COMMON_NETWORK, COMMON_ENDPOINT]
        },
        1: {
            0: [COMMON_OS],
            1: [COMMON_ROUTING, COMMON_MOBILE, COMMON_UNIX, COMMON_MICROSOFT],
            2: [COMMON_WINDOWS_SERVER, COMMON_WINDOWS, COMMON_BSD, COMMON_LINUX, COMMON_MAC_OS_X]
        },
        2: {
            0: [COMMON_ACCOUNTS],
            1: [COMMON_ADMINS, COMMON_USERS]
        },
        3: {
            0: [COMMON_CA]
        }
    }

    parent_value = ''
    last_value = ''
    new_value_unvalidated = True

    # Choose the next enum if the last value is not empty
    if inner_index > 0 and cur_settings[outer_index][inner_index-1] != '':  # Go down a certain path
        last_value = cur_settings[outer_index][inner_index-1]

        # If setting the last value was successful, set the enum to use.
        if last_value in enum_switch_known.keys():
            enum_choice = enum_switch_known[last_value]
        else:
            # If not, use the parent to get the enum data
            parent_value = cur_settings[outer_index][inner_index-2]

            # If the parent's found, set the enum_choice
            if parent_value in enum_switch_known.keys():
                enum_choice = enum_switch_known[parent_value]
            else:
                # If the parent is not found, fill with whatever value was detected and call it a day
                for i in range(inner_index, len(cur_settings[outer_index])):
                    if cur_settings[outer_index][inner_index] == '':
                        cur_settings[outer_index][inner_index] = last_value

                cur_settings = check_exceptions(cur_settings)
                return cur_settings
    else:  # Random selection as final solution
        enum_type_loc = enum_switch_unknown[outer_index][inner_index]
        enum_index = random.randint(0, len(enum_type_loc) - 1)
        enum_choice = enum_type_loc[enum_index]

    # Get the enum data
    enum_data = get_all_items(enum_choice, verbose=True)

    # If parent value set, go straight through the parent for the attempt
    if parent_value != '':
        # Set the child value and test it
        if last_value.upper() in enum_data.keys():
            child_value = enum_data[last_value.upper()]
            new_value_unvalidated, cur_settings = check_enum_value(
                outer_index, inner_index, cur_settings, last_value, child_value, parent=True
            )

        else:  # If the parent is not found, fill with whatever value was detected and call it a day
            for i in range(inner_index, len(cur_settings[outer_index])):
                if cur_settings[outer_index][inner_index] == '':
                    cur_settings[outer_index][inner_index] = last_value
    else:
        # Get a random value from the enum data the abides by unknown enum switch and test.
        # Keep doing that until a value passes the rule set.
        while enum_data and new_value_unvalidated:
            # Get a random value
            random_key = random.choice(list(enum_data.keys()))
            random_value = enum_data[random_key]

            # Test the value
            new_value_unvalidated, cur_settings = check_enum_value(
                outer_index, inner_index, cur_settings, random_key, random_value
            )

            # Remove key once used
            del enum_data[random_key]
            print(enum_data)

    # Address Hard-fill cases
    cur_settings = check_exceptions(cur_settings)
    return cur_settings


def auto_fill_types(cur_settings: list) -> list:
    """
    Autofill the types of the enum class.

    Args:
        cur_settings (list): The current settings list.

    Returns:
        tuple: Exception flag and randomly generated type properties for holder.
    """

    for outer_index in range(len(cur_settings)):
        for inner_index in range(len(cur_settings[outer_index])):
            # Get the enum to try to change
            cur_info = cur_settings[outer_index][inner_index]
            if cur_info == '':
                cur_settings = update_settings(outer_index, inner_index, cur_settings)
            print(cur_settings)

    return cur_settings


if __name__ == '__main__':
    # print(get_all_items(COMMON_ROUTING, True))

    for i in range(5000):
         auto_fill_types([['', '', ''], ['', '', '', ''], ['', ''], ['']])
