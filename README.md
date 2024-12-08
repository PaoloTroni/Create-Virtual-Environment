# CVE - Create Virtual Environment for Python

CVE (Create Virtual Environment) is a Python script designed to automate the creation of virtual environments for Python projects on Linux systems. The tool guides the user through setting up a project directory and initializing a virtual environment, streamlining the setup process for Python development.

## Features

    - Automated creation of a project folder in a user-specified or default location.
    - Initialization of a Python virtual environment using venv.
    - Error handling with cleanup for failed setups.
    - User-friendly console interface with color-coded messages using colorama.

## Prerequisites

Ensure the following requirements are met before using the script:

    - Operating System: Linux
    - Python 3 installed
    - venv module available in your Python installation

If any of these requirements are not met, exit the script (CTRL + o) and prepare your system.

## Installation

Clone this repository to your local machine:

git clone https://github.com/PaoloTroni/Create-Virtual-Environment
cd cve-python

## Usage

Run the script directly using Python:

python3 cve.py

### Steps

    1. The script will prompt you to confirm or change the base directory where the project folder will be created.
    2. You will be asked to name your project folder.
    3. The script will create the folder and initialize a virtual environment in it.
    4. Upon successful completion, the virtual environment will be ready for use.

### Error Handling

If an error occurs during the process, the script:

    - Prints an error message.
    - Attempts to clean up by deleting the partially created project folder.
