from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///sales_system.db')
Session = sessionmaker(bind=engine)

class GPSLog(Base):
    __tablename__ = 'gps_tracking'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    timestamp = Column(DateTime)

def init_db():
    Base.metadata.create_all(engine)
