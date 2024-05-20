if [ "$#" -ne 7 ]; then
    echo "Usage: $0 <master_ip> <replica_ip> <port> <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>"
    exit 1
fi

master_ip=$1
replica_ip=$2
port=$3
gomaxprocs=$4
thrifty=$5
epaxos_enabled=$6
mencius_enabled=$7

../bin/server -port $port -maddr $master_ip -addr $replica_ip -p $gomaxprocs -thrifty=$thrifty -e=$epaxos_enabled -m=$mencius_enabled &
