if [ -z "$1" ]; then
    echo "Usage: $0 <number_of_replicas>"
    exit 1
fi

../bin/server -port $1 &