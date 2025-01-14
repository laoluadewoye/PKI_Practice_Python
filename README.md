# Welcome to PyPkiPractice!

## Project Links

### - [GitHub Repository](https://github.com/laoluadewoye/PKI_Practice_Python)
### - [PyPI Package](https://pypi.org/project/PyPkiPractice/)
### - [DockerHub Repository](https://hub.docker.com/r/laoluade/pypkipractice)

## Introduction

Hi! This Project is under development. Back in version 0, I was talking about how I spent most of the time just
planning and writing notes and making sure everything is laid out before me before actually doing code. Back in version
1, I then focused mainly on setting up the automation with GitHub actions, creating releases, tightening up 
deployment environments, and then finally developing some of the actual classes I need for the project.

We are now in version 2! I have a working network (without all the communication yet) and it is fully realized, tested,
and ready for several versions of Python. It was a pain to get it all together, but we are full steam ahead on code! 
One of my main goals is to "get it right the first time." Even if I wind up working in a place that prides itself on
CI, being able to fully realize a project without mistakes is just satisfying as heck, and has forced me to learn alot
more about programming than I knew just a month ago.

For now, here is a basic idea of the project. I wanted to learn PKI architecture, how it's used, and do that while
doing some more advanced stuff with the project in Python. The final goal for the program is that, given a 
configuration file in one of the supported formats, it would create a simulation of a network of Certificate 
Authorities and End-Certificate devices where communication between end devices are encrypted, signed, and supported by
a Public Key Infrastructure. The supported formats are YAML, JSON, TOML, and XML. The final output of this program is
a CSV log file, but during it's run time you should be able to view all the action printed out in the terminal (and 
maybe even a GUI once I finish the program itself).

This program is developed in Python 3.12, but has support for Python 3.8-3.14. Currently, the only drawback is that any 
interpreter that is earlier than Python 3.10 is unable to use YAML files for configuration, and will have to use one of 
the other three supported formats. The code will let you know that.

Use the NOTES.md file to get a deeper idea about what this project is about, and the CONFIG_GUIDE.md file to understand 
how to create the configuration files yourself.

Below are basic instructions on how to install the project and use it, whether that be from the command line, a Python 
IDE, or a Docker container. As you can see, I put alot of work into making this easy for future me and anyone else. 
"It runs on my laptop," amirite?

Also, for a sense of structure, auto configurations create the underlying environment, and manual configurations are
to specify the information about specific authorities and end devices. **Always pass the autoconfiguration first, or 
else it will yell at you. The manual configuration is optional if you don't want to use customization.**

The instructions below does assume you know what Python, Pip, IDEs, and Docker are.

# Installation

You can download the repo from GitHub and work with the project in your desired IDE. PKIPractice has a file called
RunConfig.py which can be used to run the program. However, if you wish to use the installed command line program, then
the following sections show you how to install to either your local environment or a docker image storage.

## Python Install with Pip

`pip install PyPkiPractice`

## Docker Image Pull

`docker pull laoluade/pypkipractice:latest`

# Usage

## Don't have configurations? And additional options

No worries! There are some options you can pass instead of the files I use for examples below.

* `-h` or `--help`: Get help on how to use the program.
* `-d` or `--default`: Run the program using a default configuration built into the program.

There is also a folder of default configurations added to the project called "Default_Configs." In it, are annotated
examples of autoconfiguration and manual configuration files in JSON, YAML, TOML, and XML. You can pass those files
as arguments and experiment with them to your heart's content.

Other options you can pass into the program are-

* `-t` or `--test`: Run the program in test mode, which caps what parts of the program run to only the ones needed for
  automated testing. You can try it, but it's really only for use in pytest and nox.

## Running in an IDE from project root

Command Structure: python PKIPractice/RunConfig.py _(arguments)_

Command Example: `python PKIPractice/RunConfig.py config_files/config_auto.json config_files/config_manual.json`

