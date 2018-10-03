from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'
    test_id = Column('test_id', Integer, primary_key=True)
