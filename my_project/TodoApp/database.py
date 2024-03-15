from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

engine = create_engine(BASE_URL)

SessionLocal = sessionmaker(autocommit=False,bind=engine)

Base = declarative_base()