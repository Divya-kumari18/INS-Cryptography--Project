
import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag


def encrypt_message(message, key):
    # Generate a unique 12-byte nonce for this encryption
    nonce = os.urandom(12)

    # Create the AES-GCM cipher
    aes = AESGCM(key)

    # Encrypt the message; output includes the authentication tag
    ciphertext = aes.encrypt(nonce, message.encode("utf-8"), None)

    return nonce, ciphertext


def decrypt_message(nonce, ciphertext, key):
    # Create the AES-GCM cipher with the same key
    aes = AESGCM(key)

    # Decrypt and verify the authentication tag
    plaintext = aes.decrypt(nonce, ciphertext, None)

    return plaintext.decode("utf-8")


def main():
    print("=" * 50)
    print(" AES-GCM CRYPTOGRAPHIC ALGORITHM")
    print("=" * 50)

    # Generate a fresh 256-bit secret key
    key = AESGCM.generate_key(bit_length=256)

    print("\nA new 256-bit key has been generated.")

    message = input("\nEnter the message to encrypt: ")

    # Encryption
    nonce, ciphertext = encrypt_message(message, key)

    print("\n--- ENCRYPTION ---")
    print("Original message :", message)
    print("Nonce (Base64)   :", base64.b64encode(nonce).decode())
    print("Ciphertext (Base64):",
          base64.b64encode(ciphertext).decode())

    # Decryption
    recovered = decrypt_message(nonce, ciphertext, key)

    print("\n--- DECRYPTION ---")
    print("Recovered message:", recovered)
    print("Message recovered successfully:",
          recovered == message)

    # Demonstrate tampering detection
    print("\n--- TAMPERING TEST ---")

    tampered = bytearray(ciphertext)
    tampered[0] ^= 1

    try:
        decrypt_message(nonce, bytes(tampered), key)
        print("Tampering was not detected.")
    except InvalidTag:
        print("Tampering detected! Authentication failed.")

    # Demonstrate wrong-key detection
    print("\n--- WRONG-KEY TEST ---")

    wrong_key = AESGCM.generate_key(bit_length=256)

    try:
        decrypt_message(nonce, ciphertext, wrong_key)
        print("Unexpected result: decryption succeeded.")
    except InvalidTag:
        print("Wrong key rejected! Authentication failed.")

    print("\nProject demonstration completed.")


if __name__ == "__main__":
    main()
