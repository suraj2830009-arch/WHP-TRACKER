#!/bin/bash
# WHP-TRACKER SETUP
pkg update -y && pkg upgrade -y
pkg install python -y
pip install --upgrade pip
pip install phonenumbers opencage colorama geopy holehe httpx==0.24.1 httpcore==0.17.3 requests==2.31.0 urllib3==1.26.15
pip install phonenumbers opencage colorama holehe sherlock-project
chmod +x WHP-TRACKER.py
echo -e "\033[0;32m[+] WHP-TRACKER Updated. Run: python WHP-TRACKER.py\033[0m"
