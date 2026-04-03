from config import *
import datetime

def simulate_bruteforce():
    print(f"[*] Simulating brute force against: {TARGET_ACCOUNT}")
    print(f"[*] Source IP: {ATTACKER_IP}")
    print("-" * 60)

    for i in range(1, ATTEMPTS + 1):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "FAILURE"

        if i == ATTEMPTS:
            status = "SUCCESS"

        log_entry = f"{timestamp} | {status} | User: {TARGET_ACCOUNT} | IP: {ATTACKER_IP} Attempt: {i}"
        print(log_entry)

    print("-" * 60)
    print(f"[!] {ATTEMPTS - 1} failed attempts followed by a SUCCESS, classic brute force pattern.")