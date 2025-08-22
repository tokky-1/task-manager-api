from sqlalchemy import Column, Integer, String,Text
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Task(base):
    __tablename__ = "Tasks"
    id = Column(Integer,primary_key =True,autoincrement=True,index=True,nullable=False)
    title = Column(String,nullable=False)
    description = Column(Text)
