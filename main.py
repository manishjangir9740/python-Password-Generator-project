import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_password

def main():
    print("Creates strong, secure passwords.")
    

    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                raise ValueError("Count must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer for count.")

    passwords = []
    for idx in range(1, num_passwords + 1):
        while True:
            try:
                password_length = int(input(f"Enter the length for Password {idx}: "))
                if password_length <= 0:
                    raise ValueError("Length must be a positive integer.")
                passwords.append(generate_password(password_length))
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a positive integer for length.")

    print("\nGenerated Password:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
