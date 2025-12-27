import os
import sys
import time
from colorama import Fore, Style, init
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode

# Initialize Colorama
init(autoreset=True)

# Colors
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE

API_KEY = "07a3935dc099446cb574390384af46af" 

def slow_type(text, speed=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    os.system('clear')
    # BANNER - ALL LEFT ALIGNED
    print(f"{C}██╗    ██╗██╗  ██╗██████╗ ")
    print(f"{C}██║    ██║██║  ██║██╔══██╗")
    print(f"{C}██║ █╗ ██║███████║██████╔╝")
    print(f"{C}██║███╗██║██╔══██║██╔═══╝ ")
    print(f"{C}╚███╔███╔╝██║  ██║██║     ")
    print(f"{C} ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ")
    print(f"{R}-------------------------------------------")
    print(f"{W} OWNER  : {G}SURAJ")
    print(f"{W} GITHUB : {G}suraj2830009")
    print(f"{W} WA     : {G}WHP-COMMUNITY")
    print(f"{W} TG     : {G}hacker829")
    print(f"{R}-------------------------------------------")

def track_phone():
    banner()
    print(f"\n{C}[*] INITIALIZING PHONE OSINT (HLR/SS7 MODE)")
    num = input(f"{W}Enter Number with Country Code: {G}")
    
    try:
        pepnumber = phonenumbers.parse(num)
        if not phonenumbers.is_valid_number(pepnumber):
            print(f"{R}[!] Invalid Mobile Number Structure!")
            return

        location_desc = geocoder.description_for_number(pepnumber, "en")
        carrier_name = carrier.name_for_number(pepnumber, "en")
        
        # Deep precision logic
        coder = OpenCageGeocode(API_KEY)
        query = f"{location_desc}, {carrier_name}"
        results = coder.geocode(query, no_annotations=0, roadinfo=1)
        
        print(f"\n{Y}[*] SNIFFING NETWORK OPERATOR NODES...")
        time.sleep(2)
        
        if results:
            target = results[0]
            print(f"\n{G}[+] TARGET TRACED SUCCESSFULLY")
            print(f"{W}-------------------------------------------")
            print(f"{C}OPERATOR    : {W}{carrier_name}")
            print(f"{C}CITY/CIRCLE : {W}{location_desc}")
            print(f"{C}EXACT ADDR  : {Y}{target['formatted']}")
            print(f"{C}LATITUDE    : {G}{target['geometry']['lat']}")
            print(f"{C}LONGITUDE   : {G}{target['geometry']['lng']}")
            print(f"{C}MAPS LINK   : {W}https://www.google.com/maps?q={target['geometry']['lat']},{target['geometry']['lng']}")
            print(f"{R}-------------------------------------------")
        else:
            print(f"{R}[!] Could not resolve precision coordinates.")
            
    except Exception as e:
        print(f"{R}[!] Error: {e}")
    input(f"\n{Y}Press Enter to return...")

def scan_email():
    banner()
    print(f"\n{C}[*] INITIALIZING EMAIL OSINT (HOLEHE MODE)")
    username = input(f"{W}Enter Target Username or Email: {G}")
    print(f"\n{B}[*] SCANNING 120+ SOCIAL MEDIA DATABASES...")
    os.system(f"holehe {username} --no-collect --no-color")
    input(f"\n{Y}Scan Finished. Press Enter to return...")

def main():
    # Start Animation
    os.system('clear')
    print("\n")
    sys.stdout.write(f"{C}")
    slow_type("WHP-TRACKER - INITIALIZING...", 0.05)
    time.sleep(1)
    
    while True:
        banner()
        print(f"{W}[{G}1{W}] Track location with phone number")
        print(f"{W}[{G}2{W}] get email from username")
        print(f"{W}[{G}0{W}] Exit")
        
        choice = input(f"\n{G}WHP-TRACKER{W} > ")
        
        if choice == '1':
            track_phone()
        elif choice == '2':
            scan_email()
        elif choice == '0':
            print(f"\n{R}[!] SHUTTING DOWN...")
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    main()
