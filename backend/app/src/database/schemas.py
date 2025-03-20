from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    date: str
    img_path: str
    masked_img_path: str
    user_name: str
    comment: str
    GPT_comment: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
