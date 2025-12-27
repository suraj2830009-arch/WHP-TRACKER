#!/bin/bash
#!/bin/bash
# WHP-TRACKER Setup
clear
echo -e "\e[1;33m[*] Fixing dependencies and installing requirements...\e[0m"
pkg update && pkg upgrade -y
pkg install python git -y
pip uninstall urllib3 requests -y
pip install --upgrade pip
pip install requests urllib3 colorama phonenumbers geopy holehe
chmod +x WHP-TRACKER.py
echo -e "\e[1;32m[+] Setup Complete! Run: python WHP-TRACKER.py\e[0m"
