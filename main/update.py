#!/bin/bash
#Script Update
#Starts Here

import os
import requests
import time


#Colours
R='\033[1;31m'
C='\033[1;36m'
G='\033[1;92m'
E='\033[0m'
REQUEST = requests.get("https://raw.githubusercontent.com/Zaeem20/VirusX5/master/.version").text


def get_version() -> float:
    with open('./.version') as file:
        version = file.read().strip()
        return float(version)


                                #INTRO

print(G)
print('''
                  _  _  ___  ___   __  ____  ___
                 ( )( )(  ,\(   \ (  )(_  _)(  _)
                  )()(  ) _/ ) ) )/__\  )(   ) _)
                  \__/ (_)  (___/(_)(_)(__) (___) v 1.0''')
print(E)

time.sleep(1.5)
print(f"{R}                         ChecKing For Update {E}")
if float(REQUEST) > get_version():
    print(f"{G}                          Update Found!!!   {E}")

    time.sleep(1.5)
    answer = input('\n\033[1;92m[\033[0m\033[1;77m*\033[0m\033[1;92m] Would You Like To Update VirusX5 Y/n: \033[0m').lower()
    if answer == 'y':
        os.system('git checkout . && git pull ')
        print('Updated successfully')
    elif answer == 'n':
        print(f'{R}Aborting Update{E}')

else:
    print(f"{R}                          No Update Found!!!   {E}")
