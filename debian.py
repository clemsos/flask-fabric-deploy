#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib import files

def cmd_exists(cmd):
  #TODO: some sort of run test of the command perhaps
  return files.exists("/usr/bin/%s" % cmd)

def apt(cmdline):
  if not cmd_exists('aptitude'):
        sudo("apt-get -y install aptitude")
  sudo("aptitude %s" % cmdline)

def apt_install(packages):
    apt("-y install %s" % packages)

def apt_update():
    apt("update")

def apt_upgrade():
    apt_update()
    apt("-y safe-upgrade")

def ssh():
    """ Copy ssh keys on remote server """
    for host in env.hosts:
        local("ssh-copy-id -p %s %s@%s" % (env.port, env.remote_admin, host))

def install_git():
  if not cmd_exists('git'):
      apt_install("build-essential git git-core")
      run("git config --global color.ui true")

def install_nodejs():
  run("source ~/.bashrc")

  if not cmd_exists('node'):
    with cd("/tmp"):
      # get nvm
      run("wget https://raw.githubusercontent.com/creationix/nvm/v0.13.1/install.sh")
      run("bash install.sh")

      # install node
      run("nvm install v0.10.26")
      run("nvm use v0.10.26")
      run("nvm alias default v0.10.26")

      # add to path
      run("echo . ~/.nvm/nvm.sh >> ~/.bashrc")
      run("source ~/.bashrc")

      # run("rm install.sh")


def setup_debian():
    """ Install required software on host """
    # ssh()
    # apt_upgrade()
    # install_git()
    install_nodejs()
