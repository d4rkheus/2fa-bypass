import pyotp
import os
import time
import sys
from colorama import Fore, Style

os.system('cls')

def get_current_code(key):
    totp = pyotp.TOTP(key)
    return totp.now()

def read_key_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    
key = input("Give key (without space): ")
print(f"{Fore.LIGHTGREEN_EX}[DARKHEUS]{Fore.RESET} Initial code : " + get_current_code(key))

try:
    while True:
        current_code = get_current_code(key)
        print(f"{Fore.LIGHTGREEN_EX}[DARKHEUS]{Fore.RESET} Current Code : " + current_code)
        time.sleep(1)  
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)
