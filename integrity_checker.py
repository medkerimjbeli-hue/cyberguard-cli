
import hashlib
import os
import json

BASELINE_FILE = "integrity_baselines.json"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def load_baselines():
    if not os.path.exists(BASELINE_FILE):
        return {}

    with open(BASELINE_FILE, "r") as file:
        return json.load(file)


def save_baselines(baselines):
    with open(BASELINE_FILE, "w") as file:
        json.dump(baselines, file, indent=4)


def run_integrity_checker():
    print("\n=== FILE INTEGRITY CHECKER ===")
    print("[1] Register file baseline")
    print("[2] Check file integrity")

    choice = input("\nSelect an option: ")
    file_path = input("Enter the file path: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    file_hash = calculate_hash(file_path)
    baselines = load_baselines()

    if choice == "1":
        baselines[os.path.abspath(file_path)] = file_hash
        save_baselines(baselines)

        print("\nBaseline saved successfully!")
        print(f"SHA-256: {file_hash}")

    elif choice == "2":
        absolute_path = os.path.abspath(file_path)

        if absolute_path not in baselines:
            print("No baseline found. Register this file first.")
            return

        if baselines[absolute_path] == file_hash:
            print("\n[SAFE] File has not changed.")
        else:
            print("\n[WARNING] File has been modified!")

    else:
        print("Invalid option.")
