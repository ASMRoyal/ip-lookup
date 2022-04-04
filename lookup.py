# TOOL BY ASM_Royal
import requests
import socket
import time
from colorama import Back, Fore

Blue = Fore.LIGHTBLUE_EX
Green = Fore.LIGHTGREEN_EX
Red = Fore.LIGHTRED_EX
Yellow = Fore.LIGHTYELLOW_EX
Purple = Fore.LIGHTMAGENTA_EX
Reset = Fore.RESET


print(Red + """                         Tool By ASM_Royal """ + Green + """
Example1 : 
   1.1.1.1
Example2 :
   1.1.1.1,8.8.8.8,8.8.4.4
   etc. \n \n""" + Back.YELLOW + Fore.BLACK + """WARNING :""" + Back.RESET + Green + """ if input = null or an error corrupts while scan,\nyour own ip will be selected!""")
print(Reset)
ip = input(Blue + "Enter IP to lookup : " + Yellow)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan():
    try:
        print(Purple)
        print("Connecting to " + Yellow + ip)
        print(Reset)
        ping = socket.bind(ip)
    except:
        print(Green)
        print("Connection to " + Yellow + ip + Green + " accepted")
        print(Purple)
        print("Scanning... Please be patient...")
        print(Reset)
        time.sleep(1)
        scan_result = requests.get(f"http://api.db-ip.com/v2/free/{ip}/").text
        scan_result2 = requests.get(f"http://ip-api.com/json/{ip}").text
        scan_result3 = requests.get(f"https://ipqualityscore.com/api/json/ip/FxNKZ5vRitt5z00KQpzvm7POIFFJ27pe/{ip}?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true").text
        print(Purple,"\nScan result " + Yellow + "1:")
        print(Green)
        print(scan_result)
        print(Reset)
        print(Purple, "\nScan result " + Yellow + "2:")
        print(Green)
        print(scan_result2)
        print(Purple, "\nScan result " + Yellow + "3:")
        print(Green)
        print(scan_result3)
        print(Yellow)
        input("\nPress Enter to continue...")
        print(Reset)
    else:
        print(Red)
        print("Could not connect to " + ip)
        print(Reset)

scan()