import random

def generate_password_from_characters(file_path, length=8):
    
    try:
        # Read the characters from the file
        with open(file_path, 'r') as file:
            characters = [line.strip() for line in file if line.strip()]

        if len(characters) == 0:
            raise ValueError("The file does not contain any characters.")

        # Randomly select the desired number of characters
        password = ''.join(random.choices(characters, k=length))
        return password

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_path = 'dictionary.txt'  # File containing characters line by line
    password_length = int(input("Enter the desired length of the password: "))
    password = generate_password_from_characters(file_path, password_length)
    if password:
        print(f"Generated password: {password}")
