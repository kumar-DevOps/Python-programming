import re

def check_password_strength(password: str) -> str:
    """
    Check the strength of a password and return rating:
    - Weak
    - Medium
    - Strong
    """

    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[!@#$%]", password))

    # Count how many conditions are met
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    # Strength rating
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


# Script to take user input and validate password
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength = check_password_strength(user_password)

    if strength == "Strong":
        print("✅ Strong password! Your password meets all security criteria.")
    elif strength == "Medium":
        print("⚠️ Medium strength password. Consider adding more variety (uppercase, digits, special characters).")
    else:
        print("❌ Weak password. Please ensure it has:")
        print("- At least 8 characters")
        print("- Both uppercase and lowercase letters")
        print("- At least one digit (0-9)")
        print("- At least one special character (!, @, #, $, %)")
