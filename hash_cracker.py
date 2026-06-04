#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Tool Name: HashCracker & Generator Core Framework v3.5
# Developer: Imran (রানা ভাই / RANA VHAI)
# Platform : Pydroid 3 / Termux (Android Environment)
# Structure: Modular (Requires external 'wordlist.txt')
# ------------------------------------------------------------------

import os
import sys
import time
import hashlib

# টার্মিনাল কালার কোডস
GREEN  = '\033[92m'
YELLOW = '\033[93m'
RED    = '\033[91m'
CYAN   = '\033[96m'
RESET  = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"{CYAN}==================================================")
    print(f"  _   _           _      ____                _             \n"
          f" | | | | __ _ ___| |__  / ___|_ __ __ _  ___| | _____ _ __ \n"
          f" | |_| |/ _` / __| '_ \| |   | '__/ _` |/ __| |/ / _ \\ '__|\n"
          f" |  _  | (_| \__ \ | | | |___| | | (_| | (__|   <  __/ |   \n"
          f" |_| |_|\__,_|___/_| |_|\____|_|  \__,_|\___|_|\_\___|_|   ")
    print(f"       Advanced Hash Cracker & Generator Tool v3.5")
    print(f"           [ Separate External Wordlist Architecture ]")
    print(f"=================================================={RESET}")

def get_hash_object(algo, text):
    """ নির্দিষ্ট অ্যালগরিদম অনুযায়ী হ্যাশ রিটার্ন করার নোড """
    encoded_text = text.encode('utf-8', errors='ignore')
    if algo == '1': return hashlib.md5(encoded_text).hexdigest()
    if algo == '2': return hashlib.sha1(encoded_text).hexdigest()
    if algo == '3': return hashlib.sha256(encoded_text).hexdigest()
    if algo == '4': return hashlib.sha512(encoded_text).hexdigest()
    return hashlib.sha256(encoded_text).hexdigest()

def generate_hash():
    """ অরিজিনাল পাসওয়ার্ডকে হ্যাশ করে এক্সটার্নাল ফাইলে সেভ করার মডিউল """
    clear_screen()
    banner()
    print(f"{CYAN}[ Module 02: Generate & Export Hash ]{RESET}\n")
    
    password = input(f"{YELLOW}[+] Enter Original Password to Hash: {RESET}").strip()
    if not password:
        print(f"{RED}[!] Password cannot be empty!{RESET}")
        time.sleep(1.5)
        return

    print(f"\n{CYAN}[⚡] Select Hash Algorithm:{RESET}")
    print(f"{GREEN}[1]{RESET} MD5")
    print(f"{GREEN}[2]{RESET} SHA-1")
    print(f"{GREEN}[3]{RESET} SHA-256")
    print(f"{GREEN}[4]{RESET} SHA-512")
    
    algo_choice = input(f"\n{YELLOW}[+] Choose Algorithm (1-4): {RESET}").strip()
    hashed = get_hash_object(algo_choice, password)
    
    print(f"\n{CYAN}[ 🔑 GENERATED HASH REPORT ]{RESET}")
    print(f"--------------------------------------------------")
    print(f"{GREEN}[✓] Original Text : {RESET}{password}")
    print(f"{GREEN}[✓] Result Hash   : {RESET}{YELLOW}{hashed}{RESET}")
    print(f"--------------------------------------------------")
    
    save_choice = input(f"{YELLOW}[+] আপনি কি এই রেজাল্টটি 'hash_output.txt' ফাইলে সেভ করবেন? (y/n): {RESET}").strip().lower()
    if save_choice == 'y':
        try:
            with open("hash_output.txt", "a", encoding="utf-8") as f:
                f.write(f"Original: {password} | Hash: {hashed}\n")
            print(f"{GREEN}[✓] সফলভাবে 'hash_output.txt' ফাইলে এক্সপোর্ট করা হয়েছে!{RESET}")
        except Exception as e:
            print(f"{RED}[!] ফাইল রাইট করতে সমস্যা হয়েছে: {e}{RESET}")

