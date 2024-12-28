# Placeholder README file

Hi! This Project is under development. I set up the CI/CD pipeline in GitHub first before anything so that I could
automatically test and push out updates to PyPi and Dockerhub. It took a few days to figure out but my system is
pretty much set for any future updates and all I have to do is just push updates to my repo. I'll probably still be
doing a bit more tinkering with GitHub actions but bottom line is that filepath arguments work and automation works and
is dynamic enough as to not flubb up my repo posting system. I hope.

For now, here is a basic idea of the project. I wanted to learn PKI architecture, how it's used, and do that while
doing some more advanced stuff with the project in Python. The final goal for the program is that, given a 
configuration file in one of the supported formats, it would create a simulation of a network of Certificate 
Authorities and End-Certificate devices where communication between end devices are encrypted, signed, and supported by
a Public Key Infrastructure. The supported formats are YAML, JSON, TOML, and XML.

This program is developed in Python 3.12, but has support for Python 3.8-3.14. Currently, the only drawback is that any 
interpreter that is earlier than Python 3.10 is unable to use YAML files for configuration, and will have to use one of 
the other three supported formats. The code will let you know that.

Use the NOTES.md file to get a deeper idea about what this project is about. Below are basic instructions on how to
install the project and use it, whether that be from the command line, a Python IDE, or a Docker container. As you can
see, I put alot of work into making this easy for future me and anyone else. "It runs on my laptop," amirite?

Also, for a sense of structure, auto configurations create the underlying environment, and manual configurations are
to specify the information about specific authorities and end devices. Always pass the autoconfiguration first, or 
else it will yell at you. The manual configuration is optional if you don't want to use customization.

The instructions below does assume you know what Python, Pip, IDEs, and Docker are.

# Installation

## Python install with pip

pip install PyPkiPractice

## Docker Image Pull

docker pull laoluade/pypkipractice:latest

# Usage

## Don't have configurations?

No worries! There are some options you can pass instead of the files I use for examples below.

* -h or --help: Get help on how to use the program.
* -d or --default: Run the program using a default configuration built into the program.

For the docker container specifically, I made sure to have a folder of default configurations added to the container's
data. So you can access a file by specifying the folder "Default_Configs" and the file name. For example, 
Default_Configs/default_auto.json and Default_Configs/default_manual.json.

## Running in an IDE from project root

Command Structure: python PKIPractice/RunConfig.py _{arguments}_

Command Example: python PKIPractice/RunConfig.py _config_files/config_auto.json config_files/config_manual.json_

If you're in an IDE, chances are you can just set up a run configuration in your app. Make sure to add arguments in
whatever field you need as I told my program to yell at you if you don't.

## Running as a command line executable in cmd, bash, or powershell

Command Structure: run-pki-practice _{arguments}_

Command Example: run-pki-practice _config_files/config_auto.json config_files/config_manual.json_

## Running as a Docker Container from the pulled Docker image

Command Structure: docker run -v _{local_config_folder_path}_:/usr/local/app/_{container_config_folder_path}_:ro 
laoluade/pypkipractice:_{tag}_ _{arguments}_

Command Example: docker run -v _config_files_:_/usr/local/app/config_files_:ro laoluade/pypkipractice:_latest 
config_files/config_auto.json config_files/config_manual.json_