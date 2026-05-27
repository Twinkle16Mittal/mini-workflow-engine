from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)


class Workflow(Base):
    __tablename__ = "workflows"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    webhook_path = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))