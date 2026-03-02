import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive!")
        else:
            print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()