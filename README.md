# agentic-ai-1.0
Initial Experiments with Agentic AI


# VENV
## Create the virtual environment folder:
py -m venv .venv 

## Activate the virtual environment:
source .venv/Scripts/activate

    source is a shell command designed for users running on Linux (or any Posix, but whatever, not Windows).

    On Windows, virtualenv creates a .bat/.ps1 file, so you should run venv\Scripts\activate instead (per the virtualenv documentation on the activate script).

    Just run activate, without an extension, so the right file will get used regardless of whether you're using cmd.exe or PowerShell.

.venv/Scripts/activate

## Deactivate the virtual environment
deactivate

## List pip installed packages (to see what the environment has installed)
py - m pip list 

## Place pip dependencies or requirements into a text file:
py -m pip freeze > filename.txt

# install files from a list in a text file
pip install -r pip_install.txt

## .gitignore:
.venv
.env


## Local environment variables (for storing secrets that should not be checked into Github):
https://pypi.org/project/python-dotenv/
Folder:  .env

    ### Code to Load dir
    pip install python-dotenv
    from dotenv import load_dotenv
    load_dotenv() -- loads variables in the .env file

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables

    # Code of your application, which uses environment variables (e.g. from `os.environ` or
    # `os.getenv`) as if they came from the actual environment.

    # to retrieve the variable
    import os
    os.getenv("open_oi_api_key")


# Autogen

https://microsoft.github.io/autogen/stable//index.html


