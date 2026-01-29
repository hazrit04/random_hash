import hashlib
import os

def generate_random_hash():
    return hashlib.sha256(os.urandom(32)).hexdigest()[:32]

def find_hash_with_prefix(prefix="00", max_attempts=1000):
    for i in range(max_attempts):
        h = generate_random_hash()
        if h.startswith(prefix):
            print(f"Hash found after {i+1} attempts: {h}")
            return h
    print(f"No hash found with prefix '{prefix}' after {max_attempts} attempts.")
    return None

if __name__ == "__main__":
    find_hash_with_prefix()