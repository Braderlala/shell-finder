#!/usr/bin/python3

# Penulis by Braderlala
# selamat mencuba
# IMPORT MODULE

import requests
import os
import sys
import time
# BANNER
input("sila tekan apa2 untuk teruskan ")
os.system("clear")
os.system("cat banner")

# READ FILE PHP.TXT

page=open('php.txt', 'r')
shellbackdoor=page.readlines()
page.close()

# VARIABLE LINK
link=input("\033[0;31mnak links :\033[0m ")
os.system
def getpage() :
    for x in shellbackdoor :
        ap=x.strip()
        linkpage=link+ap
        check=requests.get(linkpage)
        if check.status_code == 200:
            print("\033[32mpage yang dijumpai : "+linkpage)
            break
        elif check.status_code == 404:
            print("\033[34mpage tidak dijumpai : "+linkpage)
            continue
        else:
            print("\033[1;32mGagal oii !!!!")
            break
try:
    os.system
    print("\033[0;34mSila tunggu sekejap \033[0;32m:\033[0m ")
    print("\033[0;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    time.sleep(0.001)
    getpage()
except requests.exceptions.MissingSchema:
    print("\033[34mGagal \033[0m: sila ikut seperti ini https://www.example.com/ or http://www.example.com//")
    sys.exit()
except KeyboardInterrupt:
    print("\033[33mterima kasih sudi menggunakan tool ni")
    sys.exit()
except requests.exceptions.ConnectionError:
    print("\033[0mGAGAL MENGAKSES : "+link)
    print("chek link tu betul ke tidak oi!!")
    sys.exit()
