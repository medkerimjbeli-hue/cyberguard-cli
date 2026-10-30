
from collections import Counter
import re
import os

LOG_FILE = os.path.join("samples", "auth.log")


def analyze_logs(file_path):
    failed_ips = Counter()
    failed_attempts = 0
    successful_logins = 0

    with open(file_path, "r") as file:
        for line in file:
            if "Failed password" in line:
                failed_attempts += 1

                match = re.search(r"from (\d{1,3}(?:\.\d{1,3}){3})", line)

                if match:
                    failed_ips[match.group(1)] += 1

            elif "Accepted password" in line:
                successful_logins += 1

    suspicious_ips = {
        ip: count
        for ip, count in failed_ips.items()
        if count >= 3
    }

    return {
        "failed_attempts": failed_attempts,
        "successful_logins": successful_logins,
        "failed_ips": failed_ips,
        "suspicious_ips": suspicious_ips
    }


def run_log_analyzer():
    print("\n=== AUTHENTICATION LOG ANALYZER ===")

    if not os.path.isfile(LOG_FILE):
        print(f"Error: Log file not found: {LOG_FILE}")
        return

    results = analyze_logs(LOG_FILE)

    print(f"\nFailed login attempts: {results['failed_attempts']}")
    print(f"Successful logins: {results['successful_logins']}")

    print("\nFailed attempts by IP:")

    if results["failed_ips"]:
        for ip, count in results["failed_ips"].most_common():
            print(f"- {ip}: {count} failed attempts")
    else:
        print("No failed login attempts found.")

    print("\nSuspicious IPs (3+ failures):")

    if results["suspicious_ips"]:
        for ip, count in results["suspicious_ips"].items():
            print(f"[WARNING] {ip}: {count} failed attempts")
    else:
        print("No suspicious IPs detected.")
