import string
import random

def generate_password(length=12, use_special_chars=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    if use_special_chars:
        characters = letters + digits + special_chars
    else:
        characters = letters + digits

    password = [
        random.choice(letters),
        random.choice(digits),
    ]
    if use_special_chars:
        password.append(random.choice(special_chars))
    
    password += random.choices(characters, k=length - len(password))

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    include_special_chars = input("Include special characters (yes/no)? ").lower() == 'yes'
    
    password = generate_password(length=password_length, use_special_chars=include_special_chars)
    print(f"Generated Password: {password}")
