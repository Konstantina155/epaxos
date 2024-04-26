if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <number_of_clients> <number_of_requests> <batch_size>"
    exit 1
fi

num_clients=$1
num_req=$2
batch_size=$3
rounds=$((num_req / batch_size))

for((c = 1; c <= $num_clients; c++))
do
  ../bin/client -maddr ${MASTER_SERVER_IP} -q $num_req -e=true -r $rounds &
#> logs/C-$c.out 2>&1 &
done