from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🚀 YOUR Railway Database URL
DATABASE_URL = "postgresql://postgres:WAELVvnSdqoBmdlqftBDvWvwKIpLFJOs@centerbeam.proxy.rlwy.net:27298/railway"

# Set up the connection
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
