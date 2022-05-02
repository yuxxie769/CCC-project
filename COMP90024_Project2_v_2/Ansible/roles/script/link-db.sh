#!/bin/bash
echo "===== Linking Databse Cluster ====="
echo "\n"
echo "===== Setting Environmental Varibles ====="

export declare -a nodes=(172.26.132.118 172.26.133.73 172.26.132.112)
export masternode=`echo ${nodes} | cut -f1 -d' '`
export declare -a othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user='adm1n_c0uchd6'
export pass='_gr0up68H1_'
export VERSION='3.1.1'
export cookie='fckcouchdb'

echo "===== Enabling Cluster on Master Node ====="

for node in ${othernodes} 
do
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json"\
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
             \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\",\
             \"remote_node\": \"${node}\", \"node_count\": \"$(echo ${nodes[@]} | wc -w)\",\
             \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"
done

echo "===== Adding Nodes on Master Node ====="

for node in ${othernodes}
do
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
      --header "Content-Type: application/json"\
      --data "{\"action\": \"add_node\", \"host\":\"${node}\",\
             \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
done

curl -XGET "http://${user}:${pass}@${masternode}:5984/"

echo "===== Finishing Cluster Setting ====="

curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"

echo "===== Checking Nodes States on Each Node ====="

for node in "${nodes[@]}"; do  curl -X GET "http://${user}:${pass}@${node}:5984/_membership"; done

echo "===== Linking Database Cluster Done ====="