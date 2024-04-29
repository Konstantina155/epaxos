if [ "$#" -ne 8 ]; then
    echo "Usage: $0 <clients> <requests> <writes> <epaxos_enabled> <batch_size> <GOMAXPROCS> <conflicts> <filename>"
    exit 1
fi

filename=$8
if [ -f logs/$filename ]; then
  rm logs/$filename
fi

clients=$1
reqs=$2
writes=$3
epaxos_enabled=$4
batch_size=$5
gomaxprocs=$6
conflicts=$7
rounds=$((reqs / batch_size))

echo "Num_clients:$clients and num_requests:$reqs" >> logs/$filename
for((c = 1; c <= $clients; c++))
do
  ../bin/client -q $reqs -w $writes -e=$epaxos_enabled -r $rounds -p $gomaxprocs -c $conflicts >> logs/$filename &
done
echo "Finished running clients"