If you're in an IDE, chances are you can just set up a run configuration in your app. Make sure to add arguments in
whatever field you need as I told my program to yell at you if you don't.

## Running as a command line executable in cmd, bash, or powershell

Command Structure: run-pki-practice _(arguments)_

Command Example: `run-pki-practice config_files/config_auto.json config_files/config_manual.json`

## Running as a Docker Container from the pulled Docker image

If you have docker installed, you are able to run the program as a container without installing anything.

### Basic run

First, there is running the docker container "naked" without any additional options passed to the run command.

Command Structure: docker run laoluade/pypkipractice:_(tag)_

Command Example: `docker run laoluade/pypkipractice:latest`

The docker container is automatically to use the "--default" option if no arguments are passed to the container
environment. This way, you are able to see the example of what it would look like for the program to run.

### Mounted run (output only)

Next, there is mounting a folder as a volume to the docker. This way, you can save the CSV log file locally and access
it. To do this, you will just have to connect a folder to the `/usr/local/app/` directory that the container operates
in. 

Command Structure: docker run -v _(local_output_folder_path)_:/usr/local/app/:ro laoluade/pypkipractice:_(tag)_

Let's say for example, that you had an output folder called _"output"_ you would want to receive the output. Use the 
following command:

Command Example: `docker run -v output:/usr/local/app/:ro laoluade/pypkipractice:latest`

### Mounted run (full)

Lastly, there is mounting a local folder that _also_ contains configuration files for the program that you want to send
into the container. The strategy is the same, but for safety, made the container folder a subdirectory of the `app`
directory. You can even write the log filepath in a way where the log saves in the subdirectory, making it accessible
to you on your hard drive.

Command Structure: docker run -v _{local_config_folder_path}_:/usr/local/app/_{container_config_folder_path}_:ro 
laoluade/pypkipractice:_(tag) (arguments)_

Let's say that you had a folder called config_files, which had a file called **config_auto.json** and **config_manual.json**.
You wished to expose this information to the docker container, so you can run your own custom configuration.

Command Example: `docker run -v config_files:/usr/local/app/config_files:ro laoluade/pypkipractice:latest 
config_files/config_auto.json config_files/config_manual.json`

In this example-

* **"docker run"** is the basic subcommand that will be used to run the chosen image. 
* The **"-v"** flag is used to mount the local config folder as a volume to the container's config folder. 
* **"config_files"** is the name of the local config folder.
* **"/usr/local/app/config_files"** is the path to the container's config folder.
  * The container is run in /usr/local/app, so be cognisant of that when deciding where to mount your files.
* The **"-ro"** flag is used to make the files you mount read only.
* **"laoluade/pypkipractice:latest"** is the name of the image you would pull.
  * **"latest"** is the tag of the image you would pull, which defaults to the most recent image in the repo.
* The last part of the command is the arguments you passed to the command line after stating your image. The container
  will take care of handling the arguments for you. Filepaths must be from the perspective of the container working in
  the app directory.
  * **"config_files/config_auto.json"** is the path to the autoconfiguration file.
  * **"config_files/config_manual.json"** is the path to the manual configuration file.

## Table comparing options

Here is a table comparing how each strategy compares. These are my best guess of how easy it would be for someone to
use an option if they didn't have any experience. I hope this table helps you decide which one to try.

|       Metric        | Python Interpreter | Installed CLI | Docker Container |
|:-------------------:|:------------------:|:-------------:|:----------------:|
|    GUI App Usage    |        Best        |     Worst     |      Medium      |
|    Simple to Use    |        Best        |     Best      |      Worst       |
| Machine Independent |       Medium       |    Medium     |       Best       |
| Source Code Access  |        Best        |    Medium     |      Worst       |
|     Secure Run      |       Medium       |     Worst     |       Best       |
| Reproducible Result |       Worst        |    Medium     |       Best       |
| Uses Few Resources  |       Medium       |    Medium     |       Best       |