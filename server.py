#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.operations import get, put
from fabric.contrib.files import upload_template, exists
from fabvenv import virtualenv
from jinja2 import Template

from config.settings import *

VHOST_NAME = APP_NAME
NGINX_VHOST_DIR = '/etc/nginx/conf.d/'
SUPERVISOR_DIR = '/etc/supervisor/conf.d/'
GUNICORN_CONFIG_FILE=os.path.join(CONFIG_DIR,"gunicorn-conf.py")

# Templates
def _render_template(string, context):
    """ Parse template for config files using Jinja2"""
    return Template(string).render(context)

def make_supervisor_conf():
    """ Create supervisor conf file on the specified host """
    # print USGWI_CONFIG_FILE

    supervisor_context={
        'domain': VHOST_NAME,
        'log' : LOG_DIR,
        'app_dir' : CODE_DIR,
        "gunicorn_conf" : GUNICORN_CONFIG_FILE,
        "venv_path"      : VIRTUALENV_PATH,
        "application" : APP_MAIN_FILE
    }

    if not exists(SUPERVISOR_DIR):
        sudo('mkdir -p %s' % SUPERVISOR_DIR)

    upload_template("templates/supervisor.tpl", "%s%s.conf"%(SUPERVISOR_DIR,VHOST_NAME), context=supervisor_context, use_jinja=True, use_sudo=True,backup=False)

def make_nginx_vhost():
    """ Create config file for NGINX """
    nginx_context={
        'domain': VHOST_NAME,
        'root': CODE_DIR,
        'log' : LOG_DIR,
        'static': STATIC,
        'socket':USGWI_SOCKET,
        "port" : WEBPORT
    }

    nginx_config_file_path =  "%s%s"%(NGINX_VHOST_DIR,VHOST_NAME)
    # print nginx_config_file_path

    upload_template("templates/nginx.tpl",nginx_config_file_path , context=nginx_context, use_jinja=True, use_sudo=True, backup=False)

def make_gunicorn_conf():
    """ Create config for gunicorn """

    gunicorn_context={
        'pid' : TOPOGRAM_PID,
        'log' : LOG_DIR,
        'webport' : WEBPORT
    }

    upload_template("templates/gunicorn.tpl",GUNICORN_CONFIG_FILE, context=gunicorn_context, use_jinja=True, use_sudo=True,backup=False)

def create_dirs():
    """ Create needed directories """
    run('mkdir -p %s' % LOG_DIR)
    run('mkdir -p %s' % CONFIG_DIR)
    run('mkdir -p %s' % RUN_DIR)
    sudo('chown -R www-data:www-data %s' % RUN_DIR)

def create_logs():
    """ Create log files and directories """

    sudo('touch %s/access.log' % LOG_DIR)
    sudo('touch %s/error.log' % LOG_DIR)
    sudo('chown -R www-data:www-data %s' % LOG_DIR)

# supervisor and nginx
def install_gunicorn():
  with virtualenv(VIRTUALENV_PATH):
    run("pip install gunicorn==0.16.1")

def reload_supervisor():
    sudo("sudo service supervisor restart")

def start_app():
    """ Start app using supervisor"""
    reload_supervisor()
    sudo('supervisorctl start %s' % VHOST_NAME)

def restart_app():
    """ Restart app using supervisor"""
    reload_supervisor()
    sudo('supervisorctl restart %s' % VHOST_NAME)

def stop_app():
    """ Stop app using supervisor"""
    sudo('supervisorctl stop %s' % VHOST_NAME)

def restart_webserver():
    """ Restart Nginx"""
    sudo("service nginx restart")

def restart():
    """ Reload config and restart app """
    restart_app()
    restart_webserver()

# main command
def setup_server():
    """ Create config files and restart app"""

    install_gunicorn()
    create_dirs()
    create_logs()

    make_gunicorn_conf()
    make_supervisor_conf()
    restart_app()

    make_nginx_vhost()
    restart_webserver()
