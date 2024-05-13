function verify_go() { 
   go version
}

function build_epaxos() {
    go install master
    go install client
    go install server
}

function allow_exec() {
    chmod +x scripts/*.sh
}

source ~/.bashrc
verify_go
build_epaxos
allow_exec
