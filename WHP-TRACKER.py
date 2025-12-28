import os
import sys
import time
import subprocess
from colorama import Fore, Style, init
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

init(autoreset=True)

G, R, Y, C, W, B = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.WHITE, Fore.BLUE
API_KEY = "07a3935dc099446cb574390384af46af" 

def slow_type(text, speed=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    os.system('clear')
    print(f"""
                      {C}██╗    ██╗██╗  ██╗██████╗ 
                      {C}██║    ██║██║  ██║██╔══██╗
                      {C}██║ █╗ ██║███████║██████╔╝
                      {C}██║███╗██║██╔══██║██╔═══╝ 
                      {C}╚███╔███╔╝██║  ██║██║     
                      {C} ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     
    """)
    print(f"{R}-------------------------------------------")
    print(f"{W} OWNER  : {G}SURAJ")
    print(f"{W} GITHUB : {G}suraj2830009")
    print(f"{W} WA     : {G}WHP-COMMUNITY")
    print(f"{W} TG     : {G}hacker829")
    print(f"{R}-------------------------------------------")

def track_phone():
    banner()
    print(f"{C}[*] tracking number")
    num = input(f"{W}Enter Number with Country Code: {G}")
    
    try:
        pepnumber = phonenumbers.parse(num)
        if not phonenumbers.is_valid_number(pepnumber):
            print(f"{R}[!] Invalid!")
            input("\nPress Enter...")
            return

        city_state = geocoder.description_for_number(pepnumber, "en")
        carrier_name = carrier.name_for_number(pepnumber, "en")
        
        coder = OpenCageGeocode(API_KEY)
        results1 = coder.geocode(city_state, countrycode="IN", roadinfo=1, adddetails=1)
        results2 = coder.geocode(f"{city_state} {carrier_name}", countrycode="IN", roadinfo=1, adddetails=1)
        
        best_result = results1[0] if results1 else (results2[0] if results2 else None)
        
        if best_result:
            target = best_result
            components = target.get('components', {})
            print(f"\n{G}[+] LOCATION")
            print(f"{W}{'='*40}")
            print(f"{C}CITY       : {W}{city_state}")
            print(f"{C}OPERATOR   : {W}{carrier_name}")
            print(f"{C}ADDRESS    : {Y}{target['formatted']}")
            print(f"{C}STREET     : {Y}{components.get('road', 'N/A')}")
            print(f"{C}AREA       : {Y}{components.get('neighbourhood', 'N/A')}")
            print(f"{C}LAT/LNG    : {G}{target['geometry']['lat']:.6f}, {target['geometry']['lng']:.6f}")
            print(f"{C}MAPS       : {W}https://maps.google.com/?q={target['geometry']['lat']},{target['geometry']['lng']}")
            print(f"{W}{'='*40}")
        else:
            print(f"\n{G}[+] LOCATION")
            print(f"{W}{'='*40}")
            print(f"{C}CITY     : {W}{city_state}")
            print(f"{C}OPERATOR : {W}{carrier_name}")
            print(f"{W}{'='*40}")
            
    except Exception as e:
        print(f"{R}[!] Error!")
    
    input(f"\n{Y}Press Enter...")

def get_email():
    banner()
    print(f"{C}[*] getting email")
    username = input(f"{W}Enter Username: {G}")
    try:
        result = subprocess.run(['holehe', username, '--no-collect', '--no-color'], capture_output=True, text=True)
        print(result.stdout)
    except:
        print(f"{R}[!] Install holehe!")
    input(f"\n{Y}Press Enter...")

def scan_username():
    banner()
    print(f"{C}[*] scanning username")
    username = input(f"{W}Enter Username: {G}")
    try:
        result = subprocess.run(['sherlock', username], capture_output=True, text=True, timeout=300)
        print(f"\n{G}[+] RESULTS:")
        print(result.stdout)
    except:
        print(f"{R}[!] Install sherlock-project!")
    input(f"\n{Y}Press Enter...")

def main():
    os.system('clear')
    sys.stdout.write(f"{C}")
    slow_type("WHP-TRACKER - INITIALIZING...", 0.05)
    
    while True:
        banner()
        print(f"{W}[{G}1{W}] tracking number")
        print(f"{W}[{G}2{W}] getting email")
        print(f"{W}[{G}3{W}] scanning username")
        print(f"{W}[{G}0{W}] Exit")
        
        choice = input(f"\n{G}WHP-TRACKER{W} > ")
        
        if choice == '1':
            track_phone()
        elif choice == '2':
            get_email()
        elif choice == '3':
            scan_username()
        elif choice == '0':
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    main()
