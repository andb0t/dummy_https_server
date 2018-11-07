# Dummy HTTP(S) server

A simple test setup to play with authentication.


## HTTP setup

Simply run the app as root with
```
export PORT=80
python app.py
```
If you are not root, you may let root reroute the traffic, as explained e.g. [here](https://serverfault.com/questions/112795/how-to-run-a-server-on-port-80-as-a-normal-user-on-linux)


## HTTPS setup

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
