log_file = "python-detection-lab/sample_logs.txt"

print("[*] Parsing login log file...")
print("-" * 60)

failures = 0
successes = 0

with open(log_file, "r") as f:
    for line in f:
        if not line:
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

        print(f"  Time: {timestamp} | Status: {status} | User: {user} | IP: {ip}")

print("-" * 60)
print(f"[*]  Total Events : {failures + successes}")
print(f"[*]  Failed Logins : {failures}")    
print(f"[*]  Successful Logins : {successes}")