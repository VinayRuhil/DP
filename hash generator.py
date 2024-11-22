import rsa

def generateHash(input):
    msgInBinary = input.encode('utf-8')
    return rsa.compute_hash(msgInBinary, 'SHA-256')

def main():
    while True:
        print("\nMenu:")
        print("1. Generate Hash")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_input = input('Enter the Password : ')
            output = generateHash(user_input)
            print('Generated Hash: ', output)
            print('Generated Hash in Hexa: ', output.hex())
            print('Length of Hex  : ',len(output.hex()))
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
