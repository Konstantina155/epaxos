Implementation details
======

# Amazon Setup
## Configurations
### Instance type
- t2.medium
    - 2 vCPU
    - 24 CPU Credits / hour
    - 4 GiB Memory
### Number of EC2 Instances (see below)
### Network settings (Security groups):
- epaxos_security_group
    - Default VPC 
    - Inbound rule: All traffic && All ports && 0.0.0.0
    - Outbound rule: All traffic && All ports && 0.0.0.0
- allow ports
    ```bash
    sudo ufw enable
    sudo ufw allow 7070/tcp
    sudo ufw allow 7087/tcp
    ```
### OS: Ubuntu Linux

## Preserving the budget
- Start instances + associate an Elastic IP to each instance (remains the same IP address)
- Close running instances + release Elastip IP addresses
- "End lab" after work is done
- Use https://calculator.aws/#/ to estimate the cost

## Using SSH to Connect
- Step 1: Change the permissions in the pem file
 ```bash
cd ~/Downloads
chmod 400 aws_key.pem
 ```
- Step 2: **Instances** -> Click the instance -> *Descriptions* tab -> Copy the **IPv4 Public IP** value
- Step 3: Ssh to the chosen instance
 ```bash
ssh -i aws_key.pem ubuntu@public_ip
 ```

# Implementation
### Start plotting the Figure 4 of Rabia (batching), then no-batching (Figure 8 - EPaxos) and Replicas availability (Figure 10 - EPaxos)
### Prints a message when all client processes are finished

## Table 1 (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
### NP (No-pipelined)
#### Epaxos
Edit base-profile.sh in each machine

 ```bash
git clone https://github.com/zhouaea/epaxos-single.git && cd epaxos-single
git checkout epaxos-no-pipelining-no-batching
. compileEPaxos.sh

vi runMasterServer.sh
. runMasterServer.sh

vi runServer.sh
. runServer.sh

vi runClient.sh
. runClient.sh > log.out

. calculate_throughput_latency.sh
killall -9 server master client
 ```

#### Multi-Paxos
 ```bash
git checkout paxos-no-pipelining-no-batching
. compilePaxos.sh

vi runMasterServer.sh
. runMasterServer.sh

vi runServer.sh
. runServer.sh

vi runClient.sh
. runClient.sh > log.out

. calculate_throughput_latency.sh
killall -9 server master client
 ```

### P (pipelined)
#### Epaxos
 ```bash

 ```

#### Multi-Paxos
 ```bash
git clone https://github.com/zhouaea/epaxos-single.git && cd epaxos-single
 ```

Analyze the results in the same folder and create the table:
 ```bash
python3.8 create_table.py
 ```

The table will look like this: <br>
![Alt text](results/table.png)

## Figure 4 (Batching small commands)
### 4a & 4b (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
#### Clients=20,40,60,80,100,200,300,400,500
##### Epaxos (epaxos_enabled=true and c=0), Epaxos (epaxos_enabled=true and c=100) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_master.sh 3 4 false true false
 ```
- run_server **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_server.sh 4 false true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
# Modify clients epaxos_enabled conflicts filename
./run_client.sh 3 20 20000 50 true 10 30 0 batching_epaxos0
 ```

### 4c represents the plot with 5 replicas and 99%ile Latency (ms) in y axis <br>
### 4d modified a bit (6 EC2 instances, 1 for the master + a server, 4 for servers and 1 for the client)
#### Clients=20,40,60,80,100,200,300,400,500
##### Epaxos (epaxos_enabled=true and c=0), Epaxos (epaxos_enabled=true and c=100) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_master.sh 5 4 false true false
 ```
- run_server **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_server.sh 4 false true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
# Modify clients epaxos_enabled conflicts filename
./run_client.sh 5 20 20000 50 true 10 30 0 batching_epaxos0
 ```

Analyze the results in the `logs/` folder and create the plots:
 ```bash
python3 create_plots_batching.py
 ```

## Figures from EPaxos (No-Batching small commands)
### 8 (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
#### Clients=20,40,60,80,100,200,300,400,500
##### Epaxos (epaxos_enabled=true and c=0), Epaxos (epaxos_enabled=true and c=25), Epaxos (epaxos_enabled=true and c=100), Mencius (mencius_enabled=true and c=0 and thrifty=false), Mencius (mencius_enabled=true and c=100) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_master.sh 3 4 true true false
 ```
- run_servers **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_server.sh 4 true true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
# Modify clients epaxos_enabled conflicts filename
./run_client.sh 3 20 20000 50 true 1 30 0 batching_epaxos0
 ```

Analyze the results in the `logs/` folder and create the plots:
 ```bash
python3 create_plots_no_batching.py
 ```

### IF I have the budget for an extra plot
### 10 (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
### A replica fails, the leader replica fails for Multi-Paxos, achieve 10000 throughput (reqs/sec) for all of them
##### Epaxos (epaxos_enabled=true), Mencius (mencius_enabled=true) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_master.sh 3 4 true true false
 ```
- run_servers **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
# Modify epaxos_enabled mencius_enabled
./run_server.sh 4 true true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
# Modify clients epaxos_enabled filename
./run_client.sh 3 observe_from_previous_plots 20000 50 true 1 30 0 failed_replica_epaxos0
 ```
