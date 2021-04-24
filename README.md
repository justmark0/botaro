##Test task to create backend of site to register bots in telegram

To start it you should download this repository. Then you have 2 options:

First is to install it just using python:

```
pip install -r requirements.txt
python ./backend/main.py
```

Second option is to use docker. Simply type ```docker-compose up``` and it will start.


Also, you can specify environment variables:
You can create ```.env``` file in ```backend``` folder.
You may specify security data in it if you will not do this it will use default values what is not secure:
```
SECRET_KEY = 32 symbol random string
SALT = salt to use it in passwords
```
You may create secret key using ```openssl rand -hex 32```