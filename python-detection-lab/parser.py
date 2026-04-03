from config import *

def parse_logs(log_file=LOG_FILE):
    print("[*] Parsing login log file...")
    print("-" * 60)

    failures = 0
    successes = 0
    events = []

    with open(log_file, "r") as f:
        for line in f:
            if not line.strip():
                continue

            parts = line.split("|")
            timestamp = parts[0].strip()
            status = parts[1].strip()
            user = parts[2].strip().replace("User: ", "")
            ip = parts[3].strip().replace("IP: ", "")

            if status == "FAILURE":
                failures += 1
            elif status == "SUCCESS":
                successes += 1

            events.append({
                "timestamp": timestamp,
                "status": status,
                "user": user,
                "ip": ip
            })

            print(f"  Time: {timestamp} | Status: {status} | User: {user} | IP: {ip}")

    print("-" * 60)
    print(f"[*]  Total Events : {failures + successes}")
    print(f"[*]  Failed Logins : {failures}")
    print(f"[*]  Successful Logins : {successes}")

    return events