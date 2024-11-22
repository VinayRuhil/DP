
import requests
import hashlib

# Read the file containing usernames and passwords
with open('passwords.txt', 'r') as f:
    for line in f:
      
        username, password = line.strip().split(',')

       
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

       
        if response.status_code == 200:
            
            hashes = [line.split(':') for line in response.text.splitlines()]
            if any(password_hash[5:] == h for h, _ in hashes):
                print(f"Password for user {username} has been leaked!")
            else:
                print(f"Password for user {username} is safe.")
        else:
            print(f"Could not check password for user {username}.")
