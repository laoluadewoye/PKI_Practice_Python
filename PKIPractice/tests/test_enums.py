import unittest
import inspect
import random
import string

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

# Personal Modules must be imported after the system path is modified.
from PKIPractice.Utilities import EnumUtils


class TestEnums(unittest.TestCase):
    def test_enum_retrieval(self) -> None:
        """
        Tests the EnumUtils.get_all_items() function
        """
        def get_classes_from_module(module) -> list:
            return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if
                    cls.__module__ == module.__name__]

        enums = get_classes_from_module(EnumUtils)
        for enum in enums:
            self.assertIsNotNone(EnumUtils.get_all_items(enum))
            self.assertIsNotNone(EnumUtils.get_all_items(enum, True))

    def test_enum_default_values(self) -> None:
        """
        Tests that the values returned by EnumUtils.get_all_items() can be worked with.
        """
        def get_classes_from_module(module) -> list:
            return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if
                    cls.__module__ == module.__name__]

        enums = get_classes_from_module(EnumUtils)
        for enum in enums:
            info = EnumUtils.get_all_items(enum, True)
            for enum_name, enum_value in info.items():
                self.assertEqual(enum_value, enum[enum_name].value)

    def test_enum_value_type(self) -> None:
        """
        Tests that all values in EnumUtils are tuples of strings or strings.
        """
        def get_classes_from_module(module) -> list:
            return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if
                    cls.__module__ == module.__name__]

        enums = get_classes_from_module(EnumUtils)
        for enum in enums:
            info = EnumUtils.get_all_items(enum, True)
            for enum_name, enum_value in info.items():
                is_tuple_or_string = isinstance(enum_value, tuple) or isinstance(enum_value, str)
                self.assertTrue(is_tuple_or_string)

                if isinstance(enum_value, tuple):
                    for v in enum_value:
                        self.assertIsInstance(
                            v,
                            str,
                            f'{v} is not a string, it is a {type(v)}. This is in the {enum_name} enum for the '
                            f'{enum.__name__} class.'
                        )

    def test_fail(self) -> None:
        """
        Fuzzing tests that EnumUtils.has_value() returns False for non-existent enums.
        """
        def get_classes_from_module(module) -> list:
            return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if
                    cls.__module__ == module.__name__]

        def generate_random_string(min_length: int = 1, max_length: int = 20) -> str:
            """Generate a random string of random length."""
            length = random.randint(min_length, max_length)  # Random length between min_length and max_length
            return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

        enums = get_classes_from_module(EnumUtils)
        for enum in enums:
            for i in range(10):
                random_string = generate_random_string()
                self.assertFalse(EnumUtils.has_value(enum, random_string), f'Failed with {random_string}')


if __name__ == '__main__':
    unittest.main()
