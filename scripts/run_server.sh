if [ "$#" -ne 6 ]; then
    echo "Usage: $0 <master_ip> <replica_ip> <port> <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>"
    exit 1
fi

master_ip=$1
port=$2
gomaxprocs=$3
thrifty=$4
epaxos_enabled=$5
mencius_enabled=$6

../bin/server -port $port -maddr $master_ip -addr "127.0.0.1" -p $gomaxprocs -thrifty=$thrifty -e=$epaxos_enabled -m=$mencius_enabled &
