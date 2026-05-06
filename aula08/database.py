from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,
DeclarativeBase
from deotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=false, bind=engine)