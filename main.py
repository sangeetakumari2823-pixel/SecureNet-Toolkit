# SecureNet Toolkit - Main Menu
# Run this file to access all tools

import port_scanner
import cipher_tool
import password_checker
import hash_tool

def main_menu():
    while True:
        print("\n" + "="*50)
        print("       🔐 SECURENET TOOLKIT")
        print("="*50)
        print("  [1] Port Scanner")
        print("  [2] Cipher Tool (Encrypt / Decrypt)")
        print("  [3] Password Strength Checker")
        print("  [4] Hash Generator & Verifier")
        print("  [0] Exit")

        print("="*50)

        choice = input("\n  Choose a tool (0-3): ")

        if choice == "1":
            print("\n--- PORT SCANNER ---")
            target = input("Enter target IP or domain (e.g. 127.0.0.1): ")
            start  = int(input("Start port (e.g. 1): "))
            end    = int(input("End port (e.g. 100): "))
            port_scanner.scan_ports(target, start, end)

        elif choice == "2":
            print("\n--- CIPHER TOOL ---")
            cipher_tool_menu()

        elif choice == "3":
            print("\n--- PASSWORD CHECKER ---")
            pwd = input("Enter a password to check: ")
            password_checker.check_password(pwd)

        elif choice == "4":
            print("\n--- HASH TOOL ---")
            print("  1. Generate hash")
            print("  2. Verify a hash")
            print("  3. Wordlist attack (demo)")
            c = input("\n  Choose (1/2/3): ")
            if c == "1":
                text = input("  Enter text to hash: ")
                hash_tool.hash_text(text)
            elif c == "2":
                text  = input("  Enter text: ")
                known = input("  Enter known hash: ")
                hash_tool.verify_hash(text, known)
            elif c == "3":
                known = input("  Enter hash to crack: ")
                print("  Enter words one per line (type 'done' to finish):")
                words = []
                while True:
                    w = input("  > ")
                    if w.lower() == "done":
                        break
                    words.append(w)
                hash_tool.hash_wordlist(words, known)

        elif choice == "0":
            print("\n  Goodbye! Stay secure. 🔒\n")
            break

        else:
            print("\n  ❌ Invalid choice. Please enter 0-3.")

def cipher_tool_menu():
    print("  1. Caesar Cipher")
    print("  2. Vigenere Cipher")
    choice = input("\n  Choose cipher (1 or 2): ")

    if choice == "1":
        msg   = input("Enter message: ")
        shift = int(input("Enter shift number (e.g. 3): "))
        enc   = cipher_tool.caesar_encrypt(msg, shift)
        dec   = cipher_tool.caesar_decrypt(enc, shift)
        print(f"\nEncrypted: {enc}")
        print(f"Decrypted: {dec}")

    elif choice == "2":
        msg = input("Enter message: ")
        key = input("Enter keyword (e.g. 'key'): ")
        enc = cipher_tool.vigenere_encrypt(msg, key)
        dec = cipher_tool.vigenere_decrypt(enc, key)
        print(f"\nEncrypted: {enc}")
        print(f"Decrypted: {dec}")

if __name__ == "__main__":
    main_menu()