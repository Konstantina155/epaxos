if [ -z "$1" ]; then
    echo "Usage: $0 <replicas>"
    exit 1
fi

../bin/master -N $1 &