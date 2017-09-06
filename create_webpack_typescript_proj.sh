# http://wiki.bash-hackers.org/howto/getopts_tutorial

### run with sudo access

installer=""
# get the name of the installer, brew or apt-get
if [ -z "$(uname -a | grep Darwin)" ]
then
    installer="apt-get"
else
    installer="brew"
fi

echo "$( which yarn )"

## install yarn if not present, otherwise check to see if outdated (only on osx)
if [ -z "$( which yarn )" ]
then
    echo "yarn is not installed, will install using $installer"
    if [ installer="brew" ]
    then
        brew install yarn --without-node
    else
        curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
        apt-get update
        apt-get install yarn
    fi
else
    if [ installer="brew" ]
    then
        echo "using brew"
        if [ -n "$(brew outdated | grep yarn)" ]
        then
            echo "your yarn installation is outdated, check brew"
            # exit 1
        fi
    fi
fi

new_dir_name=$"$(pwd)/$1"
echo $(echo "creating new directory: $new_dir_name")
mkdir $new_dir_name
cd $new_dir_name
mkdir server
mkdir source
mkdir src
mkdir test
touch README.md
touch webpack.config.js

yarn add webpack-dev-server
yarn add express


