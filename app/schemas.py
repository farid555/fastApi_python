from pydantic import BaseModel


class Post(BaseModel):  # pydantic_Model
    title: str
    content: str
    published: bool = True
