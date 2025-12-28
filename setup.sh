#!/bin/bash
echo " WHP-TRACKER TERMUX  SETUP..."

# Termux packages
pkg update -y && pkg upgrade -y
pkg install python git -y

# Upgrade pip
pip install --upgrade pip setuptools wheel

# Install ALL via pip (sherlock included)
pip install phonenumbers opencage colorama requests holehe sherlock

echo "✅ Setup Complete! Run: python WHP-TRACKER.py"
echo "📱 Termux Optimized - 100% Working!"
