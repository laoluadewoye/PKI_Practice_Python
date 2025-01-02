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
    os_dist = cur_settings[1][2]

    # Hardware based rules
    # If a device type is a networking device, it can only use routing OSes and Unix OSes that are not Mac OS X
    network_is_routing = h_type == 'network' and os_type == 'routing'

    network_is_unix = h_type == 'network' and os_type == 'unix'
    unix_network_not_mac = network_is_unix and os_dist != 'mac_os_x'

    if h_type == 'network' and not (network_is_routing or unix_network_not_mac):
        return False

    # If a device endpoint type is an IoT device, it can only use Unix OSes that are not Mac OS X
    iot_is_unix = h_subtype == 'iot' and os_type == 'unix'
    unix_iot_not_mac = iot_is_unix and os_dist != 'mac_os_x'

    if h_subtype == 'iot' and not unix_iot_not_mac:
        return False

    # If a device endpoint type is a phone, it can only use mobile operating systems
    phone_is_mobile = h_subtype == 'phone' and os_type == 'mobile'
    if h_subtype == 'phone' and not phone_is_mobile:
        return False

    # If a device endpoint type is a server, it can only use Windows Server OSes and Unix OSes that are not Mac OS X
    server_is_ws = h_subtype == 'server' and os_dist == 'windows_server'

    server_is_unix = h_subtype == 'server' and os_type == 'unix'
    unix_server_not_mac = server_is_unix and os_dist != 'mac_os_x'

    if h_subtype == 'server' and not (server_is_ws or unix_server_not_mac):
        return False

    # If a device endpoint type is a laptop or desktop
    laptop_or_desktop = h_subtype == 'laptop' or h_subtype == 'desktop'
    lap_desk_not_mobile = laptop_or_desktop and os_type != 'mobile'

    if laptop_or_desktop and not lap_desk_not_mobile:
        return False

    return True


def check_for_exceptions(cur_settings: list, cur_value: str) -> Tuple[bool, list]:
    """
    Checks current value to see if it fits a specific exception.
    If so, the rest of the settings are generated manually and no more randomness happens.

    Args:
        cur_settings (list): The current settings.
        cur_value (str): The current value.

    Returns:
        Tuple[bool, list]: A tuple containing a boolean and a list.
        The boolean is True if the current value is an exception, False otherwise.
        The list is the list of settings to generate manually if True.
    """
    # Sample structure
    # 0 : [type, subtype, brand]
    # 1 : [cat, subcat, dist, subdist]
    # 2 : [type, subtype, status]

    h_type = cur_settings[0][0]
    h_subtype = cur_settings[0][1]
    os_type = cur_settings[1][0]
    os_subtype = cur_settings[1][1]
    os_dist = cur_settings[1][2]

    # Software based exceptions
    # Holders without any operating system specified are considered unknown and should have the system account.
    os_group_unknown = not has_value(COMMON_OS, os_type)
    os_subgroup_unknown = (
            not has_value(COMMON_ROUTING, os_dist) and
            not has_value(COMMON_MOBILE, os_dist) and
            not has_value(COMMON_UNIX, os_dist) and
            not has_value(COMMON_MICROSOFT, os_dist)
    )
    os_dist_unknown = (
            not has_value(COMMON_MAC_OS_X, os_dist) and
            not has_value(COMMON_BSD, os_dist) and
            not has_value(COMMON_LINUX, os_dist) and
            not has_value(COMMON_WINDOWS, os_dist) and
            not has_value(COMMON_WINDOWS_SERVER, os_dist)
    )

    if os_group_unknown and os_subgroup_unknown and os_dist_unknown:
        cur_settings[1][0] = cur_settings[0][2]
        cur_settings[1][1] = cur_settings[0][2]
        cur_settings[1][2] = cur_settings[0][2]
        cur_settings[1][3] = cur_settings[0][2]
        cur_settings[2][0] = 'system'
        cur_settings[2][1] = 'system'

    return False, []


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

    enum_class_switch: dict = {
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
        }
    }

    # Choose the enum wanted
    enum_type_loc = enum_class_switch[outer_index][inner_index]
    enum_index = random.randint(0, len(enum_type_loc) - 1)
    enum_choice = enum_type_loc[enum_index]

    # Get the enum data
    enum_data = get_all_items(enum_choice, verbose=True)

    # Get a random value from the enum data the abides by generation rules
    while True:
        # Get a value
        random_key = random.choice(list(enum_data.keys()))
        random_value = enum_data[random_key].lower().replace(' ', '_').replace('-', '_')

        # Check if the value is a tuple and append accordingly
        temp_settings = copy.deepcopy(cur_settings)
        if isinstance(random_value, tuple):
            temp_settings[outer_index][inner_index] = random_key.lower().replace(' ', '_').replace('-', '_')
            temp_settings[outer_index][inner_index+1] = random.choice(random_value)
        else:
            temp_settings[outer_index][inner_index] = random_value

        # Check if temporary settings passes the rule check
        if pass_rule_check(temp_settings):
            cur_settings = temp_settings
            break


def auto_fill_types(cur_settings: list) -> tuple:
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
                settings_locked, cur_settings = update_settings(outer_index, inner_index, cur_settings)
            else:
                ...

    return settings_locked, cur_settings


if __name__ == '__main__':
    type_fill = [['', '', ''], ['', '', '', ''], ['', '', '']]
    type_fill = auto_fill_types(type_fill)


"""

    if cur_value == '':
        # Start from the beginning
        cur_settings = [[], [], []]
        enum_data = get_all_items(enum_class_switch[cur_number]['hardware'], verbose=True)
    else:
        enum_data = get_all_items(enum_class_switch[cur_number][cur_value], verbose=True)

    # Get a random value from the enum data the abides by generation rules
    while True:
        # Get a value
        random_key = random.choice(list(enum_data.keys()))
        random_value = enum_data[random_key].lower().replace(' ', '_').replace('-', '_')

        # Check if the value is a tuple and append accordingly
        if isinstance(random_value, tuple):
            temp_settings = copy.deepcopy(cur_settings)
            temp_settings[cur_number].append(random_key.lower().replace(' ', '_').replace('-', '_'))
            temp_settings[cur_number].append(random.choice(random_value))
        else:
            temp_settings = copy.deepcopy(cur_settings)
            temp_settings[cur_number].append(random.choice(random_value))

        # Check if temporary settings passes the rule check
        if pass_rule_check(temp_settings):
            cur_settings = temp_settings
            break

    # Check if there is an exception
    is_exception, cur_settings = check_for_exceptions(cur_settings, cur_value)

    # Check if there is another level
    next_level = search_in_switch(random_value, enum_class_switch)
    if next_level != -1 and not is_exception:
        is_exception, cur_settings = auto_fill_types(
            cur_value=random_value, cur_number=next_level, cur_settings=cur_settings
        )

    # Return if not
    return is_exception, cur_settings
    
"""