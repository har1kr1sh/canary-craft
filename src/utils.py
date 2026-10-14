import os
from colorama import Fore, Style, init

init(autoreset=True)

def ensure_directories():
    """Ensure required output and config directories exist."""
    os.makedirs("output", exist_ok=True)
    os.makedirs("config", exist_ok=True)
    os.makedirs("banner", exist_ok=True)
    os.makedirs("assets", exist_ok=True)

def print_alert(token: str, src_ip: str, user_agent: str, timestamp: str):
    """Render high-priority SOC alert box for triggered honey-tokens."""
    print("\n" + "🚨 " * 18)
    print(f"{Fore.RED}{Style.BRIGHT}[!] ALERT: CANARY HONEY-TOKEN TRIP DETECTED!{Style.RESET_ALL}")
    print(f" Timestamp  : {timestamp}")
    print(f" Token ID   : {Fore.YELLOW}{token}{Style.RESET_ALL}")
    print(f" Source IP  : {Fore.CYAN}{src_ip}{Style.RESET_ALL}")
    print(f" User-Agent : {user_agent}")
    print("🚨 " * 18 + "\n")
