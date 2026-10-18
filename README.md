# Password Strength Checker

A small interactive password-strength checker written in Python. It uses only
the Python standard library and does not save or transmit the password.

## Requirements

- Python 3.9 or newer

## Usage

Run the program from a terminal:

```bash
python password_checker.py
```

Enter a password when prompted. Input is hidden while typing. The checker
reports a **Weak**, **Moderate**, or **Strong** rating and suggests any missing
checks: at least 12 characters, lowercase and uppercase letters, a number, and
a symbol.

This is a simple educational checker, not a guarantee that a password is
secure. Prefer a unique password generated and stored by a trusted password
manager.
