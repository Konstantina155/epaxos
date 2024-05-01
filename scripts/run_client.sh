if [ "$#" -ne 9 ]; then
    echo "Usage: $0 <replicas> <clients> <requests> <writes> <epaxos_enabled> <batch_size> <GOMAXPROCS> <conflicts> <filename>"
    exit 1
fi

replicas=$1
clients=$2
reqs=$3
writes=$4
epaxos_enabled=$5
batch_size=$6
gomaxprocs=$7
conflicts=$8
rounds=$((reqs / batch_size))

for((c = 0; c < $clients; c++))
do
    filename=logs/$9-S$replicas-C$clients-r$reqs-b$batch_size-c$conflicts--client$c.out
  ../bin/client -q $reqs -w $writes -e=$epaxos_enabled -r $rounds -p $gomaxprocs -c $conflicts >> $filename &
done
./check_process_finished.sh