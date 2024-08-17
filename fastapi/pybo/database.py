from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


SQLALCHEMY_DATABASE_URL = 'sqlite:./pybo.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
session_local = sessionmaker(autocommit = False, autoflush = False , bind=engine)
# SessionLocal = sessionmaker(autocommit = False, autoflush = False , bind=engine)

base = declarative_base()

# 이게 테이블에 해당한다. 
class Question(declarative_base(base)):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Answer(base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship('Question', backref='answers')
