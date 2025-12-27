import os
import sys
import time
from colorama import Fore, Style, init
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode

init(autoreset=True)

# Colors
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE

# HIGH-ACCURACY API KEY
API_KEY = "07a3935dc099446cb574390384af46af" 

def banner():
    os.system('clear')
    print(f"""{C}
    ██╗    ██╗██╗  ██╗██████╗ 
    ██║    ██║██║  ██║██╔══██╗
    ██║ █╗ ██║███████║██████╔╝
    ██║███╗██║██╔══██║██╔═══╝ 
    ╚███╔███╔╝██║  ██║██║     
     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     
    {W}Owner  : {G}SURAJ
    {W}GitHub : {C}suraj2830009-arch
    {W}WA     : {C}whatsapp.com/channel/0029Vb6cdtSFSAt3SzjK8q0N
    {W}TG     : {C}t.me/hacker829
    {R}Disclaimer: Only for educational use.
    """)

def tracker_mod():
    banner()
    num = input(f"{G}[?] {W}Enter Target Number: {G}")
    
    try:
        pepnumber = phonenumbers.parse(num)
        location_desc = geocoder.description_for_number(pepnumber, "en")
        carrier_name = carrier.name_for_number(pepnumber, "en")
        
        # High-Accuracy Geocoding
        coder = OpenCageGeocode(API_KEY)
        query = str(location_desc)
        results = coder.geocode(query)
        
        print(f"\n{Y}[*] EXTRACTING PRECISE DATA...")
        time.sleep(1)
        
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            full_address = results[0]['formatted']
            
            print(f"\n{G}--- WHP LOCATION REPORT ---")
            print(f"{C}Carrier   :{W} {carrier_name}")
            print(f"{C}Region    :{W} {location_desc}")
            print(f"{C}Address   :{Y} {full_address}")
            print(f"{C}Latitude  :{G} {lat}")
            print(f"{C}Longitude :{G} {lng}")
            print(f"{C}Maps Link :{W} https://www.google.com/maps/place/{lat},{lng}")
            print(f"{G}---------------------------")
        else:
            print(f"{R}[!] Could not pinpoint precise GPS.")
            
    except Exception as e:
        print(f"{R}[!] Error: {e}")
    input(f"\n{Y}Press Enter to continue...")

def email_osint_mod():
    banner()
    username = input(f"{G}[?] {W}Enter Username to Scan: {G}")
    
    # Common domains to check
    targets = [f"{username}@gmail.com", f"{username}@yahoo.com", f"{username}@outlook.com"]
    
    for target in targets:
        print(f"\n{B}[WHP] SCANNING WORLDWIDE: {W}{target}")
        os.system(f"holehe {target}")

    input(f"\n{Y}Global Scan Finished. Press Enter...")

def main():
    while True:
        banner()
        print(f"{W}[{G}01{W}] GPS Location Tracker")
        print(f"{W}[{G}02{W}] Username OSINT Scan")
        print(f"{W}[{G}00{W}] Exit")
        
        # The new sleek prompt
        choice = input(f"\n{C}WHP > {W}")
        
        if choice == '01' or choice == '1':
            tracker_mod()
        elif choice == '02' or choice == '2':
            email_osint_mod()
        elif choice == '00':
            print(f"{R}[!] Powering Down WHP...")
            sys.exit()
        else:
            print(f"{R}[!] Error: Select valid option.")
            time.sleep(1)

if __name__ == "__main__":
    main()
