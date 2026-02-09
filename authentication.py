from jose import jwt
from passlib.context import CryptContext
import secrets

SECRET_KEY = secrets.token_hex(16)
print(SECRET_KEY)
ALGORITHM = "HS256"


jwt_token = CryptContext(schemes=["bcrypt"])


def hash_password(password: str):
    return jwt_token.hash(password)

def verify_password(password, hashed_password):
    return jwt_token.verify(password, hashed_password)

def access_token(data: dict):
    jwt_encode = data.copy()
    return jwt.encode(jwt_encode, SECRET_KEY,algorithm=ALGORITHM)