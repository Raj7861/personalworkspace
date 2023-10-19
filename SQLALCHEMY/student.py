from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:pgadmin786@localhost:5432/postgres', echo=False)
Session = sessionmaker(bin=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    
Base.metadata.create_all(engine)