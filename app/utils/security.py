from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    sha = hashlib.sha256(password.encode()).digest()  # ✅ FIX
    return pwd_context.hash(sha)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha = hashlib.sha256(plain_password.encode()).digest()  # ✅ FIX
    return pwd_context.verify(sha, hashed_password)