from argon2 import PasswordHasher
from argon2.exceptions import (VerifyMismatchError, VerificationError, InvalidHashError)
from dados.banco import *
import secrets


ph = PasswordHasher()


def hash_password(senha):
    return ph.hash(senha)


def verification_password(senha, hash_senha):
    try:
        return ph.verify(hash_senha, senha)
    except VerifyMismatchError:
        return False
    except (VerificationError, InvalidHashError):
        return False