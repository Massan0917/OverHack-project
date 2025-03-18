from typing import List, Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    id: int
    date: str
    img_path: str
    masked_img_path: str
    user_name: str
    comment: str
    GPT_comment: str

class PostCreate(PostBase):
    date: str
    img_path: str
    masked_img_path: str
    user_name: str
    comment: str
    GPT_comment: str

class Post(PostBase):
    id: int
    date: str
    img_path: str
    masked_img_path: str
    user_name: str
    comment: str
    GPT_comment: str

    class Config:
        orm_mode = True
