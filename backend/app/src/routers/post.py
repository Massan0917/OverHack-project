import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database.database import get_db
import src.database.crud as crud
from src.database.schemas import PostCreate
from src.models.bounding_box import BoundingBox
from src.services.detect_face import detect_faces


router = APIRouter()


class Post(BaseModel):
    name: str
    comment: str
    image_path: str
    bounding_boxes: list[BoundingBox]



### 投稿API
@router.post("/api/upload")
def post(post: Post, db: Session = Depends(get_db)):

    date = datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(hours=9),
            'JST'
        )
    ).strftime('%Y%m%d')

    # TODO
    file_name = datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(hours=9),
            'JST'
        )
    ).strftime('%Y%m%d%H%M%S')

    output_url = detect_faces(
        file_name,
        post.image_path,
        post.bounding_boxes
    )

    post_param = PostCreate(
        date=date,
        img_path=post.image_path,
        masked_img_path=output_url,
        user_name=post.name,
        comment=post.comment,
        GPT_comment=""
    )
    return crud.create_post(db=db, post=post_param)
