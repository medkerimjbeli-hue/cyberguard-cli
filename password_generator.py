
import secrets
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def run_generator():
    print("\n=== SECURE PASSWORD GENERATOR ===")

    try:
        length = int(input("Choose password length (8-64): "))

        if length < 8 or length > 64:
            print("Error: Choose a length between 8 and 64.")
            return

        password = generate_password(length)

        print("\nGenerated password:")
        print(password)

    except ValueError:
        print("Error: Please enter a valid number.")
