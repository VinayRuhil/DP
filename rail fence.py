def encrypt_rail_fence(text, key):
 
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0

    for char in text:
        rail[row][col] = char
        col += 1
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    encrypted_text = ''.join([''.join(row) for row in rail])
    return encrypted_text


def decrypt_rail_fence(text, key):
    rail = [['' for _ in range(len(text))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    for _ in text:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] == '*' and index < len(text):
                rail[i][j] = text[index]
                index += 1

    decrypted_text = []
    row, col = 0, 0
    for _ in range(len(text)):
        decrypted_text.append(rail[row][col])
        col += 1
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        row += 1 if direction_down else -1

    return ''.join(decrypted_text)


def main_menu():
    while True:
        print("\nRail Fence Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter your message to encrypt: ")
            key = int(input("Enter the number of rails (key): "))
            encrypted_message = encrypt_rail_fence(message, key)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter your encrypted message to decrypt: ")
            key = int(input("Enter the number of rails (key): "))
            decrypted_message = decrypt_rail_fence(message, key)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
