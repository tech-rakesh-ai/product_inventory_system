from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import setting

# Create the SQLAlchemy engine
engine = create_engine(setting.DATABASE_URL, echo=False)

# Create the session maker object
SessionLocal = sessionmaker(bind=engine, autocommit=setting.AUTOCOMMIT, autoflush=setting.AUTOFLUSH)

# Define the declarative base
Base = declarative_base()


def get_db():
    """
    This method is used to create the database instance.
    :return: database instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
