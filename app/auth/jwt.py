from jose import jwt

os.get.SECRET_KEY

ALGORITHM = "HS256"


def create_token(username):

    payload = {

        "sub": username
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)