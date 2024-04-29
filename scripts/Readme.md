Implementation details
======

### Table 1
#### NP (No-pipelined)
##### Epaxos (epaxos_enabled=true), Multi-Paxos (epaxos_enabled=false) and Mencius (mencius_enabled=true)
- run_master <replicas>
    ./run_master.sh 3
- run_servers <replicas> <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>
    ./run_server.sh 3 2 false true false
- run_client <clients> <requests> <writes> <epaxos_enabled> <batch_size> <GOMAXPROCS> <conflicts> <filename>
    ./run_client.sh 2 20000 100 true 1 2 -1 np.txt
- analyze the results after client finishes
    python3 latency_analysis.py <filename>
    python3 throughput_analysis.py <filename>

#### (pipelined)
##### Epaxos (epaxos_enabled=true), Multi-Paxos (epaxos_enabled=false) and Mencius (mencius_enabled=true)
- run_master <replicas>
    ./run_master.sh 3
- run_servers <replicas> <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>
    ./run_server.sh 3 4 false true false
- run_client <clients> <requests> <writes> <epaxos_enabled> <batch_size> <GOMAXPROCS> <conflicts> <filename>
    ./run_client.sh 2 20000 50 true 1 30 0 p.txt
- analyze the results after client finishes
    python3 latency_analysis.py <filename>
    python3 throughput_analysis.py <filename>