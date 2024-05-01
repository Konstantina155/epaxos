function install_python() {
    sudo apt update
    sudo apt install -y ${py_ver}
    sudo apt install -y ${py_ver}-pip
    ${py_ver} --version
}

# Installs a version of Golang since Rabia is written in Golang
function install_go() {
    wget -q https://golang.org/dl/${go_tar}
    sudo tar -C /usr/local -xzf ${go_tar}
    rm ${go_tar}
    echo 'export PATH=${PATH}:/usr/local/go/bin' >>~/.bashrc
    echo 'export GOPATH=$PWD' >>~/.bashrc
    echo 'export GO111MODULE="auto"' >>~/.bashrc
    source ~/.bashrc
    go version
}

# Installs pip and numpy for python3. Used for non-pipelined Paxos and EPaxos testing.
function install_numpy() {
    pip install numpy subprocess pandas matplotlib re
}

function build_epaxos() {
    go install master
    go install client
    go install server
}

function allow_exec() {
    chmod +x scripts/*.sh
}

function main() {
    install_python
    install_go
    install_numpy
    build_epaxos
    allow_exec
}

go_tar=go1.10.linux-amd64.tar.gz
py_ver=python3
main