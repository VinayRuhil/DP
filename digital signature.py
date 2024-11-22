import rsa

def generate_keys():
    """Generate RSA key pair and save them to files."""
    public_key, private_key = rsa.newkeys(2048)

    with open('public_key_file.pem', 'wb') as puk:
        puk.write(public_key.save_pkcs1('PEM'))

   
    with open('private_key_file.pem', 'wb') as prk:
        prk.write(private_key.save_pkcs1('PEM'))

    print("Keys generated and saved to 'public_key_file.pem' and 'private_key_file.pem'.")

def sign_pdf(pdf_path):
    """Sign a PDF file and save the signature."""
    try:
       
        with open(pdf_path, 'rb') as f:
            pdf = f.read()

       
        with open('private_key_file.pem', 'rb') as pr:
            private_key = rsa.PrivateKey.load_pkcs1(pr.read())

        
        signature = rsa.sign(pdf, private_key, 'SHA-256')

        
        with open('signature_file', 'wb') as sf:
            sf.write(signature)

        print(f"PDF signed. Signature saved to 'signature_file'.")
    except FileNotFoundError:
        print("Error: File not found. Please ensure the PDF and private key files exist.")

def verify_signature(pdf_path):
    """Verify the signature of a PDF file."""
    try:
       
        with open(pdf_path, 'rb') as f:
            pdf = f.read()

       
        with open('public_key_file.pem', 'rb') as puk:
            public_key = rsa.PublicKey.load_pkcs1(puk.read())

        
        with open('signature_file', 'rb') as sf:
            signature = sf.read()

        
        rsa.verify(pdf, signature, public_key)
        print("Signature is valid. The PDF is authentic.")
    except rsa.VerificationError:
        print("Signature verification failed. The PDF may have been tampered with.")
    except FileNotFoundError:
        print("Error: Required file not found. Please ensure the PDF, public key, and signature files exist.")

def main():
    """Main function to provide a menu for the user."""
    while True:
        print("\n--- Digital Signature Program ---")
        print("1. Generate Keys")
        print("2. Sign a PDF")
        print("3. Verify a PDF Signature")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            generate_keys()
        elif choice == '2':
            pdf_path = input("Enter the path to the PDF file: ")
            sign_pdf(pdf_path)
        elif choice == '3':
            pdf_path = input("Enter the path to the PDF file: ")
            verify_signature(pdf_path)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
