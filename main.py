import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, lowercase=1, uppercase=1):
    all_characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ""

        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r"\d"),
            (special_chars, fr"[{string.punctuation}]"),
            (lowercase, r"[a-z]"),
            (uppercase, r"[A-Z]")
        ]

        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
            break

    return password


def main():
    new_password = generate_password(8)
    print(new_password)


if __name__ == "__main__":
    main()