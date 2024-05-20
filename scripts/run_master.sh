if [ "$#" -ne 5 ]; then
    echo "Usage: $0 <replicas> <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>"
    exit 1
fi

replicas=$1
gomaxprocs=$2
thrifty=$3
epaxos_enabled=$4
mencius_enabled=$5

../bin/master -N $replicas &
sleep 0.1
../bin/server -port 7071 -p $gomaxprocs -thrifty=$thrifty -e=$epaxos_enabled -m=$mencius_enabled &
