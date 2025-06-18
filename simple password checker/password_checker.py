import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        'Too Short': length_error,
        'Missing Digit': digit_error,
        'Missing Uppercase': uppercase_error,
        'Missing Lowercase': lowercase_error,
        'Missing Symbol': symbol_error
    }

    if all(not error for error in errors.values()):
        return "Strong", errors
    elif sum(errors.values()) <= 2:
        return "Moderate", errors
    else:
        return "Weak", errors

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    strength, details = check_strength(password)

    print(f"\nPassword Strength: {strength}")
    print("Issues found:")
    for issue, error in details.items():
        if error:
            print(f"- {issue}")

if __name__ == "__main__":
    main()
