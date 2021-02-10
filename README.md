# DevOps Apprenticeship: Project Exercise

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using PowerShell)
```powershell
$ .\setup.ps1
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
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

When running `setup.sh`, the `.env.template` file will be copied to `.env` if the latter does not exist.

### Run on Vagrant as VM
```bash
$ vagrant up
$ vagrant provision
$ vagrant up --provision

Some usable commands: 
$ vagrant reload (to restart/stop app)
$ vagrant ssh
$ vagrant suspend

```

### Run on Docker commands:
```bash
$ docker build --tag rohanraj14/todo-app .
$ docker run -p 5000:5000 --env-file .env rohanraj14/todo-app
```


### Run on Docker as VM commands:
#### 1. Run and Build for local dev environment
```bash
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source=/.,target=/app rohanraj14/todo-app:dev
$ docker build --target development --tag rohanraj14/todo-app:dev .
```
#### 2. Run and Build for production environment
```bash
$ docker run --env-file ./.env -p 5000:5000 --mount type=bind,source=/.,target=/app rohanraj14/todo-app:prod
$ docker build --target production --tag rohanraj14/todo-app:prod .
```