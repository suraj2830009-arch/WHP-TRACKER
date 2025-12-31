#!/usr/bin/env python3
# WHP-TRACKER v6.5 - PERFECT MERGED DATABASE (425 LINES)
# Created by: SURAJ - ULTIMATE OSINT SUITE

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
# COLORS & STYLING
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
# 🔥 SINGLE MERGED DATABASE - ALL FORMATS (ONE ENTRY PER NUMBER!)
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

# 🔥 SINGLE MERGED DATABASE - CLEAN & PERFECT
MERGED_DATABASE = {
    # RAHUL KUMAR - PATNA, BIHAR (8789904492)
    "8789904492": {
        "name": "RAHUL KUMAR", 
        "location": "PATNA, BIHAR", 
        "carrier": "AIRTEL", 
        "status": "ACTIVE",
        "aliases": ["+918789904492", "918789904492"]  # All formats map here
    },
    
    # ANURAG SINGH - DELHI (7050407370)
    "7050407370": {
        "name": "ANURAG SINGH", 
        "location": "DELHI", 
        "carrier": "JIO", 
        "status": "ACTIVE",
        "aliases": ["+917050407370", "917050407370"]
    },
    
    # TEST USER - PUNE (7033045921)
    "7033045921": {
        "name": "TEST USER", 
        "location": "PUNE, MAHARASHTRA", 
        "carrier": "VI", 
        "status": "ACTIVE",
        "aliases": ["+917033045921", "917033045921"]
    }
}

SOCIAL_LINKS = list(CONFIG["social"].values())

# =============================================================================
# FILE SYSTEM
# =============================================================================
def setup_dirs():
    for d in ["results", "logs", "cache"]: os.makedirs(d, exist_ok=True)

