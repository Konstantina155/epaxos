if [ "$#" -ne 6 ]; then
    echo "Usage: $0 <replica_ip> <port> <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>"
    exit 1
fi

replica_ip=$1
port=$2
gomaxprocs=$3
thrifty=$4
epaxos_enabled=$5
mencius_enabled=$6

../bin/server -port $port -maddr "127.0.0.1" -addr $replica_ip -p $gomaxprocs -thrifty=$thrifty -e=$epaxos_enabled -m=$mencius_enabled &
