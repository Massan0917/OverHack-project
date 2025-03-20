from src.services.detect_face import detect_faces
from src.services.recognize_face import recognize_face
from src.models.bounding_box import BoundingBox
from fastapi import APIRouter


router = APIRouter()



@router.get("/api/test/image")
def image_test():
    bouding_boxes: list[BoundingBox] = recognize_face('/app/images/upload/test01.jpg')

    detect_faces(
        '/app/images/upload/test01.jpg',
        '/app/images/masked/test01.jpg',
        bouding_boxes
    )
