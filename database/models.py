from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer,
    ForeignKey,
    UniqueConstraint,
    Boolean,
)
from database.database import Base
# Base = declarative_base()



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
    # customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    email = Column(String)
    user_id = Column(Integer, primary_key=True)


# class Customers(Base):
#     __tablename__ = 'customers'
#     __table_args__ = (
#         UniqueConstraint(
#             'customer_name',
#             name='customers_un',
#         ),
#         {'extend_existing': True},
#     )
#     # customer_id = Column(Integer, primary_key=True, autoincrement='ignore_fk')
#     customer_name = Column(String)
#     customer_type = Column(String)
#     is_active = Column(Boolean)
#     created_ts = Column(DateTime)
#     updated_ts = Column(DateTime)