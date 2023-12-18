from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import (
    Column,
    String,
    Integer,
    UniqueConstraint,

)
from database.database import Base



class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        UniqueConstraint(
            'username',
            'email',
            name='users_un',
        ),
        {'extend_existing': True},
    )
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    email = Column(String)
    user_id = Column(Integer, primary_key=True)

