import hashlib
import itertools
import string
import sys
from time import time

CHARSET = string.ascii_letters + string.digits
MAX_LENGTH = 15
DISPLAY_EVERY = 100000

def hash_match(plain, target_hash, hash_type):
    return hashlib.new(hash_type, plain.encode()).hexdigest() == target_hash

def brute_force(target_hash, hash_type):
    attempts = 0
    start = time()

    print(f"Starting brute-force (max length: {MAX_LENGTH})")
    print(f"Charset size: {len(CHARSET)}\n")

    try:
        for length in range(1, MAX_LENGTH + 1):
            print(f"Trying length: {length}")
            for combo in itertools.product(CHARSET, repeat=length):
                guess = ''.join(combo)
                attempts += 1

                if hash_match(guess, target_hash, hash_type):
                    print(f"\nMatch: {guess}")
                    print(f"Attempts: {attempts}")
                    print(f"Time: {round(time() - start, 2)}s")
                    return

                if attempts % DISPLAY_EVERY == 0:
                    print(f"{attempts} guesses tried")

    except KeyboardInterrupt:
        print("\nStopped by user.")
        sys.exit()

    print(f"\nNo match. Attempts: {attempts} | Time: {round(time() - start, 2)}s")

def main():
    hash_input = input("Hash: ").strip()
    hash_type = input("Type (md5, sha1, sha256): ").strip().lower()

    if hash_type not in hashlib.algorithms_available:
        print("Invalid type.")
        return

    brute_force(hash_input, hash_type)

if __name__ == "__main__":
    main()
