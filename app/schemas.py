from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):  # pydantic_Model
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


'''
class Post(BaseModel):  # sending limited property in frontend
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime

'''


class Post(PostBase):  # sending limited property in frontend
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True
