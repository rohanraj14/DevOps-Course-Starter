# DevOps Apprenticeship: Project Exercise

## Getting started - running without docker in VM locally

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### Use .env.template to create a new .env file
```
$ cp .env.template .env 
```

Get Poetry
```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
Set Source

```
$ source $HOME/.poetry/env
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ poetry install 
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Notes

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like developement mode (which also enables features like hot reloading when you make a file change).
* There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

### Run on Vagrant as VM
```bash
$ vagrant up
```

### Some usable Vagrant commands
```
#If you want to provision and run:

$ vagrant up --provision

#Other commands: 

$ vagrant provision
$ vagrant reload (to restart/stop app)
$ vagrant ssh
$ vagrant suspend
```

### Run on Docker as Container commands:
#### 1. Run and Build for local dev environment
```bash
$ docker build --target development --tag rohanraj14/todo-app:dev .
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source=/.,target=/app rohanraj14/todo-app:dev
```
#### 2. Run and Build for production environment
```bash
$ docker build --target production --tag rohanraj14/todo-app:prod .
$ docker run --env-file ./.env -p 5000:5000  rohanraj14/todo-app:prod
```

### GitPod start docker
```
$ sudo docker-up
```