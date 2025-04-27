from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random
from database import SessionLocal
from models import UserReward, Gift, BigMotivator

router = APIRouter(
    prefix="/rewards",
    tags=["Rewards"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🚀 1. Claim a small gift
@router.post("/claim_gift/{user_id}")
def claim_gift(user_id: int, db: Session = Depends(get_db)):
    # Pick random gift from catalog
    gift = db.query(Gift).order_by(func.random()).first()
    if not gift:
        raise HTTPException(status_code=404, detail="No gifts available")

    user_reward = UserReward(
        user_id=user_id,
        reward_type=gift.gift_type,
        reward_name=gift.gift_name
    )
    db.add(user_reward)
    db.commit()
    db.refresh(user_reward)

    return {"message": "Gift claimed!", "reward": gift.gift_name}

# 🚀 2. Claim a BIG motivator (after getting 5+ gifts)
@router.post("/claim_big_motivator/{user_id}")
def claim_big_motivator(user_id: int, db: Session = Depends(get_db)):
    user_gifts = db.query(UserReward).filter(UserReward.user_id == user_id).count()
    if user_gifts < 5:
        raise HTTPException(status_code=400, detail="Need 5+ small gifts to unlock big motivator.")

    big_motivator = db.query(BigMotivator).order_by(func.random()).first()
    if not big_motivator:
        raise HTTPException(status_code=404, detail="No big motivators available")

    user_reward = UserReward(
        user_id=user_id,
        reward_type="big_motivator",
        reward_name=big_motivator.motivator_name
    )
    db.add(user_reward)
    db.commit()
    db.refresh(user_reward)

    return {"message": "BIG motivator unlocked!", "motivator": big_motivator.motivator_name}

# 🚀 3. View user's collected rewards
@router.get("/my_rewards/{user_id}")
def my_rewards(user_id: int, db: Session = Depends(get_db)):
    rewards = db.query(UserReward).filter(UserReward.user_id == user_id).all()
    return rewards
