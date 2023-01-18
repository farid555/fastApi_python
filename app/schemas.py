from pydantic import BaseModel, EmailStr
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


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
