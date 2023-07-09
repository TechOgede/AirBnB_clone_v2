#!/usr/bin/python3
#Fabric script that generates a .tgz archive from th contents of AirBnb_clone_v2/web_static



from fabric.api import *
from datetime import datetime

def do_pack():
	''' Generates .tgz archive '''
	time = datetime.now().strftime("%Y%m%d%H%M%S")
	archive_name = "web_static_" + time + ".tgz"
	local("mkdir -p versions")
	res = local("tar -cvzf versions/" + archive_name + " web_static")

	if res.succeeded:
		print(res)
		return 'versions/' + archive_name + '.tgz'
