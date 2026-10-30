# 🛡️ CyberGuard CLI

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)
![Focus](https://img.shields.io/badge/focus-defensive%20security-informational)
![License](https://img.shields.io/badge/license-MIT-green)

A defensive cybersecurity toolkit for the command line, written in pure Python with no third-party packages. It bundles four small tools that cover everyday security tasks: checking passwords, generating them, detecting file tampering, and spotting brute-force attempts in authentication logs.

Built as a hands-on way to practice security fundamentals: hashing, secure randomness, log parsing, and testing.

```text
   ______      __               ______                      __
  / ____/_  __/ /_  ___  _____ / ____/___  __  ______  ____/ /
 / /   / / / / __ \/ _ \/ ___// / __/ __ \/ / / / __ \/ __  /
/ /___/ /_/ / /_/ /  __/ /   / /_/ / /_/ / /_/ / / / / /_/ /
\____/\__, /_.___/\___/_/    \____/\____/\__,_/_/ /_/\__,_/
     /____/

       [ CYBERGUARD CLI v1.0 ]
       Defensive Security Toolkit
```

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Running Tests](#running-tests)
- [Security Notes](#security-notes)
- [Roadmap](#roadmap)
- [What I Learned](#what-i-learned)
- [Author](#author)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features

| Tool | What it does |
|------|--------------|
| **Password Strength Analyzer** | Scores a password out of 6 based on length and character variety, then suggests improvements. |
| **Secure Password Generator** | Creates random passwords of 8 to 64 characters using Python's cryptographically secure `secrets` module. |
| **File Integrity Checker** | Computes SHA-256 hashes, saves a baseline, and later detects whether a file has been modified. |
| **Authentication Log Analyzer** | Parses `auth.log` files, counts failed and successful logins, groups failures by IP, and flags suspicious IPs. |

## Quick Start

**Requirements:** Python 3.10 or later. No packages to install.

```bash
git clone https://github.com/medkerimjbeli-hue/cyberguard-cli.git
cd cyberguard-cli
python main.py
```

## Usage

The main menu lets you pick a tool. After each run you can stay in the same tool or return to the menu.

```text
[1] Password Strength Analyzer
[2] Secure Password Generator
[3] File Integrity Checker
[4] Log Analyzer
[0] Exit
```

### 1. Password Strength Analyzer

Enter a password and get a rating of `WEAK`, `MODERATE`, or `STRONG`.

| Check | Points |
|-------|--------|
| 12+ characters | 2 |
| 8 to 11 characters | 1 |
| Uppercase letter | 1 |
| Lowercase letter | 1 |
| Digit | 1 |
| Special character | 1 |

A score of 6 is `STRONG`, 4 to 5 is `MODERATE`, and anything lower is `WEAK`.

```text
Strength: MODERATE
Score: 5/6

Recommendations:
- Add special characters.
```

### 2. Secure Password Generator

Choose a length between 8 and 64. Passwords draw from letters, digits, and punctuation.

### 3. File Integrity Checker

1. Choose **Register file baseline** to store the file's SHA-256 hash.
2. Later, choose **Check file integrity** to compare the current hash against the saved one.

```text
[SAFE] File has not changed.
[WARNING] File has been modified!
```

Baselines are saved in `integrity_baselines.json`, keyed by the file's absolute path.

### 4. Authentication Log Analyzer

Analyzes `samples/auth.log` and reports:

- Total failed and successful logins
- Failed attempts grouped by IP address, most frequent first
- Suspicious IPs with **3 or more** failed attempts

```text
Failed login attempts: 12
Successful logins: 3

Suspicious IPs (3+ failures):
[WARNING] 192.168.1.50: 5 failed attempts
```

## Project Structure

```text
cyberguard-cli/
├── main.py                  # Entry point, banner, menu, and main loop
├── password_analyzer.py     # Password strength scoring
├── password_generator.py    # Secure random password generation
├── integrity_checker.py     # SHA-256 baselines and verification
├── log_analyzer.py          # Auth log parsing and IP flagging
├── samples/
│   └── auth.log             # Synthetic sample log for testing
├── tests/
│   └── test_security.py     # Unit tests
├── README.md
└── .gitignore
```

> `integrity_baselines.json` is created automatically when you register your first baseline. It is listed in `.gitignore` because it contains local file paths.

## How It Works

- **Hashing:** files are read in 4 KB chunks, so large files don't need to fit in memory.
- **Randomness:** `secrets.choice()` is used instead of `random`, which is not suitable for security purposes.
- **Log parsing:** a regular expression extracts IPv4 addresses from `Failed password` lines, and `collections.Counter` tallies them.
- **Persistence:** baselines are stored as JSON with absolute paths as keys.

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Security Notes

- The password analyzer uses simple heuristics. A high score does not guarantee a password is secure, since it can't detect common or breached passwords.
- The integrity checker only detects changes relative to saved hashes. Protect the baseline file from unauthorized modification, or an attacker could simply update it.
- The log analyzer uses a fixed threshold. Flagged IPs are indicators, not proof of malicious activity.
- Sample authentication logs are synthetic test data.

## Roadmap

- [ ] Check passwords against a list of common or breached passwords
- [ ] Let users choose which character sets the generator uses
- [ ] Verify a whole directory in the integrity checker
- [ ] Accept a custom log file path and configurable threshold
- [ ] Detect successful logins that follow repeated failures from the same IP
- [ ] Export analysis results to a report file

## What I Learned

- Structuring a Python project into modules and functions
- File handling and exception handling
- Cryptographic hashing with SHA-256
- Secure random generation with `secrets`
- JSON-based data persistence
- Log analysis with regular expressions
- Automated testing with `unittest`

## Author

**Mohamed Kerim Jbeli**
Software Engineering student (cybersecurity specialization) at ESGITECH
GitHub: [@medkerimjbeli-hue](https://github.com/medkerimjbeli-hue)

## License

This project is licensed under the MIT License. Add a `LICENSE` file to the repository to make this official.

## Disclaimer

This project is intended for educational and defensive security purposes only.
