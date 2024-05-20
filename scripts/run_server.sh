if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <gomaxprocs> <thrifty> <epaxos_enabled> <mencius_enabled>"
    exit 1
fi

gomaxprocs=$1
thrifty=$2
epaxos_enabled=$3
mencius_enabled=$4

# fill with master_ip (private) and machine_ip (private)
../bin/server -maddr "..." -addr "..." -p $gomaxprocs -thrifty=$thrifty -e=$epaxos_enabled -m=$mencius_enabled &
