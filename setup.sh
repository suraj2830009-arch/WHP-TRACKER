#!/bin/bash
clear
echo -e "\033[1;32m[*] UPDATING WHP-TRACKER SYSTEM (By Suraj)...\033[0m"
pkg update && pkg upgrade -y
pkg install python git php curl wget clang -y

# Installing OSINT dependencies
pip install holehe requests colorama phonenumbers geopy

# Setting permissions
chmod +x WHP-TRACKER.py

echo -e "\033[1;36m[+] Setup Updated Successfully!\033[0m"
echo -e "\033[1;33m[!] Type 'python WHP-TRACKER.py' to launch.\033[0m"
