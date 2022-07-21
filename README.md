# Flask app example

In first time, we need to create a virtual environment. You have 2 way for that.

## Using virtualenv

Install the package
```
apt install virtualenv
```

Create a virtual environment
```
virtualenv venv
```

## Using Python3-env

Install the package
```
apt install python3-venv
```

Create a virtual envirnment
```
python3 -m venv venv
```

## Use this one
```
. venv/bin/activate or source venv/bin/activate
```

## Leave this one
```
deactivate
```

# Install Flask

After we are in the virtual environment, we can install flask
```
pip3 install flask
```

# Create application file
Now we can create *app.py* file, and to have a basic website, use this configuration
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome on your website ! @evanbtc :)</h1>"

if __name__ == '__main__':
	app.run(debug=True)
```

Set variable
```
export FLASK_APP=app/app.py
```

Finally, you can run your application
```
flask run
```

## Create a requirements file
A requirements file is used to store all dependencies used in the application. If you change the environement of your application you can reinstall all dependencies with a simple command.
```
pip3 freeze > requirements.txt
```

For reinstall all dependencies in the new environement
```
pip3 install -r requirements.txt
```

