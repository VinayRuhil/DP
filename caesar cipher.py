def caesar_cipher(text, shift, mode='encrypt'):

    result = ''
    if mode == 'decrypt':
        shift = -shift  

    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  

    return result


def main_menu():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice : ")

        if choice == '1':
            message = input("Enter your message to encrypt: ")
            shift_value = int(input("Enter shift value (integer): "))
            encrypted_message = caesar_cipher(message, shift_value, mode='encrypt')
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter your message to decrypt: ")
            shift_value = int(input("Enter shift value (integer): "))
            decrypted_message = caesar_cipher(message, shift_value, mode='decrypt')
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
