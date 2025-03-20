from fastapi import APIRouter
from src.services.recognize_face import recognize_face
from src.models.bounding_box import BoundingBox


router = APIRouter()



### 顔検出API
@router.get("/api/face-detect")
def face_detect(image_path: str):
    bounding_boxes: list[BoundingBox] = recognize_face(image_path)
    return {
        "bounded-boxes": bounding_boxes
    }
