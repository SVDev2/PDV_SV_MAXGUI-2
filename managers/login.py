from argon2 import PasswordHasher
from argon2.exceptions import (VerifyMismatchError, VerificationError, InvalidHashError)


ph = PasswordHasher()


def hash_password(senha):
    return ph.hash(senha)


def verification_password(senha, hash_senha):
    if not isinstance(senha, str) or not isinstance(hash_senha, str):
        return False
    if not senha or not hash_senha:
        return False
        
    try:
        return ph.verify(hash_senha, senha)
    except VerifyMismatchError:
        return False
    except (VerificationError, InvalidHashError):
        return False


def needs_rehash(hash_senha):
    try:
        return ph.check_needs_rehash(hash_senha)
    except (VerificationError, InvalidHashError):
        return False