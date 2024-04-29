Implementation details
======

## Table 1
### NP (No-pipelined)
#### Epaxos (epaxos_enabled=true), Multi-Paxos (epaxos_enabled=false) and Mencius (mencius_enabled=true)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 2 false true false
 ```
- run_client **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 2 20000 100 true 1 2 -1 np.txt
 ```

### (pipelined)
#### Epaxos (epaxos_enabled=true), Multi-Paxos (epaxos_enabled=false) and Mencius (mencius_enabled=true)
- run_master **replicas** <br>
 ```bash
./run_master.sh 3
 ```
- run_servers **replicas** **gomaxprocs** **thrifty** **epaxos_enabled** **mencius_enabled** <br>
 ```bash
./run_server.sh 3 4 false true false
 ```
- run_client **clients** **requests** **writes** **epaxos_enabled** **batch_size** **GOMAXPROCS** **conflicts** **filename** <br>
 ```bash
./run_client.sh 2 20000 50 true 1 30 0 p.txt
 ```

Analyze the results in the `logs/` folder and create the table:
 ```bash
python3 create_table1.py
 ```

The table will look like this: <br>
![Alt text](results/table1.png)