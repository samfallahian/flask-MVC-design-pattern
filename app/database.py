from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{Config.DB_USERNAME}:{Config.DB_Password}@{Config.DB_HOST}:3306/{Config.DB_NAME}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
