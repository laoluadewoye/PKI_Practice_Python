import sys
from Utilities import parse_config_auto, parse_config_manual

if __name__ == "__main__":
    try:
        # Take in command line arguments
        args = sys.argv

        # Check if there are more than one argument
        assert len(args) > 1, (
            'No configuration file provided.\n' 
            '\t   Please provide a configuration file by '
            'passing the filepath of your file as an command-line argument.\n'
            '\t   Example: python Main.py Default_Configs/default_auto.yaml\n'
        )

        # Check if there is a help flag
        assert args[1] != '-h' and args[1] != '--help', (
            'Help flag detected.\n'
            '\t   Add explanation later.\n'
        )

        # Check if there is a proper argument for the auto generation
        assert 'auto' in args[1], (
            'Invalid configuration filepath provided.\n'
            '\t   Please provide a proper auto configuration file by '
            'passing the filepath of your file as an command-line argument.\n'
            '\t   Example: python Main.py Default_Configs/default_auto.yaml\n'
        )

        # Check if there is a proper argument for the manual settings or if it's just one argument
        only_auto: bool = len(args) == 2
        if only_auto:
            manual_exists: bool = True
        else:
            manual_exists: bool = 'manual' in args[2]
        assert manual_exists is True, (
            'Invalid configuration filepath provided.\n'
            '\t   Please provide a proper manual configuration file by '
            'passing the filepath of your file as an command-line argument.\n'
            '\t   Example: python Main.py Default_Configs/default_auto.yaml Default_Configs/default_manual.yaml\n'
        )

        # Warn if there are more than the two arguments that have been checked
        if len(args) > 3:
            print('Warning: More than two command-line argument provided.\n'
                  '\t Please provide a configuration file by '
                  'passing the filepath of your file as an command-line argument.\n'
                  '\t   Example: python Main.py Default_Configs/default_auto.yaml '
                  'Default_Configs/default_manual.yaml\n')

        # Pass auto argument to ingestion utilities
        env_auto_settings: dict | None = parse_config_auto(args[1])

        # Pass manual argument to ingestion utilities
        if len(args) > 2:
            env_manual_settings: dict | None = parse_config_auto(args[2])
        else:
            env_manual_settings: dict | None = None

        # Replace this with a better settings check
        assert env_auto_settings is not None, (
            'Unparseable configuration file provided.\n'
            '\t   Please ensure that your configuration file exists or is properly created.\n'
            '\t   Use the default configuration files provided in the Default_Configs folder as a guide.\n'
        )

        print(env_auto_settings)

    except AssertionError as e:
        print(f'\nException: {e}')
