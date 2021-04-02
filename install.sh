#!/bin/bash
#Tools Installation
#colours
c='\e[36m'
g='\e[92m'
e='\e[0m'

echo -e "$c"
figlet -f big Installing
echo -e "$e"

apt install python -y
apt install python2 -y
pkg install git -y
pkg install php -y
pkg install python3 -y

