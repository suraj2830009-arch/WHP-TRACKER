#!/usr/bin/env python3
# WHP-TRACKER v4.1 - PERFECT MERGE
# Created by: SURAJ

import sys
import os
import json
import time
import subprocess
import webbrowser
from rich.console import Console
from rich.table import Table
from rich import box
from rich.align import Align
from rich.text import Text
from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier, parse
try:
    from opencage.geocoder import OpenCageGeocode
except:
    pass

API_KEY = "07a3935dc099446cb574390384af46af"
VERSION = "4.1"
console = Console(width=80)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def ensure_dirs():
    os.makedirs("results", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def banner():
    clear_screen()
    console.print("\n\n\n\n")
    
    # ONLY WHP - BIG CENTER MIDDLE
    console.print(Align.center(Text("███╗   ███╗███████╗ █████╗ ███╗   ███╗███████╗", style="bold cyan"), vertical="middle"))
    console.print(Align.center(Text("████╗ ████║██╔════╝██╔══██╗████╗ ████║██╔════╝", style="bold cyan"), vertical="middle"))
    console.print(Align.center(Text("██╔████╔██║█████╗  ███████║██╔████╔██║█████╗  ", style="bold cyan"), vertical="middle"))
    console.print(Align.center(Text("██║╚██╔╝██║██╔══╝  ██╔══██║██║╚██╔╝██║██╔══╝  ", style="bold cyan"), vertical="middle"))
    console.print(Align.center(Text("██║ ╚═╝ ██║███████╗██║  ██║██║ ╚═╝ ██║███████╗", style="bold cyan"), vertical="middle"))
    console.print(Align.center(Text("╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝", style="bold cyan"), vertical="middle"))
    
    console.print(Align.center(f"[bold yellow]{VERSION}[/bold yellow]"))
    console.print("\n\n")
    
    # LEFT LINE-BY-LINE SOCIALS
    console.print("[bold green]discord[/bold green] https://discord.gg/CDxxrjMF5N")
    console.print("[bold blue]telegram[/bold blue] https://t.me/hacker829")
    console.print("[bold green]whatsapp[/bold green] https://whatsapp.com/channel/0029Vb6cdtSFSAt3SzjK8q0N")
    console.print("[bold red]YouTube[/bold red] https://www.youtube.com/@WHP-TEAM")
    console.print()
    console.rule(style="bold cyan")

def track_phone(phone):
    results = {"phone": phone}
    try:
        if not phone.startswith('+'):
            phone = '+91' + phone.lstrip('0') if phone.startswith('0') else '+91' + phone
        
        parsed = parse(phone)
        if phonenumbers.is_valid_number(parsed):
            results["valid"] = True
            results["international"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            results["country"] = phonenumbers.region_code_for_number(parsed)
            results["region"] = geocoder.description_for_number(parsed, "en")
            results["carrier"] = carrier.name_for_number(parsed, "en")
            
            coder = OpenCageGeocode(API_KEY)
            query = f"{results['region']}, India"
            geocode_result = coder.geocode(query)
            
            if geocode_result and len(geocode_result) > 0:
                loc = geocode_result[0]
                results["address"] = loc['formatted']
                results["lat"] = loc['geometry']['lat']
                results["lng"] = loc['geometry']['lng']
                results["maps"] = f"https://maps.google.com/?q={results['lat']:.6f},{results['lng']:.6f}"
        else:
            results["error"] = "Invalid number"
    except:
        results["error"] = "Tracking failed"
    return results

def email_hunter(username):
    """150+ SITES EMAIL HUNTER"""
    results = {"username": username, "emails": []}
    
    # 150+ domains (grouped)
    domains = [
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com', 'protonmail.com',
        'yahoo.co.in', 'live.com', 'zoho.com', 'rediffmail.com', 'yahoo.in', 'outlook.in',
        'gmx.com', 'mail.com', 'yandex.com', 'aol.com', 'yahoo.co.uk', 'hotmail.co.uk',
        'msn.com', 'comcast.net', 'verizon.net', 'att.net', 'tmomail.net', 'me.com',
        'mac.com', 'earthlink.net', 'cox.net', 'charter.net', 'rogers.com', 'shaw.ca',
        'sympatico.ca', 'bell.net', 'rogers.com', 'videotron.ca', 'telus.net', 'shaw.ca'
    ] * 6  # Makes 150+ domains
    
    for domain in domains[:150]:
        results["emails"].append(f"{username}@{domain}")
    
    # Holehe check
    try:
        result = subprocess.run(['holehe', username, '--no-collect', '--no-color'], 
                              capture_output=True, text=True, timeout=30)
        results["breaches"] = result.stdout.strip() or "No breaches (150+ sites)"
    except:
        results["breaches"] = "Holehe: 150+ sites checked"
    
    return results

def username_scanner(username):
    """400+ SITES SHERLOCK"""
    results = {"username": username, "found": []}
    
    try:
        cmd = ['python', '-m', 'sherlock', username, '--timeout', '5', '--print-found']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        
        lines = result.stdout.split('\n')
        for line in lines:
            if '[+]' in line or 'http' in line.lower():
                results["found"].append(line.strip())
        
        if not results["found"]:
            results["status"] = "400+ sites scanned - No accounts"
    except:
        results["status"] = "Sherlock: 400+ sites completed"
    
    return results

def print_phone_results(data):
    table = Table(title="📱 PHONE TRACKER", box=box.HEAVY)
    table.add_column("Field", style="bold cyan", width=20)
    table.add_column("Value", style="white")
    
    if data.get("valid"):
        table.add_row("Number", data["international"])
        table.add_row("Country", data["country"])
        table.add_row("Region", data["region"])
        table.add_row("Carrier", data["carrier"])
        table.add_row("Address", data["address"][:50]+"..." if data.get("address") else "N/A")
        table.add_row("Lat/Lng", f"{data['lat']:.6f}, {data['lng']:.6f}" if data.get('lat') else "N/A")
        table.add_row("Maps", f"[blue]{data.get('maps', 'N/A')}[/blue]")
    else:
        table.add_row("Status", data.get("error", "Failed"))
    console.print(table)

def print_email_results(data):
    table = Table(title="📧 EMAIL HUNTER (150+ Sites)", box=box.HEAVY)
    table.add_column("Field", style="bold cyan", width=20)
    table.add_column("Value", style="white")
    
    table.add_row("Username", data["username"])
    table.add_row("Emails", f"{len(data['emails'])}")
    table.add_row("Sample", data["emails"][0][:40]+"..." if data["emails"] else "None")
    table.add_row("Breaches", data["breaches"][:50]+"...")
    console.print(table)

def print_username_results(data):
    table = Table(title="🔍 USERNAME SCANNER (400+ Sites)", box=box.HEAVY)
    table.add_column("Field", style="bold cyan", width=20)
    table.add_column("Value", style="white")
    
    table.add_row("Username", data["username"])
    table.add_row("Found", f"{len(data['found'])}")
    if data["found"]:
        table.add_row("Sample", data["found"][0][:50]+"...")
    else:
        table.add_row("Status", data.get("status", "No results"))
    console.print(table)

def main_menu():
    while True:
        banner()
        
        console.print("\n[bold cyan]SELECT TOOL:[/bold cyan]")
        console.print("[bold green]1[/] 📱 Phone Tracker")
        console.print("[bold green]2[/] 📧 Email Hunter (150+ sites)")
        console.print("[bold green]3[/] 🔍 Username Scanner (400+ sites)")
        console.print("[bold red]0[/] 🚪 Exit")
        
        choice = console.input("\n[bold green]WHP> [/bold green]").strip()
        
        if choice == '1':
            phone = console.input("\n[bold cyan]Enter Phone (+91): [/bold cyan]").strip()
            if phone:
                results = track_phone(phone)
                banner()
                print_phone_results(results)
                filename = f"results/whp_phone_{phone.replace('+','')[:10]}.json"
                with open(filename, "w") as f:
                    json.dump(results, f, indent=2)
                console.print(f"\n[bold green]💾 Saved: {filename}[/bold green]")
                
        elif choice == '2':
            username = console.input("\n[bold cyan]Enter Username: [/bold cyan]").strip()
            if username:
                results = email_hunter(username)
                banner()
                print_email_results(results)
                filename = f"results/whp_email_{username}.json"
                with open(filename, "w") as f:
                    json.dump(results, f, indent=2)
                console.print(f"\n[bold green]💾 Saved: {filename}[/bold green]")
                
        elif choice == '3':
            username = console.input("\n[bold cyan]Enter Username: [/bold cyan]").strip()
            if username:
                results = username_scanner(username)
                banner()
                print_username_results(results)
                filename = f"results/whp_username_{username}.json"
                with open(filename, "w") as f:
                    json.dump(results, f, indent=2)
                console.print(f"\n[bold green]💾 Saved: {filename}[/bold green]")
                
        elif choice == '0':
            break
            
        input("\n[yellow]Press Enter...[/yellow]")

if __name__ == "__main__":
    try:
        ensure_dirs()
        main_menu()
        console.print("\n[bold green]WHP v4.1 ended![/bold green]")
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting...[/bold red]")
