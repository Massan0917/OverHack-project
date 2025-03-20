from fastapi import APIRouter
from src.services.recognize_face import recognize_face
from src.models.bounding_box import BoundingBox


router = APIRouter()



### 物体検出API
@router.get("/api/face_detect")
def face_detect(image_path: str):
    bounding_boxes: list[BoundingBox] = recognize_face(image_path)
    return {
        "bounded_boxes": bounding_boxes
    }
