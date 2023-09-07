import os
import sys
import colorama
from colorama import Back, Style, Fore
from cryptography.fernet import Fernet

Signature = Fore.LIGHTRED_EX+"""
  ______                             _____  _      
 |  ____|                           |  __ \(_)     
 | |__   _ __   ___ _ __ _   _ _ __ | |  | |_ _ __ 
 |  __| | '_ \ / __| '__| | | | '_ \| |  | | | '__|
 | |____| | | | (__| |  | |_| | |_) | |__| | | |   
 |______|_| |_|\___|_|   \__, | .__/|_____/|_|_|   
                          __/ | |                  
                         |___/|_|    

                    V('0.1.0')		

Programmed By : Mohammed Farhan
Github Page >>>> 'https://github.com/rexerf16'
"""
discl = Fore.LIGHTWHITE_EX + \
    "Read the README.md file. Use responsibly and legally. No liability for misuse.\n"

# Function to generate a random encryption key


def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file


def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Function to decrypt a file


def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)


# Get user input for encryption or decryption
while True:
    print(Signature)
    print(discl)
    choice = input(
        Fore.LIGHTRED_EX+"Choose an option:\n1. Encrypt directory\n2. Decrypt directory\nEnter the option (1/2): ")
    print("")

    if choice == '1':
        key = generate_key()
        key_file_path = 'encryption_key.key'
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)
        print(
            f'Encryption key saved as {key_file_path} in the current directory.')

        current_directory = os.getcwd()
        for filename in os.listdir(current_directory):
            if filename.endswith('.py') or filename == key_file_path:
                continue  # Skip the Python script and the key file itself
            encrypt_file(filename, key)
        print('All files (except Python files and the key file) in the directory have been encrypted.')
        break

    elif choice == '2':
        key_path = input('Enter the path to the decryption key file: ')
        if not os.path.exists(key_path):
            print('Key file not found. Please provide a valid path.')
            continue

        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        current_directory = os.getcwd()
        for filename in os.listdir(current_directory):
            if filename.endswith('.py') or filename == key_path:
                continue  # Skip the Python script and the key file itself
            decrypt_file(filename, key)
        print('All encrypted files in the directory have been decrypted.')
        break

    else:
        print('Invalid choice. Please enter 1 or 2.')

print('Operation completed.')
