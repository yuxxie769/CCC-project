#!/bin/bash
cd Ansible
./set_env.sh < ./password.txt
./set_dbserver.sh < ./password.txt
./set_data.sh < ./password.txt
./set_webserver.sh < ./password.txt
