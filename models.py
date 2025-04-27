from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)  # <--- Added
    profile_pic = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    xp = Column(Integer, default=0)
    lessons_completed = Column(Integer, default=0)
    streak_count = Column(Integer, default=0)
    last_lesson_date = Column(DateTime)

class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    path_name = Column(String(255))
    path_json = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class UserChapterProgress(Base):
    __tablename__ = "user_chapter_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    learning_path_id = Column(Integer, nullable=False)
    step_number = Column(Integer, nullable=False)
    chapter_number = Column(Integer, nullable=False)
    experience_level = Column(String, nullable=False, default="Beginner")


class UserBadges(Base):
    __tablename__ = "user_badges"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    badge_name = Column(String)
    earned_at = Column(DateTime(timezone=True), server_default=func.now())
