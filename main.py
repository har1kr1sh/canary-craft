#!/usr/bin/env python3
"""
CanaryCraft — Dynamic Honey-Token & Canary Document Generator Engine
Author: Hari Krishnan (@har1kr1sh)
Role: SOC L2 / Detection Engineering Portfolio
"""

import argparse
import os
from colorama import Fore, Style, init
from src.document_generator import CanaryDocumentGenerator
from src.credential_generator import DecoyCredentialGenerator
from src.web_listener import start_listener
from src.utils import ensure_directories

init(autoreset=True)

def print_banner():
    banner_path = os.path.join("banner", "banner.txt")
    if os.path.exists(banner_path):
        with open(banner_path, "r") as f:
            print(Fore.CYAN + f.read() + Style.RESET_ALL)
    else:
        print(f"{Fore.CYAN}[ CanaryCraft — Deception & Honey-Token Generator ] - @har1kr1sh{Style.RESET_ALL}")

def main():
    ensure_directories()
    print_banner()

    parser = argparse.ArgumentParser(description="CanaryCraft: Active Defense & Deception Token Generator for SOCs.")
    parser.add_argument("--doc", help="Generate a canary Word document (.docx)", action="store_true")
    parser.add_argument("--env", help="Generate a decoy .env file", action="store_true")
    parser.add_argument("--aws", help="Generate a decoy AWS credentials file", action="store_true")
    parser.add_argument("--listener", help="Launch the CanaryCraft Webhook alert receiver", action="store_true")
    parser.add_argument("--server-url", help="Callback URL for the listener", default="http://localhost:8080")
    
    args = parser.parse_args()

    if args.listener:
        start_listener()
        return

    doc_gen = CanaryDocumentGenerator(listener_url=args.server_url)
    cred_gen = DecoyCredentialGenerator(listener_url=args.server_url)

    if args.doc:
        out_path = os.path.join("output", "Confidential_Executive_Payroll.docx")
        doc_gen.create_word_canary(out_path)
        print(f"{Fore.GREEN}[+] Canary MS Word Document created:{Style.RESET_ALL} {out_path}")

    if args.env:
        out_path = os.path.join("output", ".env")
        cred_gen.generate_env_file(out_path)
        print(f"{Fore.GREEN}[+] Decoy .env File created:{Style.RESET_ALL} {out_path}")

    if args.aws:
        out_path = os.path.join("output", "aws_credentials")
        cred_gen.generate_aws_credentials(out_path)
        print(f"{Fore.GREEN}[+] Decoy AWS Credentials file created:{Style.RESET_ALL} {out_path}")

    if not (args.doc or args.env or args.aws or args.listener):
        print(f"\n{Fore.YELLOW}[?] Interactive Selection:{Style.RESET_ALL}")
        print("1. Generate Canary Word Document (.docx)")
        print("2. Generate Decoy AWS Credentials File")
        print("3. Generate Decoy .env Config File")
        print("4. Start Canary Webhook Listener Server")
        
        choice = input("\nSelect an option (1-4): ").strip()
        if choice == "1":
            out_path = os.path.join("output", "Confidential_Executive_Payroll.docx")
            doc_gen.create_word_canary(out_path)
            print(f"{Fore.GREEN}[+] Canary Document generated at:{Style.RESET_ALL} {out_path}")
        elif choice == "2":
            out_path = os.path.join("output", "aws_credentials")
            cred_gen.generate_aws_credentials(out_path)
            print(f"{Fore.GREEN}[+] AWS Honey-Token created at:{Style.RESET_ALL} {out_path}")
        elif choice == "3":
            out_path = os.path.join("output", ".env")
            cred_gen.generate_env_file(out_path)
            print(f"{Fore.GREEN}[+] Decoy .env created at:{Style.RESET_ALL} {out_path}")
        elif choice == "4":
            start_listener()

if __name__ == "__main__":
    main()
