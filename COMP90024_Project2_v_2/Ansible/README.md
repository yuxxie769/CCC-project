
### Ansible
All-in-one deployment script
May need to adjust python path in *set_env.sh* to your own python path
```
../deployment.sh
```

-----------------------------
### Each step for deployment
#### 1. Make instances on MRC
direct to *Ansible/* directory and run *./mkins.sh* script, use openstack pwd:
```
YTVmMmRkMzU4MDM0NzNh
```

#### 2. Set enviornment on remote servers
including set proxy and mount volume to filesystem
```
./set_env.sh
```

#### 3. Setup database server
pull couchDB from docker hub and excute script
```
./set_dbserver.sh
```

#### 4. Upload data and add to database
upload tweet data into instance, add each record to database
implement MapReduce function for each database
```
./set_data.sh
```

#### 6. Start backend and frontend server
upload data.zip including frontend and backend
unzip and start services
```
./set_webserver.sh
```