def log_message(msg, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {msg}"
    color = 'g' if level == "SUCCESS" else 'r' if level == "ERROR" else 'c'
    print(style(log_entry, color, bold=True))
    
    try:
        os.makedirs("logs", exist_ok=True)
        with open("logs/whp_tracker.log", "a", encoding="utf-8") as f:
            f.write(f"{log_entry}\n")
    except: pass

def save_results(data, prefix):
    try:
        os.makedirs("results", exist_ok=True)
        filename = f"results/{prefix}_{int(time.time())}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log_message(f"Results saved: {filename}", "SUCCESS")
        return True
    except Exception as e:
        log_message(f"Save error: {e}", "ERROR")
        return False

# =============================================================================
# 🔥 PERFECT NORMALIZATION → MERGED DATABASE
# =============================================================================
def normalize_phone(phone_input):
    phone_input = phone_input.strip()
    clean_digits = re.sub(r'[^\d+]', '', phone_input)
    
    # Generate ALL variants
    variants = [phone_input]
    
    # Clean 10-digit (PRIMARY KEY)
    if len(clean_digits) == 10:
        variants.append(clean_digits)
        variants.append(f"+91{clean_digits}")
        variants.append(f"91{clean_digits}")
    elif len(clean_digits) == 12 and clean_digits.startswith('91'):
        clean_10 = clean_digits[2:]
        variants.extend([clean_10, f"+91{clean_10}", f"91{clean_10}"])
    
    # Parse best format
    for variant in variants:
        try:
            parsed = parse(variant)
            if phonenumbers.is_valid_number(parsed) and phonenumbers.is_possible_number(parsed):
                clean_10 = str(parsed.national_number)[-10:]
                return parsed, {
                    "international": format_number(parsed, PhoneNumberFormat.INTERNATIONAL),
                    "national": format_number(parsed, PhoneNumberFormat.NATIONAL),
                    "e164": format_number(parsed, PhoneNumberFormat.E164),
                    "clean_10": clean_10,  # SINGLE KEY FOR DATABASE
                    "all_formats": variants
                }
        except: continue
    
    return None, {"error": "Invalid phone number"}

# =============================================================================
# 🔥 MERGED DATABASE ENGINE - ONE LOOKUP!
# =============================================================================
class MergedDatabaseEngine:
    def check_merged_database(self, clean_10):
        """🔥 SINGLE CLEAN_10 LOOKUP - PERFECT!"""
        if clean_10 in MERGED_DATABASE:
            data = MERGED_DATABASE[clean_10]
            log_message(f"🎯 MERGED DB HIT: {clean_10} → {data['name']} | {data['location']}", "SUCCESS")
            return {
                "hit": True,
                "key": clean_10,
                "data": data
            }
        return {"hit": False}
    
    def get_display_data(self, db_data):
        return {
            "name": db_data.get("name", "N/A"),
            "location": db_data.get("location", "N/A"),
            "carrier": db_data.get("carrier", "N/A"),
            "status": db_data.get("status", "UNKNOWN"),
            "aliases": db_data.get("aliases", [])
        }

# =============================================================================
# PHONEINFOGA ENGINE
# =============================================================================
class PhoneInfogaEngine:
    def __init__(self):
        self.api_key = CONFIG["opencage_key"]
        self.db_engine = MergedDatabaseEngine()
    
    def basic_analysis(self, parsed):
        try:
            type_map = {0:"Unknown",1:"Fixed",2:"Mobile",3:"Fixed/Mobile",4:"TollFree",5:"Premium"}
            analysis_type = number_type(parsed)
            return {
                "valid": phonenumbers.is_valid_number(parsed),
                "possible": phonenumbers.is_possible_number(parsed),
                "type": type_map.get(analysis_type, "Unknown"),
                "country_code": str(parsed.country_code),
                "country": phonenumbers.region_code_for_number(parsed) or "Unknown",
                "location": geocoder.description_for_number(parsed, "en") or "Unknown",
                "carrier": carrier.name_for_number(parsed, "en") or "Unknown",
                "timezones": list(timezone.time_zones_for_number(parsed)) or []
            }
        except Exception as e:
            return {"error": f"Analysis failed: {str(e)}"}
    
    def geolocation(self, location_hint):
        if not OPENCAGE_AVAILABLE:
            return {"status": "OpenCage not available"}
        try:
            geocoder_obj = OpenCageGeocode(self.api_key)
            results = geocoder_obj.geocode(f"{location_hint}, India")
            if results and len(results) > 0:
                primary = results[0]
                coords = primary['geometry']
                return {
                    "status": "SUCCESS",
                    "latitude": coords['lat'],
                    "longitude": coords['lng'],
                    "address": primary['formatted'],
                    "google_maps": f"https://maps.google.com/?q={coords['lat']},{coords['lng']}"
                }
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}
        return {"status": "FAILED"}
    
    def generate_osint_links(self, formats):
        clean_10 = formats.get('clean_10', '')
        intl = formats.get('international', '')
        return {
            "google": f"https://www.google.com/search?q={urllib.parse.quote(intl)}",
            "truecaller": f"https://www.truecaller.com/search/in/{clean_10}",
            "whatsapp": f"https://wa.me/+91{clean_10}",
            "facebook": f"https://www.facebook.com/search/top?q={urllib.parse.quote(intl)}",
            "twitter": f"https://twitter.com/search?q={urllib.parse.quote(intl)}"
        }
    
    def full_scan(self, phone_input):
        parsed, formats = normalize_phone(phone_input)
        if not parsed:
            return {"status": "ERROR", "error": formats["error"]}
        
        # 🔥 SINGLE MERGED DATABASE LOOKUP
        clean_10 = formats['clean_10']
        db_match = self.db_engine.check_merged_database(clean_10)
        
        basic = self.basic_analysis(parsed)
        location_hint = basic.get("location", "India")
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "input": phone_input,
            "formats": formats,
            "database": db_match,
            "basic": basic,
            "geo": self.geolocation(location_hint),
            "osint": self.generate_osint_links(formats),
            "status": "SUCCESS" if basic.get("valid", False) else "INVALID"
        }
        return results

# =============================================================================
# EMAIL & USERNAME TOOLS
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
# DISPLAY SYSTEM
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
    
    print(style("\n" + "="*115 + "\n🔥 SINGLE MERGED DATABASE - v6.5\n" + "="*115, 'c', bold=True))
    for name, url in CONFIG["social"].items():
        print(style(f"{name.upper()}:", 'g', bold=True) + f" {style(url, 'b', underline=True)}")
    print(style("="*115, 'c', bold=True) + "\n")

