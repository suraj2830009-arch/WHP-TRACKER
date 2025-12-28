#!/data/data/com.termux/files/usr/bin/bash
echo " WHP-TRACKER TERMUX SETUP"

# Termux ONLY 
pkg update -y && pkg upgrade -y
pkg install python python-pip git -y

# UPGRADE pip 2x
pip install --upgrade pip --user
pip install --upgrade pip setuptools wheel --user

# ALL PACKAGES (sherlock + holehe FIXED)
pip install phonenumbers==8.13.42 opencage colorama requests holehe sherlock --user

echo "✅ Termux Setup COMPLETE! Run: python WHP-TRACKER.py"
