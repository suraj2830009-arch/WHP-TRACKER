#!/bin/bash

# WHP-TRACKER SETUP SCRIPT
# OWNER: SURAJ [R]

# Colors
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
RESET='\033[0m'

echo -e "${CYAN}--------------------------------------------------${RESET}"
echo -e "${GREEN}      WHP-TRACKER INSTALLER BY SURAJ [R]          ${RESET}"
echo -e "${CYAN}--------------------------------------------------${RESET}"

echo -e "${YELLOW}[*] Updating system packages...${RESET}"
pkg update -y && pkg upgrade -y

echo -e "${YELLOW}[*] Installing Python and dependencies...${RESET}"
pkg install python -y
pkg install git -y

echo -e "${YELLOW}[*] Installing required Python libraries...${RESET}"
# We install specific versions to avoid 'urllib3' compatibility errors
pip install --upgrade pip
pip install phonenumbers opencage colorama geopy

echo -e "${YELLOW}[*] Installing OSINT Engine (holehe)...${RESET}"
pip install holehe

echo -e "${YELLOW}[*] Fixing possible library conflicts...${RESET}"
# This ensures requests and urllib3 work together perfectly
pip install requests==2.31.0 urllib3==1.26.15

echo -e "${YELLOW}[*] Granting execution permissions...${RESET}"
chmod +x WHP-TRACKER.py

echo -e "${GREEN}--------------------------------------------------${RESET}"
echo -e "${GREEN}[+] SETUP COMPLETE!${RESET}"
echo -e "${CYAN}    To start the tool, type:${RESET}"
echo -e "${YELLOW}    python WHP-TRACKER.py${RESET}"
echo -e "${GREEN}--------------------------------------------------${RESET}"
