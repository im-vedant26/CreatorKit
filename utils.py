# utils.py
from colorama import Fore

def info(msg):
    print(Fore.CYAN + f"[INFO] {msg}")

def success(msg):
    print(Fore.GREEN + f"[SUCCESS] {msg}")

def error(msg):
    print(Fore.RED + f"[ERROR] {msg}")
