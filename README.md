# Dummy HTTPS server

A simple test setup to play with authentication.

## Setup

### Install nginx
Centos7:
```
sudo yum install epel-release  # add the repo
sudo yum install -y nginx  # install nginx
sudo systemctl start nginx  # start nginx

```
If firewall:
```
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
```
Now you should be able to contact the service from outisde: http://YOUR_PUBLIC_IP_OR_DOMAIN
