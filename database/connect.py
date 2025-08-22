from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv(override=True)

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL,echo=True)
sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind = engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close() 
