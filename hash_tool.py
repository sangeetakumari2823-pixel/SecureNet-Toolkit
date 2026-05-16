# Hash Tool - Generate and verify MD5 / SHA256 hashes
# Part of SecureNet Toolkit

import hashlib

def hash_text(text):
    """Generate MD5 and SHA256 hashes for any text/password"""
    md5    = hashlib.md5(text.encode()).hexdigest()
    sha256 = hashlib.sha256(text.encode()).hexdigest()
    sha512 = hashlib.sha512(text.encode()).hexdigest()

    print(f"\n{'='*60}")
    print(f"  Input Text : {text}")
    print(f"{'='*60}")
    print(f"  MD5    : {md5}")
    print(f"  SHA256 : {sha256}")
    print(f"  SHA512 : {sha512}")
    print(f"{'='*60}\n")

    return md5, sha256, sha512

def verify_hash(text, known_hash):
    """Check if a text matches a known hash"""
    print(f"\n  Checking: '{text}'")

    # Try matching against MD5, SHA256, SHA512
    if hashlib.md5(text.encode()).hexdigest() == known_hash:
        print(f"  ✅ MATCH found! (MD5)")
        return True
    elif hashlib.sha256(text.encode()).hexdigest() == known_hash:
        print(f"  ✅ MATCH found! (SHA256)")
        return True
    elif hashlib.sha512(text.encode()).hexdigest() == known_hash:
        print(f"  ✅ MATCH found! (SHA512)")
        return True
    else:
        print(f"  ❌ No match.")
        return False

def hash_wordlist(wordlist, known_hash):
    """Try a list of words against a hash (mini brute-force demo)"""
    print(f"\n  Running wordlist attack on hash...")
    print(f"  Hash: {known_hash}\n")

    for word in wordlist:
        word = word.strip()
        if (hashlib.md5(word.encode()).hexdigest() == known_hash or
            hashlib.sha256(word.encode()).hexdigest() == known_hash):
            print(f"  ✅ CRACKED! The word is: '{word}'")
            return word

    print(f"  ❌ Hash not found in wordlist.")
    return None

if __name__ == "__main__":
    print("\n=== Hash Tool ===")
    print("  1. Generate hash")
    print("  2. Verify a hash")
    print("  3. Wordlist attack (demo)")
    choice = input("\n  Choose (1/2/3): ")

    if choice == "1":
        text = input("  Enter text to hash: ")
        hash_text(text)

    elif choice == "2":
        text  = input("  Enter text: ")
        known = input("  Enter known hash: ")
        verify_hash(text, known)

    elif choice == "3":
        known = input("  Enter hash to crack: ")
        print("  Enter words one per line (type 'done' to finish):")
        words = []
        while True:
            w = input("  > ")
            if w.lower() == "done":
                break
            words.append(w)
        hash_wordlist(words, known)