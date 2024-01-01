import random
import string
def generate_password(length, use_digits, use_symbols, use_uppercase):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
while length <= 8:
    length = int(input("Not enough characters. Please try again.\n" + "Enter password length: "))
use_digits = input("Include digits? (y/n): ").upper() == 'y'
use_symbols = input("Include symbols? (y/n): ").upper() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").upper() == 'y'

password = generate_password(length, use_digits, use_symbols, use_uppercase)
print("Generated Password:", password)
