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
@router.post("/api/face-detect")
def post(post: Post, db: Session = Depends(get_db)):

    date = datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(hours=9),
            'JST'
        )
    ).strftime('%Y%m%d')

    input_path = '/app/images/upload/' + post.image_path
    output_path = '/app/images/masked/' + post.image_path

    detect_result: bool = detect_faces(input_path, output_path, post.bounding_boxes)

    if not detect_result:
        return {
            "message": "Failed to detect faces."
        }

    post_param = PostCreate(
        date=date,
        img_path=post.image_path,
        masked_img_path=post.image_path,
        user_name=post.name,
        comment=post.comment,
        GPT_comment=""
    )
    return crud.create_post(db=db, post=post_param)
