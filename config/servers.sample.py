from fabric.api import *

def staging():
    env.hosts = ['127.0.0.1']
    env.user  = 'junkware'
    env.remote_admin  = 'junkware'
    env.port="2022"
    env.mongo_user = "root"
    env.mongo_host = "localhost"
    env.mongo_db_name = "topogram"
    env.mongo_db_password = "password"

def prod():
    env.hosts = ['127.0.0.1']
    env.user  = 'junkware'
    env.remote_admin  = 'junkware'
    env.port="2022"
    env.mongo_user = "root"
    env.mongo_host = "localhost"
    env.mongo_db_name = "topogram"
    env.mongo_db_password = "password"

