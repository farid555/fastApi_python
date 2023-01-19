from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash password


def hash(password: str):
    return pwd_context.hash(password)


# verify the login possword

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
