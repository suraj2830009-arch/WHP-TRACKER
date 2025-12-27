#!/bin/bash

# WHP SETUP SCRIPT (BUG FIX VERSION)
# OWNER: SURAJ

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
RESET='\033[0m'

echo -e "${CYAN}[*] Patching System for WHP...${RESET}"
pkg update -y && pkg upgrade -y
pkg install python -y

echo -e "${YELLOW}[*] Installing stable networking libraries...${RESET}"
pip install --upgrade pip
# Forced versions to prevent the SSL handshake timeout in Termux
pip install httpx==0.24.1 httpcore==0.17.3 
pip install phonenumbers opencage colorama geopy holehe

# Fix for urllib3 compatibility
pip install requests==2.31.0 urllib3==1.26.15

chmod +x WHP.py

echo -e "${GREEN}[+] WHP Fix Applied!${RESET}"
echo -e "${CYAN}[!] Type 'python WHP-TRACKER.py' to launch.${RESET}"
