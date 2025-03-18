import datetime
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database.database import get_db
import src.database.crud as crud
from src.database.schemas import PostCreate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

router = APIRouter()

class BoundingBox(BaseModel):
    id: int
    x_center: int
    y_center: int
    width: int
    height: int

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

    __make_masked_img(input_path, output_path, post.bounding_boxes)

    post_param = PostCreate(
        date=date,
        img_path=post.image_path,
        masked_img_path=post.image_path,
        user_name=post.name,
        comment=post.comment,
        GPT_comment=""
    )
    return crud.create_post(db=db, post=post_param)

def __make_masked_img(input_path: str, output_path: str, bounding_boxes: list[BoundingBox]) -> str:
    # 画像を読み込む
    color = (1, 0, 0)
    img = mpimg.imread(input_path).copy()

    # 画像が float 型 (0-1) の場合と uint8 (0-255) の場合の対応
    if img.dtype == np.uint8:
        color = tuple(int(c * 255) for c in color)  # 0-255 に変換
    elif img.dtype == np.float32 or img.dtype == np.float64:
        color = tuple(c for c in color)  # そのまま使用

    for box in bounding_boxes:
        x, y, w, h = box.x_center, box.y_center, box.width, box.height

        # 塗りつぶす領域の開始・終了座標を計算
        x1, x2 = max(0, x - w // 2), min(img.shape[1], x + w // 2)
        y1, y2 = max(0, y - h // 2), min(img.shape[0], y + h // 2)

        # 指定領域を塗りつぶし
        img[y1:y2, x1:x2, :3] = color

    # 画像を保存
    plt.imsave(output_path, img)
