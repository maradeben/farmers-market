""" utilities for models """
import bcrypt

def hash_password(password: str) -> bytes:
    """ encrypt password """
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    """ verify password is as hashed """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# test password hasing
# correct = 'abcd'
# incorrect = 'efgh'
# hashed = hash_password(correct)
# print(type(hashed))
# print(verify_password(correct, hashed))
# print(verify_password(incorrect, hashed))