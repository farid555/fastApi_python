from typing import Optional, List
from fastapi import FastAPI, Response, HTTPException, status, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
