# main.py

import argparse
from config import *
from simulate import simulate_bruteforce
from parser import parse_logs
from detector import detect_anomalies
from reporter import generate_report

def main():
    parser = argparse.ArgumentParser(description="Detection as Code Pipeline")
    parser.add_argument("--log-file", default=LOG_FILE, help="Path to log file")
    parser.add_argument("--threshold", type=int, default=ALERT_THRESHOLD, help="Alert threshold for failed logins")
    args = parser.parse_args()

    print("=" * 60)
    print(" DETECTION PIPELINE STARTING")
    print("=" * 60)

    simulate_bruteforce()
    events = parse_logs(args.log_file)
    alerts, ip_map = detect_anomalies(events, args.threshold)
    generate_report(alerts, ip_map)

    print("=" * 60)
    print(" PIPELINE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()