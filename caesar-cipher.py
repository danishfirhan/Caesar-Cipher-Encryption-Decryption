def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    # Iterate through each character in the text
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    
    return result

def main():
    while True:
        choice = input("Choose an option (Encrypt/Decrypt/Quit): ").lower()

        if choice == 'encrypt':
            text = input("Enter text to encrypt: ")
            shift = 3  # Fixed key for Caesar Cipher
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted text:", encrypted_text)

        elif choice == 'decrypt':
            text = input("Enter text to decrypt: ")
            shift = 3  # Fixed key for Caesar Cipher
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            print("Decrypted text:", decrypted_text)
        
        elif choice == 'quit':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please enter 'Encrypt', 'Decrypt', or 'Quit'.")

if __name__ == "__main__":
    main()
