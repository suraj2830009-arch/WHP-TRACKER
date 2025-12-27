#!/bin/bash

# WHP SETUP SCRIPT
# OWNER: SURAJ

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[0;33m'
RESET='\033[0m'

echo -e "${CYAN}[*] Initializing System for WHP...${RESET}"
pkg update -y && pkg upgrade -y
pkg install python -y

echo -e "${YELLOW}[*] Installing dependencies...${RESET}"
pip install --upgrade pip
pip install phonenumbers opencage colorama geopy holehe

# Fix for urllib3/requests compatibility
pip install requests==2.31.0 urllib3==1.26.15

chmod +x WHP.py

echo -e "${GREEN}[+] WHP Setup Complete!${RESET}"
echo -e "${CYAN}[!] Type 'python WHP.py' to launch.${RESET}"
