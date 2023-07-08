#!/usr/bin/env bash
#Sets up web-01 and web-02 for the deployment of web_static

#upgrade packages and install nginx
if ! dpkg -s nginx &> /dev/null; then
    apt update
    apt upgrade
    apt -y install nginx
fi

#create the necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared

#create 'fake' HTML
echo -e '<!DOCTYPE html>\n<html lang="en"><body>Testing 1, 2, 3</body></html>' > /data/web_static/releases/test/index.html

#create a sym link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#gives ownership of /data/ to ubuntu user and group
chown -R ubuntu:ubuntu /data

#Configure Nginx to serve the content of the symlink to hbnb_static
sed -i 's|^[^#].*location / {$|\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;|' /etc/nginx/sites-available/default

#Restart nginx
service nginx restart

