
# 🛡️ CyberGuard CLI

A Python-based defensive cybersecurity toolkit built to practice
security fundamentals through practical command-line tools.

## Features

### 1. Password Strength Analyzer
- Evaluates password length and character variety.
- Provides a strength rating and improvement recommendations.

### 2. Secure Password Generator
- Generates random passwords using Python's `secrets` module.
- Supports configurable lengths from 8 to 64 characters.

### 3. File Integrity Checker
- Calculates SHA-256 hashes.
- Saves file hash baselines.
- Detects changes by comparing current hashes with saved baselines.

### 4. Authentication Log Analyzer
- Counts failed and successful login attempts.
- Groups failed attempts by IP address.
- Flags IP addresses with three or more failed attempts.

## Technologies

- Python 3
- hashlib
- secrets
- collections
- regular expressions
- JSON
- unittest

## Project Structure

```text
cyberguard-cli/
├── main.py
├── password_analyzer.py
├── password_generator.py
├── integrity_checker.py
├── log_analyzer.py
├── integrity_baselines.json
├── samples/
│   └── auth.log
├── tests/
│   └── test_security.py
├── README.md
└── .gitignore
```

Note: `integrity_baselines.json` is created when you register
your first file baseline.

## Requirements

- Python 3.10 or later recommended
- No third-party packages required

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd cyberguard-cli
```

Run the application:

```bash
python main.py
```

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Security Notes

- The password analyzer uses simple heuristic checks and does not
  guarantee that a password is secure.
- The integrity checker detects changes relative to saved hashes.
  Protect your baseline data against unauthorized modification.
- The log analyzer uses a simple threshold, not proof of malicious
  activity.
- Sample authentication logs are synthetic test data.

## Learning Objectives

- Python modules and functions
- File handling and exception handling
- Cryptographic hashing with SHA-256
- Secure random generation
- JSON-based data persistence
- Log analysis and automated testing

## Disclaimer

This project is intended for educational and defensive security
purposes.
