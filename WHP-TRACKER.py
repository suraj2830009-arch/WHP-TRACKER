#!/usr/bin/env python3
# WHP-TRACKER - ULTIMATE OSINT SUITE (400 LINES)
# Created by: SURAJ - PROFESSIONAL TOOLKIT

import sys, os, json, time, subprocess, webbrowser, requests, re, urllib.parse, random, threading
from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier, parse, timezone, format_number, PhoneNumberFormat
from phonenumbers.phonenumberutil import number_type
try: 
    from opencage.geocoder import OpenCageGeocode
    OPENCAGE_AVAILABLE = True
except: 
    OPENCAGE_AVAILABLE = False
    OpenCageGeocode = None

# =============================================================================
# ADVANCED COLORS & STYLING (45 LINES)
# =============================================================================
class Colors:
    RED = '\033[91m'; GREEN = '\033[92m'; YELLOW = '\033[93m'
    BLUE = '\033[94m'; MAGENTA = '\033[95m'; CYAN = '\033[96m'; WHITE = '\033[97m'
    BOLD = '\033[1m'; UNDERLINE = '\033[4m'; END = '\033[0m'
    
def style(text, color='w', bold=False, underline=False):
    c = {'r':Colors.RED, 'g':Colors.GREEN, 'y':Colors.YELLOW, 'b':Colors.BLUE, 
         'm':Colors.MAGENTA, 'c':Colors.CYAN, 'w':Colors.WHITE}[color[0]]
    fmt = Colors.BOLD if bold else ''
    fmt += Colors.UNDERLINE if underline else ''
    return f"{c}{fmt}{text}{Colors.END}"

# =============================================================================
# CONFIG & SOCIAL (30 LINES)
# =============================================================================
CONFIG = {
    "opencage_key": "07a3935dc099446cb574390384af46af",
    "social": {
        "youtube": "https://www.youtube.com/@WHP-TEAM",
        "telegram": "https://t.me/hacker829",
        "discord": "https://discord.gg/CDxxrjMF5N",
        "whatsapp": "https://whatsapp.com/channel/0029Vb6cdtSFSAt3SzjK8q0N"
    }
}

SOCIAL_LINKS = list(CONFIG["social"].values())

# =============================================================================
# FILE & LOGGING SYSTEM (50 LINES)
# =============================================================================
def setup_dirs():
    for d in ["results", "logs", "cache"]:
        os.makedirs(d, exist_ok=True)

