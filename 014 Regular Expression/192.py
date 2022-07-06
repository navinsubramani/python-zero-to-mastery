import re

email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$")
pwd_pattern = re.compile(r"[a-zA-Z0-9@$%#]{7,}[0-9]$")

while True:
    inp = input("Enter your email: ")
    result = email_pattern.match(inp)

    if result is None:
        continue

    else:
        print("Email is Valid...")

        while True:
            inp = input("Enter the password: ")
            result = pwd_pattern.match(inp)

            if result is None:
                continue

            else:
                print("Password is correct...")
                break

        break
