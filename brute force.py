import itertools
import string

def brute_force_attack(password):
    # Define the character set
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    attempts = 0

    print("Starting brute force attack...")

    # Iterate over possible password lengths
    for length in range(1, len(password) + 1):
        # Generate all possible combinations of the current length
        for combination in itertools.product(characters, repeat=length):
            # Increment attempt count
            attempts += 1
            guess = ''.join(combination)

            # Check if the guess matches the password
            if guess == password:
                print(f"Password found: {guess}")
                print(f"Total attempts: {attempts}")
                return guess

    print("Password not found.")
    return None

if __name__ == "__main__":
    user_password = input("Enter the password to crack: ").strip()

    if user_password == "":
        print("Password cannot be empty.")
    else:
        brute_force_attack(user_password)
