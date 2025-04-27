from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from models import User

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

class SignupRequest(BaseModel):
    email: str
    username: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.email == request.email) | (User.username == request.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")

    new_user = User(
        email=request.email,
        username=request.username,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully.", "user_id": new_user.id}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    return {"message": "Login successful", "user_id": user.id}
