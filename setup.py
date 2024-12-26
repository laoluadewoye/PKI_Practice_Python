from setuptools import setup, find_packages

with open("requirements.txt", 'r') as req_file:
    requirements = req_file.read().splitlines()

setup(
    name="Py PKI Practice",
    version="0.4.1",
    description="A project that, given two input files, can simulate the usage of a Public-Key Infrastructure while "
                "devices communicate with each other.",
    author='Laolu Adewoye',
    author_email='laoluadewoye@gmail.com',
    readme='README.md',
    requires_python='>=3.12',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
    license='MIT',
    url='https://github.com/laoluadewoye/PKI_Practice_Python',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': ['run-pki-practice = PKIPractice:basic_check']
    }
)
