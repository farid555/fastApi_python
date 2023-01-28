from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):  # pydantic_Model
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


"""
class Post(BaseModel):  # sending limited property in frontend
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    
    /////////
    {
        "Post": {
            "published": true,
            "owner_id": 2,
            "title": "eee  search option Test-3",
            "id": 22,
            "content": "this is awesome ,",
            "created_at": "2023-01-21T20:09:30.944754+02:00"
        },
        "votes": 0
    },

"""


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):  # sending limited property in frontend
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):  # login user model
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


# vote


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
