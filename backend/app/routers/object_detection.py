from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Image(BaseModel):
    image_path: str


### 物体検出API
@router.get("/api/face-detect")
async def face_detect(image: Image):
    return {
        "bounded_boxes": [
            {
                "id": 1,
                "x_center": 0.5,
                "y_center": 0.5,
                "width": 0.5,
                "height": 0.5,
            },
        ]
    }