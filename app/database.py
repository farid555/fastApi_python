from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:farid555@localhost/postgres'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


'''
while True:

    try:
        conn = psycopg2.connect(
            host='localhost', database='postgres', user='postgres', password='farid555', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was succesful!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error", error)
        time.sleep(2)
'''
