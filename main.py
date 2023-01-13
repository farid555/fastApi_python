from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()


class Post(BaseModel):  # pydantic_Model
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "Python", "content": "It is powerful, user-friendly and easy to learn.", "id": 1}, {
    "title": "Java", "content": "It is a particularly popular programming language for server-client web applications", "id": 2}, {
    "title": "Javascript", "content": "JavaScript is a lightweight interpreted programming language", "id": 3
}]


def find_post(id):
    for p in my_posts:
        print(type(p))
        if p['id'] == id:
            return p

# Get all post


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# Create post
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)  # added random ID weith post bodoy
    print(post.dict())   # Change paydantic model to Dict()...[create a object]
    my_posts.append(post_dict)
    print(my_posts)  # store the newlly created post_dict in my_posts
    return {"data": post_dict}


# Get single post
@app.get("/post/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND # status HTTP_Error 
        return {"message": f"post with id:{id} not found"}
    return {"post_details": post}
