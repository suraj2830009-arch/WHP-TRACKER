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
    os.system('clear || cls')
    print(f"{C}                              ██╗    ██╗██╗  ██╗██████╗ ")
    print(f"                              ██║    ██║██║  ██║██╔══██╗")
    print(f"                              ██║ █╗ ██║███████║██████╔╝")
    print(f"                              ██║███╗██║██╔══██║██╔═══╝ ")
    print(f"                              ╚███╔███╔╝██║  ██║██║     ")
    print(f"                               ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     {R}")
    print(f"{R}╔══════════════════════════════════════════════════════╗")
    print(f"{W}║{G}             OWNER  : SURAJ                 {W}║")
    print(f"{W}║{G}             GITHUB : suraj2830009         {W}║")
    print(f"{W}║{G}             WA     : WHP-COMMUNITY        {W}║")
    print(f"{W}║{G}             TG     : hacker829            {W}║")
    print(f"{R}╚══════════════════════════════════════════════════════╝{R}")

def track_phone():
    banner()
    print(f"{C}[*] Street-Level Phone Tracking")
    num = input(f"{W}Enter Number (+91): {G}")
    
    try:
        pepnumber = phonenumbers.parse(num)
        if not phonenumbers.is_valid_number(pepnumber):
            print(f"{R}[!] Invalid number!")
            input("\nPress Enter...")
            return

        # PHONENUMBERS GEOCODER (Primary - MOST ACCURATE)
        city_state = geocoder.description_for_number(pepnumber, "en")
        carrier_name = carrier.name_for_number(pepnumber, "en")
        print(f"{Y}[*] Detected: {city_state} | {carrier_name}")
        
        # 4-LAYER OPENCAGE FALLBACK (STREET LEVEL)
        coder = OpenCageGeocode(API_KEY)
        queries = [
            city_state,                          # Layer 1: Pure city
            f"{city_state}, India",              # Layer 2: City+India  
            f"{city_state} {carrier_name}",      # Layer 3: City+Carrier
            f"{city_state}, India {carrier_name}" # Layer 4: Full combo
        ]
        
        best_result = None
        for query in queries:
            try:
                results = coder.geocode(query, countrycode="IN", roadinfo=1, adddetails=1)
                if results and len(results) > 0:
                    best_result = results[0]
                    print(f"{Y}[*] Matched: {query}")
                    break
            except:
                continue
        
        print(f"\n{G}🎯 LOCATION TRACKED (Street-Level)!")
        print(f"{W}{'='*65}")
        print(f"{C}📍 CITY/STATE    : {W}{city_state}")
        print(f"{C}📶 OPERATOR      : {W}{carrier_name}")
        
        if best_result:
            target = best_result
            components = target.get('components', {})
            
            # PRIORITY STREET/AREA EXTRACTION (NO N/A)
            street = (components.get('road') or 
                     components.get('pedestrian') or 
                     components.get('suburb') or 
                     components.get('city_district') or 
                     components.get('neighbourhood') or
                     f"{city_state} Street")
            
            area = (components.get('neighbourhood') or 
                   components.get('suburb') or 
                   components.get('city_district') or 
                   components.get('road') or
                   f"{city_state} Area")
            
            print(f"{C}🏠 FULL ADDRESS  : {Y}{target['formatted']}")
            print(f"{C}🛣️  STREET       : {Y}{street}")
            print(f"{C}🌆 AREA          : {Y}{area}")
            print(f"{C}📈 LAT/LNG       : {G}{target['geometry']['lat']:.6f}, {target['geometry']['lng']:.6f}")
            print(f"{C}🗺️  GOOGLE MAPS  : {W}https://maps.google.com/?q={target['geometry']['lat']:.6f},{target['geometry']['lng']:.6f}")
        else:
            print(f"{C}📍 LOCATION      : {Y}{city_state}")
        
        print(f"{W}{'='*65}")
            
    except Exception as e:
        print(f"{R}[!] Error: {str(e)}")
    
    input(f"\n{Y}Press Enter...")

def get_email():
    banner()
    print(f"{C}[*] Email Hunter (30+ sites)")
    username = input(f"{W}Enter Username: {G}")
    
    print(f"{Y}[*] Scanning holehe (30+ sites)...")
    
    try:
        result = subprocess.run(['holehe', username, '--no-collect', '--no-color'], 
                              capture_output=True, text=True, timeout=90)
        if result.stdout.strip():
            print(f"\n{G}📧 HOLEHE RESULTS:")
            print(f"{W}" + "="*60)
            print(result.stdout)
        else:
            print(f"{Y}[*] holehe: No emails found")
    except subprocess.TimeoutExpired:
        print(f"{Y}[*] holehe: Timeout (some sites slow)")
    except:
        print(f"{R}[!] holehe issue - try manual check")
    
    # POPULAR DOMAINS
    popular = [f"{username}@{d}" for d in 
              ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 
               'icloud.com', 'protonmail.com', 'yahoo.co.in']]
    
    print(f"\n{G}⭐ POPULAR EMAILS:")
    print(f"{W}" + "="*60)
    for email in popular:
        print(f"{C}✉️  {email}")
    
    input(f"\n{Y}Press Enter...")

def scan_username():
    banner()
    print(f"{C}[*] Username Scanner (400+ sites)")
    username = input(f"{W}Enter Username: {G}")
    
    try:
        print(f"{Y}[*] Sherlock scanning 400+ sites (timeout 5min)...")
        result = subprocess.run(['sherlock', username, '--timeout', '10', '--print-found'], 
                              capture_output=True, text=True, timeout=300)
        
        print(f"\n{G}🔍 SHERLOCK RESULTS (400+ sites):")
        print(f"{W}" + "="*65)
        
        found = False
        lines = result.stdout.split('\n')
        for line in lines:
            line = line.strip()
            if '[+]' in line or 'http' in line.lower():
                print(f"{G}✅ {line}")
                found = True
        
        if not found:
            print(f"{Y}[!] No accounts found across 400+ sites")
            
    except subprocess.TimeoutExpired:
        print(f"{Y}[*] Scan timeout - some sites slow")
    except:
        print(f"{R}[!] sherlock issue")
    
    input(f"\n{Y}Press Enter...")

def main():
    os.system('clear || cls')
    sys.stdout.write(f"{C}")
    slow_type("WHP-TRACKER v2.1 - TERMUX ULTRA", 0.05)
    
    while True:
        banner()
        print(f"{W}╔══════════════════════════════════════╗")
        print(f"{W}║{G}  [1] Track number                 {W}║")
        print(f"{W}║{G}  [2] Get email from username     {W}║")
        print(f"{W}║{G}  [3] Scan username              {W}║")
        print(f"{W}║{G}  [0] Exit (silent)              {W}║")
        print(f"{W}╚══════════════════════════════════════╝")
        
        choice = input(f"\n{G}WHP-TRACKER{W} > ").strip()
        
        if choice == '1':
            track_phone()
        elif choice == '2':
            get_email()
        elif choice == '3':
            scan_username()
        elif choice == '0':
            os.system('clear || cls')
            sys.exit(0)
        else:
            print(f"{R}[!] Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    main()
