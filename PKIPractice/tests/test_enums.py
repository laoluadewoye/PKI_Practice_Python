import unittest
import inspect

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

# Personal Modules must be imported after the system path is modified.
from PKIPractice.Utilities import EnumUtils


class TestEnums(unittest.TestCase):
    def test_enum_retrieval(self) -> None:
        def get_classes_from_module(module) -> list:
            return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if
                    cls.__module__ == module.__name__]

        enums = get_classes_from_module(EnumUtils)
        for enum in enums:
            self.assertIsNotNone(EnumUtils.get_all_items(enum))
            self.assertIsNotNone(EnumUtils.get_all_items(enum, True))

    def test_enum_default_values(self) -> None:
        def get_classes_from_module(module) -> list:
            return [cls for name, cls in inspect.getmembers(module, inspect.isclass) if
                    cls.__module__ == module.__name__]

        enums = get_classes_from_module(EnumUtils)
        for enum in enums:
            info = EnumUtils.get_all_items(enum, True)
            for enum_name, enum_value in info.items():
                self.assertEqual(enum_value, enum[enum_name].value)

    def test_enum_value_type(self) -> None:
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


if __name__ == '__main__':
    unittest.main()
