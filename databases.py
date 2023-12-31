"""The create_engine function is used to create an engine,
    which is the starting point for working with a database using SQLAlchemy."""
from sqlalchemy import create_engine

"""The sessionmaker is used to create session objects that interact with the database."""
from sqlalchemy.orm import sessionmaker

"""The declarative_base is used to create base classes for declarative SQLAlchemy models."""
from sqlalchemy.ext.declarative import declarative_base

# DB_URL = 'mysql://root:Temp123@127.0.0.1:3306/rk_company'
DB_URL = 'postgresql://rk_company_96oj_user:sKQmyXTTTIYZZyUgISAdW5D8qfB8xQti@dpg-cj90c6qvvtos73ftj7a0-a/rk_company_96oj'
engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()