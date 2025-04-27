from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Content

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🚀 API to list all lessons
@router.get("/")
def list_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Content).all()
    return lessons
