#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os
from fabric.api import env
from fabric.operations import run, put, sudo
env.hosts = ['52.90.98.156', '52.207.85.204']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        print(archive_path)
        new_arch = archive_path.split("/")
        new_comp = new_arch[-1]
        new_folder = ("/data/web_static/release/" + new_arch[-1][:-4])
        for ip_add in env.hosts:
            put(archive_path, "/tmp/")
            run("mkdir {}".format(new_folder))
            run("tar -xzf /tmp/{} -C {}".format(new_arch[-1], new_folder))
            run("rm /tmp/{}".format(new_arch[-1]))
            run("mv {}/web_static/* {}".format(new_folder, new_folder))
            run("rm -rf {}/web_static".format(new_folder))
            run('rm -rf /data/web_static/current')
            run("ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False