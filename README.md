# Personal Media Library Flask Website
## How to run
It is recomended to use a virtual environment while developing  
use thes commands to create and activate
``` zsh
    python3 -m venv venv 
    source venv/bin/activate # on windows you just need to run venv/Scripts/activate
``` 
To get all the dependincies for this project just run this command in the venv
``` zsh
    python3 -m pip install -r requirements.txt # or just pip install -r requirements.txt
```
Will need to set the FLASK_ENV, SECRET_KEY, FLASK_ALL environment variables before running
``` zsh
    export VAR_NAME=VAR_VALUE
```
