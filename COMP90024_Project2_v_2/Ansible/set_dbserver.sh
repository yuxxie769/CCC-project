#!/bin/bash

. ./unimelb-comp90024-2021-grp-68-openrc.sh; ansible-playbook -i inventory/inventory.ini set_dbserver.yaml 