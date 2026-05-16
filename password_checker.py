# Password Strength Checker
# Part of SecureNet Toolkit

import re

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("  ✗ Too short - use at least 8 characters")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("  ✗ Add at least one UPPERCASE letter")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("  ✗ Add at least one lowercase letter")

    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("  ✗ Add at least one number")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 2
    else:
        feedback.append("  ✗ Add a special character (!@#$% etc.)")

    # Common passwords check
    common = ["password", "123456", "qwerty", "abc123", "letmein"]
    if password.lower() in common:
        score = 0
        feedback.append("  ✗ This is a very common password!")

    # Score result
    print(f"\n  Password: {password}")
    print(f"  Score: {score}/7")

    if score >= 6:
        print("  Strength: 🟢 STRONG")
    elif score >= 4:
        print("  Strength: 🟡 MODERATE")
    else:
        print("  Strength: 🔴 WEAK")

    if feedback:
        print("\n  Suggestions:")
        for tip in feedback:
            print(tip)
    else:
        print("  ✓ Great password!")

# --- Run the checker ---
if __name__ == "__main__":
    print("\n=== Password Strength Checker ===")
    pwd = input("Enter a password to check: ")
    check_password(pwd)