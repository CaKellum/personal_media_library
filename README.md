# Personal Media Library Flask Website
This is a specific solution that I use to track and maintain my growing collection of media from music to video games  
  
I can see this being most useful for thoes that want to see a working example of a flask app, but if you choose to clone and implement this solution then have at it.
## How to run dev environment
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
## External Resources
[Flask Website](https://flask.palletsprojects.com/en/2.2.x/)
[Python](https://www.python.org/)