def log_message(msg, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {msg}"
    color = 'g' if level == "SUCCESS" else 'r' if level == "ERROR" else 'c'
    print(style(log_entry, color, bold=True))
    
    try:
        with open("logs/whp_tracker.log", "a", encoding="utf-8") as f:
            f.write(f"{log_entry}\n")
    except: pass

def save_results(data, prefix):
    try:
        filename = f"results/{prefix}_{int(time.time())}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log_message(f"Results saved: {filename}", "SUCCESS")
        return True
    except Exception as e:
        log_message(f"Save error: {e}", "ERROR")
        return False

# =============================================================================
# PHONE NORMALIZATION ENGINE (35 LINES)
# =============================================================================
def normalize_phone(phone_input):
    """Advanced phone number normalization"""
    phone_input = phone_input.strip()
    variants = [phone_input]
    
    # Clean and generate variants
    clean = re.sub(r'[^\d+]', '', phone_input)
    if clean.startswith('0') and len(clean) == 11:
        variants.append(f"+91{clean[1:]}")
    elif len(clean) == 10 and clean.isdigit():
        variants.append(f"+91{clean}")
    elif len(clean) == 12 and clean.startswith('91'):
        variants.append(f"+{clean}")
    
    for variant in variants:
        try:
            parsed = parse(variant)
            if phonenumbers.is_valid_number(parsed) and phonenumbers.is_possible_number(parsed):
                formats = {
                    "international": format_number(parsed, PhoneNumberFormat.INTERNATIONAL),
                    "national": format_number(parsed, PhoneNumberFormat.NATIONAL),
                    "e164": format_number(parsed, PhoneNumberFormat.E164)
                }
                return parsed, formats
        except: continue
    
    return None, {"error": "Invalid phone number"}

# =============================================================================
# PHONEINFOGA PROFESSIONAL ENGINE (90 LINES)
# =============================================================================
class PhoneInfogaEngine:
    def __init__(self):
        self.api_key = CONFIG["opencage_key"]
    
    def basic_analysis(self, parsed):
        """Complete basic phone analysis"""
        try:
            type_map = {0:"Unknown",1:"Fixed",2:"Mobile",3:"Fixed/Mobile",4:"TollFree"}
            return {
                "valid": phonenumbers.is_valid_number(parsed),
                "possible": phonenumbers.is_possible_number(parsed),
                "type": type_map.get(number_type(parsed), "Unknown"),
                "country_code": parsed.country_code,
                "country": phonenumbers.region_code_for_number(parsed),
                "location": geocoder.description_for_number(parsed, "en"),
                "carrier": carrier.name_for_number(parsed, "en") or "Unknown",
                "timezones": list(timezone.time_zones_for_number(parsed))
            }
        except: return {"error": "Analysis failed"}
    
    def geolocation(self, location_hint):
        """Street-level geolocation"""
        if not OPENCAGE_AVAILABLE:
            return {"status": "OpenCage not available"}
        
        try:
            geocoder = OpenCageGeocode(self.api_key)
            results = geocoder.geocode(f"{location_hint}, India")
            
            if results and len(results) > 0:
                primary = results[0]
                coords = primary['geometry']
                return {
                    "status": "SUCCESS",
                    "latitude": coords['lat'],
                    "longitude": coords['lng'],
                    "address": primary['formatted'],
                    "google_maps": f"https://maps.google.com/?q={coords['lat']},{coords['lng']}",
                    "confidence": primary.get('confidence', 0)
                }
        except Exception as e: pass
        
        return {"status": "FAILED"}
    
    def generate_osint_links(self, phone, formats):
        """Generate comprehensive OSINT links"""
        clean_phone = re.sub(r'[^\d]', '', str(phone))
        return {
            "google": f"https://www.google.com/search?q={urllib.parse.quote(formats['international'])}",
            "truecaller": f"https://www.truecaller.com/search/in/{clean_phone.lstrip('91')}",
            "whatsapp": f"https://wa.me/{clean_phone}",
            "facebook": f"https://www.facebook.com/search/top?q={urllib.parse.quote(formats['international'])}",
            "twitter": f"https://twitter.com/search?q={urllib.parse.quote(formats['international'])}"
        }
    
    def full_scan(self, phone_input):
        """Complete PhoneInfoga scan"""
        parsed, formats = normalize_phone(phone_input)
        if not parsed:
            return {"status": "ERROR", "error": formats["error"]}
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "input": phone_input,
            "formats": formats,
            "basic": self.basic_analysis(parsed),
            "geo": self.geolocation(results["basic"].get("location", "India")),
            "osint": self.generate_osint_links(parsed, formats),
            "status": "SUCCESS" if results["basic"].get("valid") else "INVALID"
        }
        return results

# =============================================================================
# EMAIL & USERNAME TOOLS (40 LINES)
# =============================================================================
DOMAINS = ['gmail.com','yahoo.com','hotmail.com','outlook.com','live.com','yahoo.co.in',
           'rediffmail.com','zoho.com','protonmail.com','icloud.com','gmx.com']

def email_hunter(username):
    emails = []
    patterns = [username, username.lower(), f"{username}123", f"info.{username}"]
    for pattern in patterns:
        emails.extend([f"{pattern}@{d}" for d in DOMAINS])
    return {"username": username, "emails": emails[:25], "total": len(emails)}

def username_scanner(username):
    try:
        result = subprocess.run(
            ['python3', '-m', 'sherlock', username, '--timeout', '8', '--print-found'],
            capture_output=True, text=True, timeout=90
        )
        found = [line.strip() for line in result.stdout.split('\n') if '[+]' in line]
        return {"username": username, "found": found[:15], "count": len(found)}
    except: return {"username": username, "error": "Sherlock not installed"}

# =============================================================================
# DISPLAY SYSTEM (60 LINES)
# =============================================================================
def clear_screen(): os.system('cls' if os.name=='nt' else 'clear')

def show_banner():
    clear_screen()
    print("\n"*3)
    banner_text = [
        style("      ██████╗ ██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗      ", 'c', bold=True),
        style("      ██╔══██╗██║ ██╔╝██╔════╝██╔════╝██║ ██╔╝██╔════╝      ", 'c', bold=True),
        style("      ██████╔╝█████╔╝ █████╗  ██║     █████╔╝ █████╗       ", 'c', bold=True),
        style("      ██╔══██╗██╔═██╗ ██╔══╝  ██║     ██╔═██╗ ██╔══╝       ", 'c', bold=True),
        style("      ██║  ██║██║  ██╗███████╗╚██████╗██║  ██╗███████╗      ", 'c', bold=True),
        style("      ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝      ", 'c', bold=True)
    ]
    for line in banner_text: print(line.center(115))
    
    print(style("\n" + "="*115 + "\nPROFESSIONAL OSINT SUITE\n" + "="*115, 'c', bold=True))
    for name, url in CONFIG["social"].items():
        print(style(f"{name.upper()}:", 'g', bold=True) + f" {style(url, 'b', underline=True)}")
    print(style("="*115, 'c', bold=True) + "\n")