def crack_hash():
    """ আলাদা 'wordlist.txt' ফাইল থেকে ডাটা লোড করে ক্র্যাক করার মডিউল """
    clear_screen()
    banner()
    print(f"{CYAN}[ Module 01: External Wordlist Cracker Node ]{RESET}\n")
    
    target_hash = input(f"{YELLOW}[+] Enter the Target Hash Password: {RESET}").strip().lower()
    if not target_hash:
        print(f"{RED}[!] Hash field cannot be empty!{RESET}")
        time.sleep(1.5)
        return

    print(f"\n{CYAN}[⚡] Select Target Hash Type:{RESET}")
    print(f"{GREEN}[1]{RESET} MD5")
    print(f"{GREEN}[2]{RESET} SHA-1")
    print(f"{GREEN}[3]{RESET} SHA-256")
    print(f"{GREEN}[4]{RESET} SHA-512")
    
    type_choice = input(f"\n{YELLOW}[+] Choose Type (1-4): {RESET}").strip()
    
    # 📁 এক্সটার্নাল ফাইল পাথ চেক
    wordlist_path = "wordlist.txt"
    if not os.path.exists(wordlist_path):
        print(f"\n{RED}[!] Error: '{wordlist_path}' ফাইলটি খুঁজে পাওয়া যায়নি!{RESET}")
        print(f"{YELLOW}[*] দয়া করে পাইথন ফাইলের পাশে 'wordlist.txt' ফাইলটি তৈরি করে পাসওয়ার্ড লিস্টটি রাখুন।{RESET}")
        return

    print(f"\n{RED}[!] Activating External File Stream Sockets...{RESET}")
    print(f"{YELLOW}[*] Testing target against separate wordlist database...{RESET}\n")
    time.sleep(0.5)
    
    found = False
    start_time = time.time()
    attempts = 0
    
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                attempts += 1
                word = line.strip()
                if not word:
                    continue
                    
                guess_hash = get_hash_object(type_choice, word)
                
                if guess_hash == target_hash:
                    end_time = time.time()
                    print(f"{GREEN}[✓] HASH MATCHED FROM EXTERNAL DATABASE!{RESET}")
                    print(f"--------------------------------------------------")
                    print(f"{GREEN}[+] Target Hash      : {RESET}{target_hash}")
                    print(f"{GREEN}[+] Original Password: {RESET}{YELLOW}{word}{RESET} 🔥")
                    print(f"{GREEN}[+] Total Attempts   : {RESET}{attempts}")
                    print(f"{GREEN}[+] Time Elapsed     : {RESET}{end_time - start_time:.4f} seconds")
                    print(f"--------------------------------------------------")
                    found = True
                    break
    except Exception as e:
        print(f"{RED}[!] ফাইল রিড করার সময় সমস্যা হয়েছে: {e}{RESET}")
        return
            
    if not found:
        print(f"{RED}[!] Cracking Failed. Tested {attempts} words from '{wordlist_path}'.{RESET}")
        print(f"{YELLOW}[*] টার্গেট হ্যাশটি আলাদা টেক্সট ফাইলের কোনো পাসওয়ার্ডের সাথে মেলেনি।{RESET}")

def main_system():
    while True:
        clear_screen()
        banner()
        print(f"{GREEN}[01]{CYAN} Convert Hash -> Original Password (Reads separate wordlist.txt){RESET}")
        print(f"{GREEN}[02]{CYAN} Convert Original Password -> Hash (Saves to separate file){RESET}")
        print(f"{RED}[99]{RESET} Shut Down Framework")
        print(f"{CYAN}==================================================")
        
        choice = input(f"{YELLOW}[+] Select Framework Module: {RESET}").strip()
        
        if choice in ['1', '01']:
            crack_hash()
            input(f"\n{CYAN}[Press Enter to return to main menu...]{RESET}")
        elif choice in ['2', '02']:
            generate_hash()
            input(f"\n{CYAN}[Press Enter to return to main menu...]{RESET}")
        elif choice == '99' or choice.lower() == 'exit':
            print(f"\n{YELLOW}[*] Framework safely shut down, রানা ভাই!{RESET}\n")
            break
        else:
            print(f"{RED}[!] Invalid Selection.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    try: main_system()
    except KeyboardInterrupt: print(f"\n\n{RED}[!] Tool interrupted by operator.{RESET}\n")
