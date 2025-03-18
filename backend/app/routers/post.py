from fastapi import APIRouter
from pydantic import BaseModel

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
async def post(post: Post):
    return {
        "status": "success",
        "post_id": 1,
    }
