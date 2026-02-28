import requests
import json
from datetime import datetime, timezone

# Load credentials
from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET

# Step 1 - Get access token
def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }
    response = requests.post(url, data=data)
    token = response.json().get("access_token")
    return token

# Step 2 - Pull sign-in logs
def get_signin_logs(token):
    url = "https://graph.microsoft.com/v1.0/auditLogs/signIns"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.json()

# Step 3 - Analyze logs
def analyze_logs(logs):
    failed_logins = {}
    off_hours = []

    for entry in logs.get("value", []):
        user = entry.get("userPrincipalName", "Unknown")
        status = entry.get("status", {})
        error_code = status.get("errorCode", 0)
        time_str = entry.get("createdDateTime", "")

        # Flag failed logins
        if error_code != 0:
            failed_logins[user] = failed_logins.get(user, 0) + 1

        # Flag off hours logins (before 6am or after 10pm)
        if time_str:
            time = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
            hour = time.astimezone().hour
            if hour < 6 or hour > 22:
                off_hours.append({
                    "user": user,
                    "time": time_str,
                    "hour": hour
                })

    return failed_logins, off_hours

# Step 4 - Print report
def print_report(failed_logins, off_hours):
    print("\n========== SIGN-IN LOG ANALYSIS ==========\n")

    print("--- Failed Login Attempts ---")
    if failed_logins:
        for user, count in sorted(failed_logins.items(), key=lambda x: x[1], reverse=True):
            flag = " ⚠️  HIGH" if count >= 3 else ""
            print(f"  {user}: {count} failed attempt(s){flag}")
    else:
        print("  No failed logins detected.")

    print("\n--- Off-Hours Authentication ---")
    if off_hours:
        for entry in off_hours:
            print(f"  {entry['user']} logged in at hour {entry['hour']} ({entry['time']})")
    else:
        print("  No off-hours logins detected.")

    print("\n==========================================\n")

# Run it
if __name__ == "__main__":
    print("Authenticating...")
    token = get_access_token()
    if not token:
        print("Failed to get token. Check your credentials.")
    else:
        print("Pulling sign-in logs...")
        logs = get_signin_logs(token)
        failed, offhours = analyze_logs(logs)
        print_report(failed, offhours)