def display_phone_results(results):
    print(style("\n🔍 MERGED DATABASE TRACKER", 'm', bold=True).center(115))
    print(style("="*115, 'c'))
    status_color = 'g' if results['status']=='SUCCESS' else 'r'
    print(style(f"📊 STATUS: {results['status']}", status_color, bold=True))
    
    # 🔥 MERGED DATABASE DISPLAY
    db = results.get('database', {})
    if db.get('hit', False):
        db_engine = MergedDatabaseEngine()
        db_data = db_engine.get_display_data(db['data'])
        print(f"\n{style('🎯 MERGED DATABASE HIT!', 'g', bold=True)}")
        print(f"  {style('👤 NAME:', 'y', bold=True)} {style(db_data['name'], 'w', bold=True)}")
        print(f"  {style('📍 LOCATION:', 'y', bold=True)} {style(db_data['location'], 'g', bold=True)}")
        print(f"  {style('📶 CARRIER:', 'y', bold=True)} {style(db_data['carrier'], 'c', bold=True)}")
        print(f"  {style('⚡ STATUS:', 'y', bold=True)} {style(db_data['status'], 'g', bold=True)}")
        print(f"  {style('🔑 MATCHED:', 'y')} {style(db['key'], 'm', bold=True)}")
    else:
        print(f"\n{style('❌ No Database Match', 'y')}")
    
    print(f"\n{style('📱 PHONE FORMATS', 'b', bold=True)}")
    for fmt, value in results['formats'].items():
        if fmt != 'all_formats':
            print(f"  {style(fmt.upper(), 'y')}: {style(value, 'w')}")
    
    basic = results['basic']
    print(f"\n{style('📊 BASIC INFO', 'b', bold=True)}")
    print(f"  {style('TYPE:', 'y')} {basic.get('type', 'N/A')} | {style('CARRIER:', 'y')} {basic.get('carrier', 'N/A')}")
    
    geo = results['geo']
    if geo.get('status') == 'SUCCESS':
        print(f"\n{style('🗺️ GEOLOCATION', 'b', bold=True)}")
        print(f"  {style('📍 MAPS:', 'y')} {style(geo['google_maps'], 'b', underline=True)}")
    
    print(f"\n{style('🔗 OSINT LINKS', 'b', bold=True)}")
    for name, link in list(results['osint'].items())[:5]:
        print(f"  {style(name.title(), 'y')}: {style(link, 'b', underline=True)}")

# =============================================================================
# MAIN LOOP
# =============================================================================
def open_social_links():
    def open_url(url):
        try: webbrowser.open(url); time.sleep(1)
        except: pass
    threads = []
    for url in SOCIAL_LINKS[:2]:
        t = threading.Thread(target=open_url, args=(url,))
        t.start()
        threads.append(t)
    for t in threads: t.join()

def main():
    setup_dirs()
    log_message("🚀 WHP-TRACKER v6.5 - SINGLE MERGED DATABASE!", "SUCCESS")
    open_social_links()
    
    phone_engine = PhoneInfogaEngine()
    
    while True:
        show_banner()
        print(style("1. PHONE TRACKER (Merged DB)", 'g', bold=True))
        print(style("2. EMAIL HUNTER (25+)", 'g', bold=True))
        print(style("3. USERNAME SCAN (400+)", 'g', bold=True))
        print(style("4. SOCIAL LINKS", 'g', bold=True))
        print(style("0. EXIT", 'r', bold=True))
        
        choice = input(style("\nWHP> ", 'c', bold=True)).strip()
        
        if choice == '1':
            phone = input(style("Enter Phone (+91/91/10-digit): ", 'c')).strip()
            if phone:
                results = phone_engine.full_scan(phone)
                show_banner()
                display_phone_results(results)
                save_results(results, f"phone_{results['formats'].get('clean_10', 'unknown')}")
            
        elif choice == '2':
            username = input(style("Enter Username: ", 'c')).strip()
            results = email_hunter(username)
            show_banner()
            print(style(f"Generated {results['total']} emails:", 'g', bold=True))
            for email in results['emails'][:10]: print(style(email, 'b'))
            save_results(results, f"email_{username}")
            
        elif choice == '3':
            username = input(style("Enter Username: ", 'c')).strip()
            results = username_scanner(username)
            show_banner()
            print(style(f"Found {results.get('count', 0)} accounts:", 'g', bold=True))
            for account in results.get('found', [])[:10]: print(style(account, 'b'))
            save_results(results, f"user_{username}")
            
        elif choice == '4': open_social_links()
        elif choice == '0': log_message("👋 Goodbye!", "SUCCESS"); sys.exit(0)
        else: print(style("Invalid!", 'r', bold=True))
        
        input(style("\nPress Enter...", 'y'))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(style("\nGoodbye!", 'y'))
        sys.exit(0)
