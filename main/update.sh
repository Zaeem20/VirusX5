#!/bin/bash
#Script Update
#Starts Here

#Colours
R='\e[1;31m'
C='\e[1;36m'
G='\e[1;92m'
E='\e[0m'
                             #INTRO

echo -e "$G"
echo '
                  _  _  ___  ___   __  ____  ___
                 ( )( )(  ,\(   \ (  )(_  _)(  _)
                  )()(  ) _/ ) ) )/__\  )(   ) _)
                  \__/ (_)  (___/(_)(_)(__) (___) v 1.0'
echo -e "$E"

sleep 1.5
echo -e "$R                         ChecKing For 2.0 $E"
echo 
sleep 1.5
echo -e "$C                         ChecKing For 2.0 $E"
echo 
sleep 1.5
echo -e "$G                          Update Found!!!   $E"
sleep 1.5
echo 
read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] You are Going To Update VirusX5 Y/n: \e[0m'
if [[ $option == y || $option == Y ]]; then

echo -e "$G                          Updating VirusX5  $E"
cd $HOME
rm -rf VirusX5
git clone https://github.com/Zaeem20/VirusX5
cd VirusX5
unzip VirusX5.zip
chmod +x *

echo -e "$C                        SucessFully Updated VirusX5 $E"
echo 
echo -e "$G                           Returning to VirusX5 $E"
sleep 2.0
bash Virus.sh

else
exit
clear && cd

fi
