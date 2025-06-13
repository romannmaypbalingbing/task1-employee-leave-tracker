import json
import os
from cryptography.fernet import Fernet
from django.conf import settings

#keygen
def generate_key():
    """Generate a new encryption key."""
    key = Fernet.generate_key()
    print("decode")
    print(key.decode())
    return key

#load the key from a file or environment variable
cipher_key = Fernet(settings.ENCRYPTION_KEY.encode())

def encrypt_data(data: str) -> str:
    """Encrypt the given data."""
    encypted_data = cipher_key.encrypt(data.encode())
    return encypted_data.decode()

def decrypt_data(encrypted_data: str) -> str:
    """Decrypt the given encrypted data."""
    decrypted_data = cipher_key.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

def encrypt_leave_request(leave_request_data: dict) -> str:
    """Encrypt the leave request data."""
    return encrypt_data(json.dumps(leave_request_data))

def decrypt_leave_request(encrypted_leave_request: str) -> dict:
    """Decrypt the leave request data."""
    decrypted_data = decrypt_data(encrypted_leave_request)
    return json.loads(decrypted_data)