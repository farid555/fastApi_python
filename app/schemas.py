from pydantic import BaseModel


class PostBase(BaseModel):  # pydantic_Model
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


    

