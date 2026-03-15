from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class AIModel(Base):
    __tablename__ = "ai_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    version = Column(String)
    status = Column(String, default="online")
    endpoint_url = Column(String)
    latency = Column(Float, default=0.0)
    cpu_load = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner = Column(String)
