
def analyze_password(password):
    score = 0
    weaknesses = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        weaknesses.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        weaknesses.append("Add uppercase letters.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        weaknesses.append("Add lowercase letters.")

    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        weaknesses.append("Add numbers.")

    # Check special characters
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        weaknesses.append("Add special characters.")

    # Determine strength
    if score >= 6:
        strength = "STRONG"
    elif score >= 4:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    return {
        "score": score,
        "strength": strength,
        "weaknesses": weaknesses
    }


def run_analyzer():
    print("\n=== PASSWORD STRENGTH ANALYZER ===")

    password = input("Enter a password to analyze: ")

    result = analyze_password(password)

    print(f"\nStrength: {result['strength']}")
    print(f"Score: {result['score']}/6")

    if result["weaknesses"]:
        print("\nRecommendations:")
        for weakness in result["weaknesses"]:
            print(f"- {weakness}")
    else:
        print("\nAll basic checks passed!")
