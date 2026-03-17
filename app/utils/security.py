from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    # truncate to avoid bcrypt 72-byte limit
    password = password[:72]
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    password = password[:72]
    return pwd_context.verify(password, hashed_password)