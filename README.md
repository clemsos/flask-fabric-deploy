# flask-fabric-deploy

Fabric scripts to deploy projects using Python, Pip, Bower, Gunicorn and Supervisor (tested with Flask on Debian).

## Usage

Edit ```settings.py``` and ```servers.py``` according to your needs

    fab setup_debian 
    fab deploy
    fab setup_server
    fab restart

NB : Your project hould have a ```wsgi.py``` file to run the application

### TODO

* Auto write Flask config file
* Add support for Chef / Ansible
* 
