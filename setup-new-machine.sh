apt-get install software-properties-common

#rvm repository
apt-add-repository -y ppa:rael-gc/rvm

# update after adding all the additional repositories
apt-get update

apt-get -y install git
apt-get -y install rvm
apt-get -y install curl


#install pyenv
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash


### installing tmux
TMUX_VERSION=2.5
apt-get -y install wget 
apt-get -y install tar 
apt-get -y install libevent-dev
apt-get -y install libncurses-dev
wget https://github.com/tmux/tmux/releases/download/${TMUX_VERSION}/tmux-${TMUX_VERSION}.tar.gz
tar xf tmux-${TMUX_VERSION}.tar.gz
rm -f tmux-${TMUX_VERSION}.tar.gz
cd tmux-${TMUX_VERSION}
./configure
make
sudo make install
cd -
sudo rm -rf /usr/local/src/tmux-*
sudo mv tmux-${TMUX_VERSION} /usr/local/src



