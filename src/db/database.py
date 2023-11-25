from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://root:shrjsgh@svc.sel5.cloudtype.app:31880/zipper"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ = "health_users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(40))
    gender = Column(CHAR(2))
    age = Column(Integer(4))

Base.metadata.create_all(bind=engine)