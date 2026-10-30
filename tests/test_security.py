
import sys
import os
import unittest
import tempfile

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from password_analyzer import analyze_password
from password_generator import generate_password
from integrity_checker import calculate_hash
from log_analyzer import analyze_logs


class TestCyberGuard(unittest.TestCase):

    def test_strong_password(self):
        result = analyze_password("CyberGuard2026!")
        self.assertEqual(result["strength"], "STRONG")

    def test_weak_password(self):
        result = analyze_password("abc")
        self.assertEqual(result["strength"], "WEAK")

    def test_password_generator_length(self):
        password = generate_password(20)
        self.assertEqual(len(password), 20)

    def test_password_generator_characters(self):
        password = generate_password(30)
        self.assertTrue(all(
            char in (
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789"
                "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
            )
            for char in password
        ))

    def test_file_hash_changes(self):
        with tempfile.NamedTemporaryFile(mode="wb", delete=False) as file:
            file.write(b"original content")
            file_path = file.name

        try:
            original_hash = calculate_hash(file_path)

            with open(file_path, "wb") as file:
                file.write(b"modified content")

            modified_hash = calculate_hash(file_path)

            self.assertNotEqual(original_hash, modified_hash)
        finally:
            os.remove(file_path)

    def test_log_analyzer(self):
        sample_logs = (
            "Oct 22 09:10:01 server sshd[1201]: "
            "Failed password for admin from 203.0.113.45 port 50122 ssh2\n"
            "Oct 22 09:10:02 server sshd[1202]: "
            "Failed password for admin from 203.0.113.45 port 50123 ssh2\n"
            "Oct 22 09:10:03 server sshd[1203]: "
            "Failed password for admin from 203.0.113.45 port 50124 ssh2\n"
            "Oct 22 09:10:04 server sshd[1204]: "
            "Accepted password for karim from 192.168.1.10 port 50125 ssh2\n"
        )

        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", delete=False
        ) as file:
            file.write(sample_logs)
            file_path = file.name

        try:
            results = analyze_logs(file_path)

            self.assertEqual(results["failed_attempts"], 3)
            self.assertEqual(results["successful_logins"], 1)
            self.assertEqual(results["suspicious_ips"]["203.0.113.45"], 3)
        finally:
            os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
