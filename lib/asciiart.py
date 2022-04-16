import platform
import random

def check_platform():
    """A Function for checking whether OS is Windows, Linux , Mac\n
    `For Windows -> False`"""
    if platform.system() == 'Windows':
        return False
    return True

colors = check_platform()

if colors:
    R='\033[1;31m'  # Red
    C='\033[1;36m'  #cyan
    G='\033[1;92m'  #Green
    E='\033[0m'     #End
    RN = random.choice([C,G])  #Random color between C and G
else:
    R = C = G = E = RN = ''

# In future i will add more banner

banner = f'''                        {RN}+{E}{R}--------------------------------------{E}{RN}+{E}
                        {R}|{E}        {R}_{E}                {R}__  __ {E}{G}____{E}  {R}|{E}
                        {R}|{E} {G}__   _{E}{R}(_){E}{G}_ __ _   _ __  {R}\ \/ /{E}{G}/ ___|{E} {R}|{E}
                        {R}|{E} {G}\ \ / / | '__| | | / __| {R}\  /{E}{G}|___  \{E} {R}|{E}
                        {R}|{E} {G} \ V /| | |  | |_| \__ \ {R}/  \{E}{G}  __) |{E} {R}|{E} 
                        {R}|{E} {G}  \_/ |_|_|   \__,_|___/{R}/_/\_\{E}{G}|____/{E} {R}|{E}
                        {RN}+{E}{R}--------------------------------------{E}{RN}+{E}
'''
