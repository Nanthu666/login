from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import Session
from . import models
from database import schemas

username= "postgres"
password= "123456"
ip_address= "localhost"
port= 5432
database= "connector"

db_string = f"postgresql://{username}:{password}@{ip_address}:{port}/{database}"




engine = create_engine(db_string, pool_size=20, max_overflow=0)

Base = declarative_base()
session = scoped_session(sessionmaker(bind=engine))


def create_user(db: Session, user_data: schemas.UserCreate):
    db_user = models.Users(
        email=user_data.email,
        username=user_data.username,
        password=password,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.autoflush = False

    try:
        yield session
    except:
        session.close()
    finally:
        session.close()
