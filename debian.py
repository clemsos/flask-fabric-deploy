#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

def ssh():
    """ Copy ssh keys on remote server """
    for host in env.hosts:
        local("ssh-copy-id -p %s %s@%s" % (env.port, env.remote_admin, host))

def setup_debian():
    """ Install required software on host """
    ssh()
