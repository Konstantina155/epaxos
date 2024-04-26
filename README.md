EPaxos
======


### Usage of bin/client:
 ```bash
-c int
    Percentage of conflicts. Defaults to 0% (default -1)
-check
    Check that every expected reply was received exactly once.
-e    Egalitarian (no leader). Defaults to false.
-eps int
    Send eps more messages per round than the client will wait for (to discount stragglers). Defaults to 0.
-f    Fast Paxos: send message directly to all replicas. Defaults to false.
-maddr string
    Master address. Defaults to localhost
-mport int
    Master port.  Defaults to 7077. (default 7087)
-p int
    GOMAXPROCS. Defaults to 2 (default 2)
-q int
    Total number of requests. Defaults to 5000. (default 5000)
-r int
    Split the total number of requests into this many rounds, and do rounds sequentially. Defaults to 1. (default 1)
-s float
    Zipfian s parameter (default 2)
-v float
    Zipfian v parameter (default 1)
-w int
    Percentage of updates (writes). Defaults to 100%. (default 100)
 ```

### Usage of bin/server:
 ```bash
-addr string
    Server address (this machine). Defaults to localhost.
-beacon
    Send beacons to other replicas to compare their relative speeds.
-cpuprofile string
    write cpu profile to file
-dreply
    Reply to client only after command has been executed.
-durable
    Log to a stable store (i.e., a file in the current dir).
-e    Use EPaxos as the replication protocol. Defaults to false.
-exec
    Execute commands.
-g    Use Generalized Paxos as the replication protocol. Defaults to false.
-m    Use Mencius as the replication protocol. Defaults to false.
-maddr string
    Master address. Defaults to localhost.
-mport int
    Master port.  Defaults to 7087. (default 7087)
-p int
    GOMAXPROCS. Defaults to 2 (default 2)
-port int
    Port # to listen on. Defaults to 7070 (default 7070)
-thrifty
    Use only as many messages as strictly required for inter-replica communication.
 ```

### Usage of bin/master:
 ```bash
 -N int
    Number of replicas. Defaults to 3. (default 3)
-port int
    Port # to listen on. Defaults to 7087 (default 7087)
```

## Plots

### 2 Bar plots horizontally for each set of commands' size
- Small (16B) commands
- Large (1KB) commands

#### Replicas
- 3

#### Throughut (reqs / sec) on x axis

#### Variants of Paxos on y axis
- EPaxos with 0% conflict
- EPaxos with 25% conflict
- EPaxos with 50% conflict
- EPaxos with 100% conflict
- Mencius
- Multi-Paxos

- EPaxos, slow-acc with 0% conflict
- EPaxos, slow-acc with 100% conflict
- Mencius, slow-acc
- Multi-Paxos, slow-leader

### 2 Bar plots horizontally for each set of commands' size
- Small (16B) commands
- Large (1KB) commands

#### Replicas
- 5

#### Throughut (reqs / sec) on x axis

#### Variants of Paxos on y axis
- EPaxos with 0% conflict
- EPaxos with 25% conflict
- EPaxos with 50% conflict
- EPaxos with 100% conflict
- Mencius
- Multi-Paxos

- EPaxos, slow-acc with 0% conflict
- EPaxos, slow-acc with 100% conflict
- Mencius, slow-acc
- Multi-Paxos, slow-leader

### 2 Line plots for each latency on y axis:
- Median Latency (ms) 
- 99th Percentile Latency

#### Replicas
- 3

#### Batching
- batch_size = 0

#### Throughut (reqs / sec) on x axis

#### Variants of Paxos
- Multi-Paxos
- Mencius with 100% conflict
- Mencius with 0% conflict
- EPaxos with 100% conflict
- EPaxos with 25% conflict
- EPaxos with 0% conflict

### 2 Line plots for each replica set:
- 3 replicas
- 5 replicas

#### Batching
- batch_size = 10

#### 2 Line plots for each latency on y axis:
- Median Latency (ms) 
- 99th Percentile Latency

#### Throughut (reqs / sec) on x axis

#### Variants of Paxos
- Multi-Paxos
- EPaxos with 100% conflict
- EPaxos with 0% conflict