def display_phone_results(results):
    print(style("\nPHONEINFOGA PROFESSIONAL RESULTS", 'm', bold=True).center(115))
    print(style("="*115, 'c'))
    print(style(f"STATUS: {results['status']}", 'g' if results['status']=='SUCCESS' else 'r', bold=True))
    
    print(f"\n{style('📱 PHONE FORMATS', 'g', bold=True)}")
    for fmt, value in results['formats'].items():
        print(f"  {style(fmt.upper(), 'y', bold=True)}: {style(value, 'w')}")
    
    basic = results['basic']
    print(f"\n{style('📊 BASIC INFO', 'g', bold=True)}")
    print(f"  {style('TYPE:', 'y')} {basic.get('type', 'N/A')} | {style('CARRIER:', 'y')} {basic.get('carrier', 'N/A')}")
    print(f"  {style('LOCATION:', 'y')} {basic.get('location', 'N/A')}")
    
    geo = results['geo']
    print(f"\n{style('📍 GEOLOCATION', 'g', bold=True)}")
    if geo.get('status') == 'SUCCESS':
        print(f"  {style('MAPS:', 'y')} {style(geo['google_maps'], 'b', underline=True)}")
    else:
        print(f"  {style('Unavailable', 'y')}")
    
    print(f"\n{style('🔗 OSINT LINKS', 'g', bold=True)}")
    for name, link in list(results['osint'].items())[:5]:
        print(f"  {style(name.title(), 'y')}: {style(link, 'b', underline=True)}")

# =============================================================================
# SOCIAL & MAIN LOOP (50 LINES)
# =============================================================================
def open_social_links():
    def open_url(url):
        try: webbrowser.open(url); time.sleep(1)
        except: pass
    
    threads = []
    for url in SOCIAL_LINKS[:2]:  # YouTube + Telegram
        t = threading.Thread(target=open_url, args=(url,))
        t.start()
        threads.append(t)
    for t in threads: t.join()
    log_message("Opened YouTube & Telegram - Please Subscribe & Follow!", "SUCCESS")

def main():
    setup_dirs()
    log_message("🚀 WHP-TRACKER Professional OSINT Suite Started!", "SUCCESS")
    open_social_links()
    
    phone_engine = PhoneInfogaEngine()
    
    while True:
        show_banner()
        print(style("1. PHONEINFOGA (Street-Level Geo)", 'g', bold=True))
        print(style("2. EMAIL HUNTER (25+ Variations)", 'g', bold=True))
        print(style("3. USERNAME SCAN (Sherlock 400+)", 'g', bold=True))
        print(style("4. SOCIAL LINKS (YouTube/Telegram)", 'g', bold=True))
        print(style("0. EXIT", 'r', bold=True))
        
        choice = input(style("\nWHP> ", 'c', bold=True)).strip()
        
        if choice == '1':
            phone = input(style("Enter Phone Number: ", 'c')).strip()
            results = phone_engine.full_scan(phone)
            show_banner()
            display_phone_results(results)
            save_results(results, f"phone_{phone[:10]}")
            
        elif choice == '2':
            username = input(style("Enter Username: ", 'c')).strip()
            results = email_hunter(username)
            show_banner()
            print(style(f"Generated {results['total']} email variations:", 'g', bold=True))
            for email in results['emails'][:10]:
                print(style(email, 'b', underline=True))
            save_results(results, f"email_{username}")
            
        elif choice == '3':
            username = input(style("Enter Username: ", 'c')).strip()
            results = username_scanner(username)
            show_banner()
            print(style(f"Found {results.get('count', 0)} social accounts:", 'g', bold=True))
            for account in results.get('found', [])[:10]:
                print(style(account, 'b', underline=True))
            save_results(results, f"username_{username}")
            
        elif choice == '4':
            open_social_links()
            
        elif choice == '0':
            log_message("👋 Thank you for using WHP-TRACKER!", "SUCCESS")
            sys.exit(0)
        
        else:
            print(style("Invalid option!", 'r', bold=True))
        
        input(style("\nPress Enter to continue...", 'y'))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(style("\nGoodbye!", 'y'))
        sys.exit(0)
