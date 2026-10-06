import hashlib
import secrets
import getpass


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    )


def create_user(password):
    salt = secrets.token_bytes(16)
    password_hash = hash_password(password, salt)

    return {
        "salt": salt,
        "password_hash": password_hash
    }


def verify_password(password, user):
    password_hash = hash_password(password, user["salt"])

    return secrets.compare_digest(
        password_hash,
        user["password_hash"]
    )


# Demo user
demo_user = create_user("StrongPassword@123")


username = input("Enter username: ").strip()

if not username:
    print("Invalid username.")
else:
    password = getpass.getpass("Enter password: ")

    if not password:
        print("Password cannot be empty.")
    elif verify_password(password, demo_user):
        print("Login successful!")
    else:
        print("Invalid username or password.")