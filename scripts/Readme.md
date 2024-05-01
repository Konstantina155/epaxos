Implementation details
======

# Amazon Setup
## Configurations
### Instance type (select one of the below)
- t2.medium
    - 2 vCPU
    - 24 CPU Credits / hour
    - 4 GiB Memory
- t2.large
    - 2 vCPU
    - 36 CPU Credits / hour
    - 8 GiB Memory
### Number of EC2 Instances (see below)
### Network settings: Secure Shell (SSH)
### OS: Ubuntu Linux 11.10

## Preserving the budget
- Close running instances + Elastip IP addresses
- Use an Elastip IP to keep it after an instance is stopped and delete it *before ending lab*
- Use https://calculator.aws/#/ to estimate the cost

## Using SSH to Connect
- Step 1: Change the permissions in the pem file
 ```bash
cd ~/Downloads
chmod 400 filename.pem
 ```
- Step 2: **Instances** -> Click the instance -> *Descriptions* tab -> Copy the **IPv4 Public IP** value
- Step 3: Ssh to the chosen instance
 ```bash
ssh -i filename.pem ec2-user@public_ip
 ```

# Implementation
## Plays a beep sound when all client processes are finished

## Table 1 (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
### NP (No-pipelined with big commands)
#### Epaxos (epaxos_enabled=true), Multi-Paxos (epaxos_enabled=false) and Mencius (mencius_enabled=true)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 2 false true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 3 2 20000 100 true 1 2 -1 np_epaxos
 ```

### (pipelined with small commands)
#### Epaxos (epaxos_enabled=true), Multi-Paxos (epaxos_enabled=false) and Mencius (mencius_enabled=true)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 4 false true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 3 2 20000 50 true 1 30 0 p_epaxos
 ```

Analyze the results in the `logs/` folder and create the table:
 ```bash
python3 create_table1.py
 ```

The table will look like this: <br>
![Alt text](results/table1.png)

## Figure 4 (Batching small commands)
### 4a & 4b (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
#### Clients=20,40,60,80,100,200,300,400,500
##### Epaxos (epaxos_enabled=true and c=0), Epaxos (epaxos_enabled=true and c=100) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 4 false true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 3 20 20000 50 true 10 30 0 batching_epaxos0
 ```

### 4c represents the plot with 5 replicas and 99%ile Latency (ms) in y axis <br>
### 4d modified a bit (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
#### Clients=20,40,60,80,100,200,300,400,500
##### Epaxos (epaxos_enabled=true and c=0), Epaxos (epaxos_enabled=true and c=100) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** <br>
 ```bash
./run_master.sh 5
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 5 4 false true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 5 20 20000 50 true 10 30 0 batching_epaxos0
 ```

## Figures from EPaxos (No-Batching small commands)
### 8 (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
#### Clients=20,40,60,80,100,200,300,400,500
##### Epaxos (epaxos_enabled=true and c=0), Epaxos (epaxos_enabled=true and c=25), Epaxos (epaxos_enabled=true and c=100), Mencius (mencius_enabled=true and c=0 and thrifty=false), Mencius (mencius_enabled=true and c=100) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 4 true true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 3 20 20000 50 true 1 30 0 batching_epaxos0
 ```

### IF I have the budget for an extra plot
### 10 (4 EC2 instances, 1 for the master + a server, 2 for servers and 1 for the client)
### A replica fails, the leader replica fails for Multi-Paxos, achieve 10000 throughput (reqs/sec) for all of them
##### Epaxos (epaxos_enabled=true), Mencius (mencius_enabled=true) and Multi-Paxos (epaxos_enabled=false)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 4 true true false
 ```
- run_client **replicas** **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 3 observe_from_previous_plots 20000 50 true 1 30 0 failed_replica_epaxos0
 ```