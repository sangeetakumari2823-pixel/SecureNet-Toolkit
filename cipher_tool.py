# Cipher Tool - Encrypt and Decrypt messages
# Supports Caesar Cipher and Vigenere Cipher
# Part of SecureNet Toolkit

# ---- CAESAR CIPHER ----
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decrypting = shifting backwards

# ---- VIGENERE CIPHER ----
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# --- Run the tool ---
if __name__ == "__main__":
    print("\n=== Cipher Tool ===")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    choice = input("\nChoose cipher (1 or 2): ")

    if choice == "1":
        msg   = input("Enter message: ")
        shift = int(input("Enter shift number (e.g. 3): "))
        enc   = caesar_encrypt(msg, shift)
        dec   = caesar_decrypt(enc, shift)
        print(f"\nEncrypted: {enc}")
        print(f"Decrypted: {dec}")

    elif choice == "2":
        msg = input("Enter message: ")
        key = input("Enter keyword (e.g. 'key'): ")
        enc = vigenere_encrypt(msg, key)
        dec = vigenere_decrypt(enc, key)
        print(f"\nEncrypted: {enc}")
        print(f"Decrypted: {dec}")