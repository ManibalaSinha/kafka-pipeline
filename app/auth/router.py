from fastapi import APIRouter, HTTPException
from .schemas import UserCreate, UserLogin, Token
from .password import hash_password, verify_password
from .jwt_handler import create_token

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

# TEMP DB (replace with PostgreSQL later)
fake_users_db = {}

@router.post("/register")
def register(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[user.email] = {
        "email": user.email,
        "password": hash_password(user.password)
    }

    return {"message": "User created successfully"}


@router.post("/login", response_model=Token)
def login(user: UserLogin):
    db_user = fake_users_db.get(user.email)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
