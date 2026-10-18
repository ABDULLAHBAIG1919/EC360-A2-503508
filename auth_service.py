import hashlib
import secrets
def hash_password(password):
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    ).hex()
    return f"{salt}${digest}"
def register_user(username, password, users):
    if not username or not password:
        raise ValueError("Username and password are required")
    if username in users:
        raise ValueError("Username already exists")
    users[username] = hash_password(password)
    return {"username": username, "registered": True}
