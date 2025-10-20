import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


import hashlib

code = "metai-key"
# Generate a 32-byte key for AES-256 using SHA-256
encryption_key = hashlib.sha256(code.encode()).digest()


def encrypt_data(plaintext: str) -> str:
    """Encrypt a string using AES-256-CBC."""
    iv = os.urandom(16)

    # Pad and encrypt
    padder = padding.PKCS7(128).padder()
    padded = padder.update(plaintext.encode()) + padder.finalize()

    cipher = Cipher(
        algorithms.AES(encryption_key), modes.CBC(iv), backend=default_backend()
    )
    encrypted = cipher.encryptor().update(padded) + cipher.encryptor().finalize()

    # Return base64(iv + encrypted)
    return base64.b64encode(iv + encrypted).decode()
