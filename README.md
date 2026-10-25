# AES-256-GCM Cryptographic Algorithm Using Python

## Project Overview
This project demonstrates AES-256-GCM authenticated encryption and decryption using Python. It shows how messages can be encrypted securely and how unauthorized modifications can be detected.

## Objectives
- Implement AES-256-GCM encryption and decryption.
- Generate a random 256-bit secret key.
- Generate a unique 12-byte nonce for encryption.
- Verify successful message recovery.
- Detect ciphertext tampering.
- Reject decryption attempts using an incorrect key.

## Technologies Used
- Python
- `cryptography` library
- Visual Studio Code

## Installation

Install the required dependency:

```bash
python -m pip install cryptography
```

## How to Run

```bash
python aes_gcm_project.py
```

Enter a message when prompted.

## Demonstration
The program demonstrates:
1. Encryption of the original message.
2. Decryption and successful recovery.
3. Authentication failure after ciphertext tampering.
4. Authentication failure when using an incorrect key.

## Academic Activity
Information and Network Security (INS) — JSS Academy of Technical Education.

## Security Note
This is an educational demonstration. The secret key is generated in memory for each execution and is not saved. Never reuse a nonce with the same AES-GCM key. Base64 is an encoding format, not encryption.
