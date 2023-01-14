from typing import Optional
from fastapi import FastAPI, Response, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()


class Post(BaseModel):  # pydantic_Model
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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


# Get all post
@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * From posts  """)
    posts = cursor.fetchall()
    print(posts)
    return {"data": posts}


# Create post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING
    *  """,
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


# Get single post
@app.get("/post/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * From posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_details": post}


# Delete Post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """DELETE From posts WHERE id = %s returning *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update Post
@app.put("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, post: Post):

    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s  WHERE id = %s RETURNING *""",
                   (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return {"data": updated_post}
