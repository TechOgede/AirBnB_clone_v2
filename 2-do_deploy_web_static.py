#!/usr/bin/python3
'''Fabric script that distributes the
.tgz archive to web-01 and web-02
'''

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.25.156.15', '100.25.36.199']


def do_pack():
    ''' Generates .tgz archive '''
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + time + ".tgz"
    local("mkdir -p versions")
    res = local("tar -cvzf versions/" + archive_name + " web_static")

    if res.succeeded:
        print(res)
        return 'versions/' + archive_name + '.tgz'


def do_deploy(archive_path):
    ''' Distributes the generated archive to the webservers'''
    if not os.path.exists(archive_path):
        return False

    upload = put(archive_path, '/tmp/')

    archive_and_ext = os.path.basename(archive_path)
    archive = os.path.splitext(archive_and_ext)[0]

    unzipped_path = '/data/web_static/releases/' + archive

    res = run('mkdir -p ' + unzipped_path +
              ' && ' + 'tar -xvzf /tmp/' + archive_and_ext +
              ' -C ' + unzipped_path +
              ' && ' + 'rm -f /tmp/' + archive_and_ext +
              ' && ' + 'mv ' + unzipped_path + '/web_static/* ' +
              unzipped_path +
              ' && ' + 'rm -rf ' + unzipped_path + '/web_static' +
              ' && ' + 'rm -rf /data/web_static/current' +
              ' && ' + 'ln -s ' + unzipped_path +
              ' /data/web_static/current')

    if res.succeeded and upload.succeeded:
        return True
    return False
