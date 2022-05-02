 #！/bin/bash

sudo docker stop webapp
sudo docker rm webapp
sudo docker image rm frontend_image
sudo docker build -t frontend_image .
sudo docker run -p 80:80 -d --name webapp frontend_image