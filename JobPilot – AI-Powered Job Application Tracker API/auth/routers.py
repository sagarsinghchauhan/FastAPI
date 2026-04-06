from fastapi import APIRouter, Depends, HTTPException
from auth.schema import UserCreate, UserResponse
from sqlalchemy.orm import Session
from Database.database import get_db
from auth.model import User
from auth.hashing import hash_password, verify_password
from auth.jwt_handler import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Wrong password")

    token = create_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
