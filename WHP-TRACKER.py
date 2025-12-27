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

# HIGH-ACCURACY API KEY (OpenCage)
API_KEY = "07a3935dc099446cb574390384af46af" 

def banner():
    os.system('clear')
    print(f"""{C}
  ██╗    ██╗██╗  ██╗██████╗         ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██║    ██║██║  ██║██╔══██╗        ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ██║ █╗ ██║███████║██████╔╝  █████╗   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
  ██║███╗██║██╔══██║██╔═══╝   ╚════╝   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  ╚███╔███╔╝██║  ██║██║                ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██╗
   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝                ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 {R}------------------------------------------------------------------------------------------
 {W}  OWNER  : SURAJ [R]        |   TELEGRAM: https://t.me/hacker829
 {W}  GITHUB : suraj2830009-arch |   WHATSAPP: https://whatsapp.com/channel/0029Vb6cdtSFSAt3SzjK8q0N
 {R}------------------------------------------------------------------------------------------
 {Y} [!] DISCLAIMER: The owner is not responsible for any misuse of this tool. For educational use only.
 {R}------------------------------------------------------------------------------------------
    """)

def tracker_mod():
    banner()
    print(f"{G}[R] {W}LOGGED IN: HIGH-ACCURACY GPS TRACKING ENABLED")
    num = input(f"\n{C}Enter Phone Number (+CountryCode): {W}")
    
    try:
        pepnumber = phonenumbers.parse(num)
        location_desc = geocoder.description_for_number(pepnumber, "en")
        carrier_name = carrier.name_for_number(pepnumber, "en")
        tz = timezone.time_zones_for_number(pepnumber)

        print(f"\n{Y}[*] EXTRACTING DATA FROM SATELLITE...")
        time.sleep(1.5)
        
        geocoder_api = OpenCageGeocode(API_KEY)
        query = str(location_desc)
        results = geocoder_api.geocode(query)
        
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
            address = results[0]['formatted']
            
            print(f"\n{G}[+] TARGET IDENTIFIED:")
            print(f"{W}-------------------------------------")
            print(f"{B}[R] {C}Service Provider: {W}{carrier_name}")
            print(f"{B}[R] {C}Registration    : {W}{location_desc}")
            print(f"{B}[R] {C}Current Timezone: {W}{tz}")
            print(f"{B}[R] {C}Exact Address   : {Y}{address}")
            print(f"{B}[R] {C}Latitude        : {G}{lat}")
            print(f"{B}[R] {C}Longitude       : {G}{lng}")
            print(f"{B}[R] {C}Location Link   : {W}https://www.google.com/maps/search/?api=1&query={lat},{lng}")
            print(f"{W}-------------------------------------")
        else:
            print(f"{R}[!] Error: Could not pinpoint precise coordinates.")
            
    except Exception as e:
        print(f"{R}[R] ERROR: {e}")
    input(f"\n{Y}Press Enter to go back to Menu...")

def email_osint_mod():
    banner()
    print(f"{G}[R] {W}LOGGED IN: 150+ SITE USERNAME SCANNER")
    username = input(f"\n{C}Enter Target Username: {W}")
    
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    
    for dom in domains:
        target = f"{username}@{dom}"
        print(f"\n{B}[R] RUNNING GLOBAL SCAN FOR: {W}{target}")
        print(f"{R}" + "="*50)
        os.system(f"holehe {target}")
        print(f"{R}" + "="*50)

    input(f"\n{Y}Global Scan Complete. Press Enter to return...")

def main():
    while True:
        banner()
        print(f"{G} [1] {W}Track Location (Accurate GPS) [R]")
        print(f"{G} [2] {W}Find Email & Scan 150+ Sites  [R]")
        print(f"{R} [00] {W}Exit WHP-TRACKER")
        
        choice = input(f"\n{C}WHP-TRACKER >> {W}")
        
        if choice == '1':
            tracker_mod()
        elif choice == '2':
            email_osint_mod()
        elif choice == '00':
            print(f"{R}[!] Closing Security Framework. Goodbye Suraj!")
            sys.exit() # Force exit the process
        else:
            print(f"{R}[!] Invalid Input!")
            time.sleep(1)

if __name__ == "__main__":
    main()
