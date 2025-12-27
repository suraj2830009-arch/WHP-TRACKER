import os
import sys
import time
import subprocess
from colorama import Fore, Style, init
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim

init(autoreset=True)

# Colors
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE

def banner():
    os.system('clear')
    print(f"""
{R} __      __.__ __________        ___________ __________  _________  ____  __.___________ 
{R}/  \    /  \  |__\______ \       \__    ___/|    |   \ \_   ___ \|    |/ _|\_   _____/ 
{W}\   \/\/   /  |  ||    |  \        |    |   |    |   / /    \  \/|      <   |    __)_  
{W} \        /|  |  ||    `   \       |    |   |    |  /  \     \___|    |  \  |        \ 
{G}  \__/\  / |__|__|/_______  /______ |____|   |______/    \______  /____|__ \/_______  / 
{G}       \/                 \/_____/                              \/        \/        \/  
        {C}CREATED BY SURAJ | TRACKER & OSINT | VERSION 2.0
    """)

def tracker():
    banner()
    print(f"{Y}[*] PHONE LOCATION TRACKER")
    num = input(f"\n{G}Enter Number (+CountryCode): {W}")
    try:
        pepnumber = phonenumbers.parse(num)
        location = geocoder.description_for_number(pepnumber, "en")
        service = carrier.name_for_number(pepnumber, "en")
        time_zone = timezone.time_zones_for_number(pepnumber)
        
        geolocator = Nominatim(user_agent="WHP")
        coord = geolocator.geocode(location)
        
        print(f"\n{C}Carrier: {W}{service}")
        print(f"{C}Region:  {W}{location}")
        print(f"{C}Timezone:{W}{time_zone}")
        
        if coord:
            print(f"{C}Lat/Lon: {W}{coord.latitude}, {coord.longitude}")
            print(f"{G}Maps: {W}https://www.google.com/maps/search/?api=1&query={coord.latitude},{coord.longitude}")
        else:
            print(f"{R}[!] Detailed coordinates not found for this region.")
    except Exception as e:
        print(f"{R}Error: {e}")
    input(f"\n{Y}Press Enter to return...")

def email_osint():
    banner()
    print(f"{Y}[*] USERNAME TO EMAIL OSINT (150+ SITES)")
    username = input(f"\n{G}Enter Target Username: {W}")
    
    # Common domains to check against the username
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    print(f"\n{C}[+] Generating common email patterns for: {W}{username}")
    
    for domain in domains:
        target_email = f"{username}@{domain}"
        print(f"\n{Y}--- Scanning for: {target_email} ---{W}")
        try:
            # Executes holehe for each generated email target
            subprocess.run(["holehe", target_email])
        except Exception as e:
            print(f"{R}Error scanning {domain}: {e}")
            
    input(f"\n{Y}Search Complete. Press Enter to return...")

def main():
    while True:
        banner()
        print(f"{G}1. {W}Track Location with Phone Number")
        print(f"{G}2. {W}Find Email from Username & Scan 150+ Sites")
        print(f"{G}0. {W}Exit")
        
        choice = input(f"\n{C}SELECT OPTION: {W}")
        
        if choice == '1':
            tracker()
        elif choice == '2':
            email_osint()
        elif choice == '0':
            print(f"{R}Goodbye!")
            break
        else:
            print(f"{R}Invalid key!")
            time.sleep(1)

if __name__ == "__main__":
    main()
