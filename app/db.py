from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.config import get_settings


engine = create_engine(get_settings().DB_URL)
Session = sessionmaker(bind=engine, autoflush=False)

