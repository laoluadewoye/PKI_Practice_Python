import unittest
import subprocess

# Relative pathing from project package
import sys
from os.path import abspath, dirname, basename, curdir

script_dir = dirname(abspath(__file__))

if script_dir in ['PKI_Practice', 'app']:
    sys.path.append(abspath('PKIPractice'))
elif script_dir == 'PKIPractice':
    sys.path.append(abspath(script_dir))
else:
    sys.path.append(abspath('..'))


class TestCLI(unittest.TestCase):
    def setUp(self):
        current_dir = basename(abspath(curdir))
        if current_dir in ['PKI_Practice', 'PKI Practice']:
            self.pyfile = 'PKIPractice/RunConfig.py'
            self.dc_dir = './'
        elif current_dir == 'PKIPractice':
            self.pyfile = 'RunConfig.py'
            self.dc_dir = '../'
        elif current_dir == 'tests':
            self.pyfile = '../RunConfig.py'
            self.dc_dir = '../../'
        else:
            self.pyfile = 'PKIPractice/RunConfig.py'
            self.dc_dir = './'

    def test_help(self):
        result = subprocess.run(['python', self.pyfile, '-h'], capture_output=True)
        print(result)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, b'')

        result = subprocess.run(['python', self.pyfile, '--help'], capture_output=True)
        print(result)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, b'')

    def test_default(self):
        result = subprocess.run(['python', self.pyfile, '-d'], capture_output=True)
        print(result)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, b'')

        result = subprocess.run(['python', self.pyfile, '--default'], capture_output=True)
        print(result)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, b'')

    def test_args(self):
        arg_combos = [
            ['python', self.pyfile, f'{self.dc_dir}Default_Configs/default_auto.yaml'],
            ['python', self.pyfile, f'{self.dc_dir}Default_Configs/default_auto.json'],
            ['python', self.pyfile, f'{self.dc_dir}Default_Configs/default_auto.toml'],
            ['python', self.pyfile, f'{self.dc_dir}Default_Configs/default_auto.xml'],
            [
                'python',
                self.pyfile,
                f'{self.dc_dir}Default_Configs/default_auto.yaml',
                f'{self.dc_dir}Default_Configs/default_manual.yaml'
            ],
            [
                'python',
                self.pyfile,
                f'{self.dc_dir}Default_Configs/default_auto.json',
                f'{self.dc_dir}Default_Configs/default_manual.json'
            ],
            [
                'python',
                self.pyfile,
                f'{self.dc_dir}Default_Configs/default_auto.toml',
                f'{self.dc_dir}Default_Configs/default_manual.toml'
            ],
            [
                'python',
                self.pyfile,
                f'{self.dc_dir}Default_Configs/default_auto.xml',
                f'{self.dc_dir}Default_Configs/default_manual.xml'
            ]
        ]

        for args in arg_combos:
            result = subprocess.run(args, capture_output=True)
            print(result)

            self.assertEqual(
                result.returncode,
                0,
                f'Failed with args: {args}. Full file path: {abspath(self.pyfile)}'
            )
            self.assertEqual(
                result.stderr,
                b'',
                f'Failed with args: {args}. Full file path: {abspath(self.pyfile)}'
            )
