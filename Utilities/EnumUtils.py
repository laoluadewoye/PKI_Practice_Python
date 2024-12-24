from enum import StrEnum, auto


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
