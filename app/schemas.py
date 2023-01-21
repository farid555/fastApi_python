from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


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
