"""A small interactive password-strength checker."""


def assess_password(password: str) -> tuple[str, list[str]]:
    """Return a strength label and suggestions for improving a password."""
    checks = [
        (len(password) >= 12, "Use at least 12 characters."),
        (any(char.islower() for char in password), "Add a lowercase letter."),
        (any(char.isupper() for char in password), "Add an uppercase letter."),
        (any(char.isdigit() for char in password), "Add a number."),
        (
            any(not char.isalnum() for char in password),
            "Add a symbol, such as !, ?, or #.",
        ),
    ]
    score = sum(passed for passed, _ in checks)
    suggestions = [suggestion for passed, suggestion in checks if not passed]

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    return strength, suggestions


def main() -> None:
    from getpass import getpass

    password = getpass("Enter a password to check (input is hidden): ")
    strength, suggestions = assess_password(password)
    print(f"Password strength: {strength}")
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password meets all five checks.")


if __name__ == "__main__":
    main()
