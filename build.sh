unset GOPATH
export GOPATH=$PWD
echo "GOPATH=$GOPATH"
go install master
go install client
go install server