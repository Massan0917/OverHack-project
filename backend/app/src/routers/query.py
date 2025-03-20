from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
import src.database.crud as crud


router = APIRouter()



### 画像閲覧API
@router.get("/api/face-detect")
def query(db: Session = Depends(get_db)):
    result = crud.get_posts(db)

    # 日付の降順に並び替え
    sorted_result = sorted(result, key=lambda post: post.date, reverse=True)

    # 先頭から10件取得
    filtered_result = sorted_result[:10]

    return {
        "posts": [
            {
                "id": post.id,
                "user-name": post.user_name,
                "comment": post.comment,
                "masked-img-path": post.masked_img_path,
            } for post in filtered_result
        ],
    }
