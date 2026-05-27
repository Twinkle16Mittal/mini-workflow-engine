from jose import jwt
import bcrypt

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"


def hash_password(password: str):
    # Truncate to 72 bytes (bcrypt limitation) before hashing
    password = password[:72]
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def verify_password(
    plain_password: str,
    hashed_password: str
):
    # Truncate to 72 bytes (bcrypt limitation) before verifying
    plain_password = plain_password[:72]
    try:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    except (ValueError, TypeError):
        # Handle edge cases with invalid hashes
        return False

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

