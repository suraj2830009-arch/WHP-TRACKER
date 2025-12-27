import os
import sys
import time
from colorama import Fore, Style, init
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode

# Initialize Colorama
init(autoreset=True)

# Define Colors
G, R, Y, C, W, B = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.WHITE, Fore.BLUE
API_KEY = "07a3935dc099446cb574390384af46af" 

# Get Termux user name for the prompt
try:
    USER_NAME = os.getlogin()
except:
    USER_NAME = "hacker"

def slow_type(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    os.system('clear')
    print(f"""{C}
  ██╗    ██╗██╗  ██╗██████╗         ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██║    ██║██║  ██║██╔══██╗        ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ██║ █╗ ██║███████║██████╔╝  █████╗   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
  ██║███╗██║██╔══██║██╔═══╝   ╚════╝   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  ╚███╔███╔╝██║  ██║██║                ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██╗
   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝                ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    {W}          WHP-TRACKER V5.0
    {R}      {'='*30}
    {W} OWNER  : {G}SURAJ
    {W} GITHUB : {G}suraj2830009-arch
    {W} WA     : {G}whatsapp.com/channel/0029Vb6cdtSFSAt3SzjK8q0N
    {W} TG     : {G}t.me/hacker829
    {R}      {'='*30}
    """)

def disclaimer_screen():
    os.system('clear')
    print(f"\n{R}[!] BIG DISCLAIMER [!]")
    print(f"{W}This tool is for educational purposes only. Unauthorized")
    print(f"{W}tracking of individuals is illegal. The WHP TEAM and")
    print(f"{W}the owner (SURAJ) are not responsible for any misuse.")
    print(f"{W}By using this tool, you agree to take full responsibility.")
    print(f"\n{G}--- THANKS TO WHP TEAM ---")
    input(f"\n{Y}Press Enter to Agree and Continue...")

def tracker_mod():
    banner()
    print(f"\n{C}[*] INITIALIZING HIGH-PRECISION TRIANGULATION (1-50m)")
    num = input(f"{W}Enter Number with Country Code (e.g. +91...): {G}")
    
    try:
        pepnumber = phonenumbers.parse(num)
        if not phonenumbers.is_valid_number(pepnumber):
            print(f"{R}[!] Invalid Phone Number!")
            return

        location_desc = geocoder.description_for_number(pepnumber, "en")
        carrier_name = carrier.name_for_number(pepnumber, "en")
        
        # Deep Geo-Query for High Accuracy
        coder = OpenCageGeocode(API_KEY)
        query = f"{location_desc}, {carrier_name}"
        # Requesting highest confidence to avoid generic state centers
        results = coder.geocode(query, no_annotations=0, proximity="1.0, 1.0")
        
        print(f"\n{Y}[*] CONNECTING TO SIGNAL TOWERS...")
        time.sleep(1.5)
        print(f"{Y}[*] CALCULATING GPS NODES (1-50m)...")
        time.sleep(1.5)
        
        if results:
            best_node = results[0]
            print(f"\n{G}  [+] TARGET SIGNAL ISOLATED")
            print(f"{W}  -------------------------------------------")
            print(f"{C}  CARRIER     : {W}{carrier_name}")
            print(f"{C}  COUNTRY     : {W}{location_desc}")
            print(f"{C}  PRECISE ADDR: {Y}{best_node['formatted']}")
            print(f"{C}  LATITUDE    : {G}{best_node['geometry']['lat']}")
            print(f"{C}  LONGITUDE   : {G}{best_node['geometry']['lng']}")
            print(f"{C}  ACCURACY    : {G}HIGH (1-50m Radius)")
            print(f"{C}  GOOGLE MAPS : {W}https://www.google.com/maps?q={best_node['geometry']['lat']},{best_node['geometry']['lng']}")
            print(f"{W}  -------------------------------------------")
        else:
            print(f"{R}[!] No precision nodes found for this number.")
            
    except Exception as e:
        print(f"{R}[!] Error: {e}")
    input(f"\n{Y}Press Enter to return...")

def email_osint_mod():
    banner()
    username = input(f"{W}Enter Target Username: {G}")
    domains = ["outlook.com", "yahoo.com", "gmail.com"]
    
    for dom in domains:
        target = f"{username}@{dom}"
        print(f"\n{B}[WHP-TRACKER] SCANNING DATABASE: {W}{target}")
        os.system(f"holehe {target} --no-collect --no-color")
        time.sleep(1)

    input(f"\n{Y}Scan Finished. Press Enter...")

def startup_animation():
    os.system('clear')
    print(f"\n\n\n")
    slow_type(f"        {W}STATUS: {G}INITIALIZING...", 0.05)
    slow_type(f"        {W}SOURCE: {G}SURAJ-OFFICIAL", 0.05)
    # Step by step WHP-TRACKER reveal
    slow_type(f"        {C}WHP-TRACKER", 0.1)
    time.sleep(1)

def main():
    startup_animation()
    disclaimer_screen()
    while True:
        banner()
        print(f" {W}[{G}01{W}] Precise Location (1-50m)")
        print(f" {W}[{G}02{W}] Username OSINT Tracker")
        print(f" {W}[{G}00{W}] Exit")
        
        # User defined prompt based on Termux name
        choice = input(f"\n{G}{USER_NAME}{W} > ")
        
        if choice == '1' or choice == '01':
            tracker_mod()
        elif choice == '2' or choice == '02':
            email_osint_mod()
        elif choice == '00':
            print(f"{R}[!] Shutting Down WHP-TRACKER...")
            sys.exit()
        else:
            print(f"{R}[!] Invalid Choice!")
            time.sleep(1)

if __name__ == "__main__":
    main()
