import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    char_set = ""
    
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_special:
        char_set += string.punctuation

    if len(char_set) == 0:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated Password: {password}\n")
        except ValueError as e:
            print(e)
            continue

        another = input("Generate another password? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using the Password Generator! Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
