import random
import string

def password_generator():
    print("----- PASSWORD GENERATOR -----\n")

    length = int(input("Enter password length: "))

    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    characters = string.ascii_lowercase

    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("❌ No character set selected!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    print("\n----- GENERATED PASSWORD -----")
    print(password)

password_generator()
