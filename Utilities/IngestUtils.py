import yaml
import json
import xmltodict
import tomllib
import re
from .EnumUtils import SUPPORTED_HASH_ALGS, SUPPORTED_ENCRYPT_ALGS


def adjust_types(settings: dict) -> dict or None:
    """
    Adjusts the data types and format of the settings dictionary.

    Args:
        settings (dict): The dictionary to be modified and wrangled.

    Returns:
        dict: The tailored dictionary.
    """
    try:
        settings['level_count'] = int(settings['level_count'])
        settings['count_by_level'] = list(map(int, settings['count_by_level']))
        settings['uid_hash'] = settings['uid_hash'].lower().replace('-', '_')
        settings['sig_hash'] = settings['sig_hash'].lower().replace('-', '_')
        settings['encrypt_alg']['alg'] = settings['encrypt_alg']['alg'].lower()
        settings['encrypt_alg']['params']['pub_exp'] = int(settings['encrypt_alg']['params']['pub_exp'])
        settings['encrypt_alg']['params']['key_size'] = int(settings['encrypt_alg']['params']['key_size'])
        settings['revoc_probs'] = list(map(float, settings['revoc_probs']))
    except (KeyError, TypeError, ValueError) as e:
        return None

    return settings


def validate_settings(settings: dict) -> bool:
    """
    Validates the settings dictionary.

    Args:
        settings (dict): The dictionary to be validated.

    Returns:
        bool: True if the settings are valid, False otherwise.
    """

    # Checking the existence and lengths of lists
    try:
        for setting in [
            settings['count_by_level'], settings['revoc_probs'], settings['cert_valid_durs'],
            settings['cache_durs'], settings['cooldown_durs'], settings['timeout_durs']
        ]:
            if not isinstance(setting, list):
                return False
            if len(setting) != settings['level_count']:
                return False
    except KeyError as e:
        return False

    # Checking existence of untouched strings
    if not settings['uid_hash'] or not settings['sig_hash'] or not settings['encrypt_alg']['alg']:
        return False

    # Checking durations for correct formats
    for dur in settings['cert_valid_durs']:
        if not (re.match(r'^[0-9]+:[0-9]{2}:[0-9]{2}$', dur) or dur == 'none'):
            return False

    for dur in settings['cache_durs']:
        if not (re.match(r'^[0-9]{2}:[0-9]{2}$', dur) or dur == 'none'):
            return False

    for dur in settings['cooldown_durs']:
        if not (re.match(r'^[0-9]+$', dur) or dur == 'none'):
            return False

    for dur in settings['timeout_durs']:
        if not (re.match(r'^[0-9]+$', dur) or dur == 'none'):
            return False

    # Checking if revoc_probs are between 0 and 1 inclusive
    for prob in settings['revoc_probs']:
        if prob < 0.0 or prob > 1.0:
            return False

    # Checking if parameters for hashing and encryption are valid
    if not SUPPORTED_HASH_ALGS.has_alg(settings['uid_hash']):
        return False

    if not SUPPORTED_HASH_ALGS.has_alg(settings['sig_hash']):
        return False

    if not SUPPORTED_ENCRYPT_ALGS.has_alg(settings['encrypt_alg']['alg']):
        return False

    return True


def parse_config_auto(filepath: str) -> dict or None:
    """
    Parses an autoconfiguration file given its file path.

    Args:
        filepath (str): The path to the configuration file to be parsed.

    Returns:
        dict: A dictionary containing the parsed configuration data.
    """

    settings = None

    # Check file type
    assert any(ext in filepath for ext in ['.yaml', '.yml', '.json', '.xml', '.toml']), (
        'Invalid configuration file provided.\n'
        '\t   Please provide a configuration file that is a YAML, JSON, XML, or TOML file.\n'
        '\t   Look in the Default_Configs folder for examples.\n'
    )

    # File type tree
    try:
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            with open(filepath, 'r') as file:
                settings = yaml.load(file, Loader=yaml.Loader)
        elif filepath.endswith('.json'):
            with open(filepath, 'r') as file:
                settings = json.load(file)
        elif filepath.endswith('.xml'):
            with open(filepath, 'r') as file:
                settings = xmltodict.parse(file.read())
                settings = settings['config']
        elif filepath.endswith('.toml'):
            with open(filepath, 'rb') as file:
                settings = tomllib.load(file)
    except Exception as e:
        print(f'Ingestion libraries experienced an error: "{str(e).title()}"')
        return settings

    # Type adjustment
    settings = adjust_types(settings)
    assert settings is not None, (
        'Ingested settings were not able to be adjusted due to incorrect configuration format.\n'
        '\t   Please ensure your configuration file is correctly created.\n'
        '\t   Use the default configuration file as a template.\n'
    )

    # Settings validation
    assert validate_settings(settings) is True, (
        'Ingested settings were not found to be valid.\n'
        '\t   Please ensure your configuration file is correctly created.\n'
        '\t   Use the default configuration file as a template.\n'
    )

    return settings


def parse_config_manual(filepath: str) -> dict or None:
    """
    Parses a manual configuration file given its file path.

    Args:
        filepath (str): The path to the configuration file to be parsed.

    Returns:
        dict: A dictionary containing the parsed configuration data.
    """

    return None
