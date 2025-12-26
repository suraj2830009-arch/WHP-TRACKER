import os
import sys
import time
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim
from colorama import Fore, Style, init

init(autoreset=True)

# --- Colors ---
R, G, Y, B, C, W = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.WHITE

def banner():
    os.system('clear')
    print(C + r"""
 __      __.__ __________ ___________ __________   _____  _________  ____  __.___________ 
/  \    /  |  |   \______ \\______   \\______   \ /  _  \ \_   ___ \|    |/ _|\_   _____/ 
\   \/\/   |  |   ||     ___/|     ___/ |       _//  /_\  \/    \  \/|      <   |    __)_  
 \        /|  |   ||    |    |    |     |    |   /    |    \     \___|    |  \  |        \ 
  \__/\  / |______|____|    |____|     |____|_  /\____|__  /\______  |____|__ \/_______  / 
       \/                                     \/         \/        \/        \/        \/  
    """ + Style.BRIGHT)
    print(f"{R}      [!] WHP-TRACKER | Specialized OSINT Suite [!]{W}")
    print(f"{Y}      MADE BY SURAJ | Educational Purposes Only")
    print(f"{B}      -------------------------------------------")

def get_location():
    print(f"\n{C}[ TRACK PHONE LOCATION ]{W}")
    number = input(f"{G}[+] Enter Phone Number (+CountryCode): {W}")
    try:
        parsed_number = phonenumbers.parse(number)
        region = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        zone = timezone.time_zones_for_number(parsed_number)
        
        print(f"\n{Y}[*] Location: {W}{region}")
        print(f"{Y}[*] Carrier:  {W}{operator}")
        print(f"{Y}[*] Timezone: {W}{zone}")

        # Map generation
        geolocator = Nominatim(user_agent="WHP-TRACKER")
        location = geolocator.geocode(region)
        if location:
            print(f"{G}[+] Map Link: {W}https://www.google.com/maps/place/{location.latitude}+{location.longitude}")
    except:
        print(f"{R}[!] Invalid format. Use +1234567890")

def get_email_osint():
    print(f"\n{C}[ SEARCHING 150+ SITES FOR EMAIL ]{W}")
    target = input(f"{G}[+] Enter Target Email: {W}")
    print(f"\n{Y}[*] Hunting profiles on 150+ platforms... Please wait.{W}")
    
    # Executing Holehe engine for 150+ sites one-click lookup
    os.system(f"holehe {target}")
    
    print(f"\n{G}[+] Search Finished for: {target}")

def main():
    while True:
        banner()
        print(f"{G}  [01]{W} Get Location with Phone Number")
        print(f"{G}  [02]{W} Get Email Details (Search 150+ Sites)")
        print(f"{R}  [00]{W} Exit Tool")
        
        choice = input(f"\n{B} Suraj@WHP >> {W}")

        if choice in ['01', '1']:
            get_location()
            input(f"\n{Y}Press Enter to go back...")
        elif choice in ['02', '2']:
            get_email_osint()
            input(f"\n{Y}Press Enter to go back...")
        elif choice in ['00', '0']:
            print(f"{G}Goodbye Suraj!{W}")
            sys.exit()
        else:
            print(f"{R}Invalid Choice!{W}")
            time.sleep(1)

if __name__ == "__main__":
    main()
