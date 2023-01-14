from typing import Optional
from fastapi import FastAPI, Response, HTTPException, status
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


def find_index_post(id):
    for index, p in enumerate(my_posts):
        if p['id'] == id:
            print(p)
            return index


# Get all post
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# Create post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_details": post}


# Delete Post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post_delete_index = find_index_post(id)
    if post_delete_index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    my_posts.pop(post_delete_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update Post
@app.put("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_post(id: int, post: Post):
    update_post_index = find_index_post(id)
    if update_post_index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    post_dict_update = post.dict()
    post_dict_update["id"] = id
    my_posts[update_post_index] = post_dict_update
    return {"data": post_dict_update}
