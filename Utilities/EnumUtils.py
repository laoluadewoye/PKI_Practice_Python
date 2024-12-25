from enum import Enum, StrEnum, auto


class SUPPORTED_HASH_ALGS(StrEnum):
    """
    This class contains all supported hash algorithms.
    It is used in the config file to determine which hash algorithms are available to use.
    """
    SHA224 = auto()
    SHA256 = auto()
    SHA384 = auto()
    SHA512 = auto()
    SHA3_224 = auto()
    SHA3_256 = auto()
    SHA3_384 = auto()
    SHA3_512 = auto()
    BLAKE2B = auto()
    BLAKE2S = auto()

    @classmethod
    def has_alg(cls, alg: str) -> bool:
        if alg in (item.value for item in cls):
            return True
        else:
            return False


class SUPPORTED_ENCRYPT_ALGS(StrEnum):
    """
    This class contains all supported encryption algorithms.
    It is used in the config file to determine which encryption algorithms are available to use.
    """
    RSA = auto()
    ECC = auto()

    @classmethod
    def has_alg(cls, alg: str) -> bool:
        if alg in (item.value for item in cls):
            return True
        else:
            return False


class SUPPORTED_ECC_CURVES(StrEnum):
    """
    This class contains all supported curves for eliptic curve cryptography.
    It is used in the config file to determine which ecc curves are available to use.
    """
    SECP256R1 = auto()
    SECP384R1 = auto()
    SECP521R1 = auto()
    SECP224R1 = auto()
    SECP192R1 = auto()
    SECP256K1 = auto()

    @classmethod
    def has_curve(cls, curve: str) -> bool:
        if curve in (item.value for item in cls):
            return True
        else:
            return False


class COMMON_USERS(StrEnum):
    GUEST = auto()
    PERSONAL = auto()
    ENTERPRISE = auto()


class COMMON_ADMINS(StrEnum):
    DOMAIN_ADMIN = auto()
    SCHEMA_ADMIN = auto()
    SERVER_ADMIN = auto()
    NETWORK_ADMIN = auto()
    CLOUD_ADMIN = auto()
    DATABASE_ADMIN = auto()
    AUDITOR = auto()


class COMMON_ACCOUNTS(StrEnum):
    USER = auto()
    ADMIN = auto()


class COMMON_WINDOWS(Enum):
    WINDOWS_2000 = ('Professional', 'Server', 'Advanced Server', 'Datacenter Server')
    WINDOWS_XP = ('Home', 'Professional')
    WINDOWS_VISTA = ('Starter', 'Home Basic', 'Home Premium', 'Business', 'Enterprise', 'Ultimate')
    WINDOWS_7 = ('Starter', 'Home Basic', 'Home Premium', 'Business', 'Enterprise', 'Ultimate')
    WINDOWS_8 = ('Home', 'Pro', 'Enterprise')
    WINDOWS_10 = ('Home', 'Pro', 'Educational', 'Enterprise')
    WINDOWS_11 = ('Home', 'Pro', 'Educational', 'Enterprise')

    @property
    def editions(self) -> tuple:
        return self.value

    @classmethod
    def versions(cls, verbose: bool = False) -> dict | list:
        if verbose:
            ver: dict = {}
            for item in cls:
                ver[item.name] = item.value
        else:
            ver: list = []
            for item in cls:
                ver.append(item.name)
        return ver


class COMMON_WINDOWS_SERVER(Enum):
    WINDOWS_SERVER_2003 = ('Web', 'Standard', 'Enterprise', 'Datacenter')
    WINDOWS_SERVER_2008 = ('Web', 'Standard', 'Enterprise', 'Datacenter', 'Itanium', 'Foundation', 'HPC')
    WINDOWS_SERVER_2012 = ('Foundation', 'Essentials', 'Standard', 'Datacenter')
    WINDOWS_SERVER_2016 = ('Standard', 'Datacenter')
    WINDOWS_SERVER_2019 = ('Standard', 'Datacenter')
    WINDOWS_SERVER_2022 = ('Standard', 'Datacenter', 'Datacenter Azure')

    @property
    def editions(self) -> tuple:
        return self.value

    @classmethod
    def versions(cls, verbose: bool = False) -> dict | list:
        if verbose:
            ver: dict = {}
            for item in cls:
                ver[item.name] = item.value
        else:
            ver: list = []
            for item in cls:
                ver.append(item.name)
        return ver


class COMMON_MICROSOFT(StrEnum):
    WINDOWS = auto()
    WINDOWS_SERVER = auto()


class COMMON_OS(StrEnum):
    MICROSOFT = auto()
    UNIX = auto()
    MOBILE = auto()
    ROUTING = auto()
