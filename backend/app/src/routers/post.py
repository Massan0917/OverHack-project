from datetime import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database.database import get_db
import src.database.crud as crud
from src.database.schemas import PostCreate

router = APIRouter()

class BoundingBox(BaseModel):
    id: int
    x_center: float
    y_center: float
    width: float
    height: float

class Post(BaseModel):
    name: str
    comment: str
    image_path: str
    bounding_boxes: list[BoundingBox]

### 投稿API
@router.post("/api/face-detect")
def post(post: Post, db: Session = Depends(get_db)):

    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    date = datetime.datetime.now(JST).strftime('%Y%m%d')

    masked_img_path = __make_masked_img(post.image_path, post.bounding_boxes)

    post_param = PostCreate(
        date=date,
        img_path=post.image_path,
        masked_img_path=masked_img_path,
        user_name=post.name,
        comment=post.comment,
        GPT_comment=""
    )
    return crud.create_post(db=db, post=post_param)

def __make_masked_img(path: str, bounding_boxes: list[BoundingBox]) -> str:
    # TODO : 画像にマスクをかける処理を実装
    return path