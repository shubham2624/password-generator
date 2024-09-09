import string
import random

def generate_password(length=12, use_special_chars=True):
    
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user preference
    if use_special_chars:
        characters = letters + digits + special_chars
    else:
        characters = letters + digits

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(letters),
        random.choice(digits),
    ]
    if use_special_chars:
        password.append(random.choice(special_chars))
    
    # Fill the remaining length with random choices from the combined set
    password += random.choices(characters, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    include_special_chars = input("Include special characters (yes/no)? ").lower() == 'yes'
    
    password = generate_password(length=password_length, use_special_chars=include_special_chars)
    print(f"Generated Password: {password}")
