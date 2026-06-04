#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Tool Name: Password Cracker Core v1.0
# Developer: Imran (রানা ভাই / RANA VHAI)
# Platform : Pydroid 3 / Termux
# ------------------------------------------------------------------

import time
import os

# টার্মিনাল কালার কোডস
GREEN  = '\033[92m'
YELLOW = '\033[93m'
RED    = '\033[91m'
CYAN   = '\033[96m'
RESET  = '\033[0m'

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}==================================================")
    print(f"  ____                                      _             \n"
          f" |  _ \\ __ _ ___ ___ _____      _____  _ __| | _____ _ __ \n"
          f" | |_) / _` / __/ __/ _ \\ \\ /\\ / / _ \\| '__| |/ / _ \\ '__|\n"
          f" |  __/ (_| \\__ \\ (_| (_) \\ V  V / (_) | |  |   <  __/ |   \n"
          f" |_|   \\__,_|___/\\___\\___/ \\_/\\_/ \\___/|_|  |_|\\_\\___|_|   ")
    print(f"          Advanced Password Cracker Engine v1.0")
    print(f"               🔥 Custom Built for Imran 🔥")
    print(f"=================================================={RESET}")

def brute_force_login(target_username, target_password_real):
    print(f"\n{YELLOW}[*] Initializing wordlist stream...{RESET}")
    time.sleep(1)
    
    attempts = 0
    start_time = time.time()
    
    try:
        with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                guess = line.strip()
                attempts += 1
                
                # লজিক্যাল ম্যাচিং
                if guess == target_password_real:
                    print(f"\n{GREEN}[✓] PASSWORD FOUND!{RESET}")
                    print(f"--------------------------------")
                    print(f"{CYAN}Username: {RESET}{target_username}")
                    print(f"{CYAN}Password: {RESET}{YELLOW}{guess}{RESET}")
                    print(f"{CYAN}Attempts: {RESET}{attempts}")
                    print(f"{CYAN}Time:     {RESET}{time.time() - start_time:.2f} seconds")
                    return True
                
                if attempts % 500 == 0:
                    print(f"{YELLOW}[*] Testing password count: {attempts}...{RESET}", end="\r")
                    
        print(f"\n{RED}[!] Password not found in wordlist!{RESET}")
                    
    except FileNotFoundError:
        print(f"\n{RED}[!] Error: 'wordlist.txt' ফাইলটি খুঁজে পাওয়া যায়নি!{RESET}")
        return False

def main():
    while True:
        banner()
        print(f"{GREEN}[01]{CYAN} Start Wordlist Password Cracker")
        print(f"{RED}[99]{RESET} Shut Down Engine")
        print(f"{CYAN}==================================================")
        
        choice = input(f"{YELLOW}[+] Select Option: {RESET}").strip()
        
        if choice == '01' or '1':
            user = input(f"{CYAN}[+] Target Username: {RESET}")
            real_pass = input(f"{CYAN}[+] Target Real Password: {RESET}")
            brute_force_login(user, real_pass)
            input(f"\n{YELLOW}[Press Enter to continue...]{RESET}")
        elif choice == '99':
            print(f"\n{YELLOW}[*] Shutting down, রানা ভাই!{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid Selection!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
