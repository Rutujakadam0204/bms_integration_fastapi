from databases import Base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    password = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # display = relationship("Displaypermission", back_populates='owner')

class Displaypermission(Base):
    __tablename__ = 'display'
    id = Column(Integer, primary_key=True, index=True)
    company = Column(Boolean, default=False)
    customer_details = Column(Boolean, default=False)
    invoice = Column(Boolean, default=False)
    payment_paid = Column(Boolean, default=False)
    product = Column(Boolean, default=False)

    owner = relationship("User", back_populates='display')