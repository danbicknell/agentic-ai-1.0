# agentic-ai-1.0
Initial Experiments with Agentic AI


# VENV
## Create the virtual environment folder:
py - m venv .venv 

## Activate the virtual environment:
source .venv/Scripts/activate

## Deactivate the virtual environment
deactivate

## List pip installed packages (to see what the environment has installed)
py - m pip list 

## Place pip dependencies or requirements into a text file:
py -m pip freeze > filename.txt

## .gitignore:
.venv


## Local environment variables (for storing secrets that should not be checked into Github):
Folder:  .env

    ### Code to Load
    from dotenv import load_dotenv
    load_dotenv() -- loads variables in the .env file


