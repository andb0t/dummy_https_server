# Dummy HTTP(S) server

A simple test setup to play with authentication.


## HTTP setup

Simply run the app as root with
```
python app.py 80
```
or
```
sudo pipenv run python app.py 80
```
If you are not root, you may let root reroute the traffic, as explained e.g. [here](https://serverfault.com/questions/112795/how-to-run-a-server-on-port-80-as-a-normal-user-on-linux)

Now you should be able to contact the service from outisde: http://YOUR_PUBLIC_IP_OR_DOMAIN
To receive the JSON: http://YOUR_PUBLIC_IP_OR_DOMAIN/api/dummy


## HTTP setup through nginx

### Install nginx
Centos7:
```
sudo yum install epel-release  # add the repo
sudo yum install -y nginx  # install nginx
sudo systemctl start nginx  # start nginx
sudo systemctl enable nginx  # start at system start
# sudo systemctl restart nginx  # restart the service
```
If firewall:
```
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
```
Now you should be able to contact the nginx service from outisde: http://YOUR_PUBLIC_IP_OR_DOMAIN



### Start the app
```
pipenv run python app.py 8080 &
```

### Configure reverse proxy
Now it's time to use nginx as reverse proxy. Allow it to reroute reqeusts:
```
sudo setsebool -P httpd_can_network_connect 1
```
Locate the `/etc/nginx/nginx.conf` file and change this:
```
         location / {
         }
```
to this:
```
         location / {
             proxy_pass http://127.0.0.1:8080;
         }
```
Now restart nginx. You should now be able to contact your app from outisde: http://YOUR_PUBLIC_IP_OR_DOMAIN
