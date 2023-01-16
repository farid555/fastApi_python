from typing import Optional, List
from fastapi import FastAPI, Response, HTTPException, status, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:

    try:
        conn = psycopg2.connect(
            host='localhost', database='fastApi', user='postgres', password='farid555', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was succesful!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error", error)
        time.sleep(2)


my_posts = [{"title": "Python", "content": "It is powerful, user-friendly and easy to learn.", "id": 1}, {
    "title": "Java", "content": "It is a particularly popular programming language for server-client web applications", "id": 2}, {
    "title": "Javascript", "content": "JavaScript is a lightweight interpreted programming language", "id": 3
}]


def find_post(id):
    for p in my_posts:
        print(type(p))
        if p['id'] == id:
            return p


def find_index_post(id):
    for index, p in enumerate(my_posts):
        if p['id'] == id:
            print("T4", p)
            return index


# test Database create


# Get all post
@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post


# Create post
@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    print(post.dict())
    new_post = models.Post(**post.dict()
                           )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Get single post
@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print("get", post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return post


# Delete Post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update
@app.put("/posts/{id}", response_model=schemas.Post)
def updated_post(id: int, newly_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_query.update(newly_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
