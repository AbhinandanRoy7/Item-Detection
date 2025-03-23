from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Database Setup
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Define Database Model
class RoomScan(Base):
    __tablename__ = "room_scans"
    room_id = Column(String, primary_key=True)
    before_items = Column(JSON)
    after_items = Column(JSON)

Base.metadata.create_all(engine)

# Function to store scan results
def save_scan(room_id, before_items=None, after_items=None):
    scan = RoomScan(room_id=room_id, before_items=before_items, after_items=after_items)
    session.add(scan)
    session.commit()
