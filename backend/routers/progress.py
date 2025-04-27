from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import UserProgress, UserChapterProgress, UserBadges

router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🎯 Badge thresholds
BADGE_THRESHOLDS = {
    100: "Beginner Badge 🥉",
    250: "Intermediate Badge 🥈",
    500: "Advanced Badge 🥇",
    1000: "Expert Badge 🏆"
}

# 🎯 Input Model for Chapter Completion
class ChapterCompletionRequest(BaseModel):
    experience_level: str

# 🎯 Get user progress
@router.get("/{user_id}")
def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    progress = db.query(UserProgress).filter(UserProgress.user_id == user_id).first()
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found for user.")
    return progress

# 🎯 Complete chapter + Add XP + Award Badges
@router.post("/complete_chapter/{user_id}/{path_id}/{step}/{chapter}")
def complete_chapter(user_id: int, path_id: int, step: int, chapter: int, request: ChapterCompletionRequest, db: Session = Depends(get_db)):
    # Check if chapter for that experience already completed
    existing = db.query(UserChapterProgress).filter_by(
        user_id=user_id,
        learning_path_id=path_id,
        step_number=step,
        chapter_number=chapter,
        experience_level=request.experience_level
    ).first()

    if existing:
        return {"message": "Chapter already completed for this experience level."}

    # Save new completed chapter
    new_record = UserChapterProgress(
        user_id=user_id,
        learning_path_id=path_id,
        step_number=step,
        chapter_number=chapter,
        experience_level=request.experience_level
    )
    db.add(new_record)

    # Update XP
    progress = db.query(UserProgress).filter(UserProgress.user_id == user_id).first()
    if not progress:
        progress = UserProgress(user_id=user_id, xp=0)
        db.add(progress)

    progress.xp += 20  # ✅ Add 20 XP per chapter

    # Award badges if thresholds crossed
    earned_badges = db.query(UserBadges).filter(UserBadges.user_id == user_id).all()
    earned_badge_names = [badge.badge_name for badge in earned_badges]

    for xp_needed, badge_name in BADGE_THRESHOLDS.items():
        if progress.xp >= xp_needed and badge_name not in earned_badge_names:
            new_badge = UserBadges(user_id=user_id, badge_name=badge_name)
            db.add(new_badge)

    db.commit()
    db.refresh(progress)

    return {"message": "Chapter completed successfully!", "current_xp": progress.xp}

# 🎯 Get user badges
@router.get("/badges/{user_id}")
def get_user_badges(user_id: int, db: Session = Depends(get_db)):
    badges = db.query(UserBadges).filter(UserBadges.user_id == user_id).all()
    return badges

# 🎯 Get completed chapters for user
@router.get("/completed/{user_id}")
def get_completed_chapters(user_id: int, db: Session = Depends(get_db)):
    completed = db.query(UserChapterProgress).filter(UserChapterProgress.user_id == user_id).all()
    return [
        {
            "path_id": c.learning_path_id,
            "step": c.step_number,
            "chapter": c.chapter_number,
            "experience_level": c.experience_level
        }
        for c in completed
    ]
