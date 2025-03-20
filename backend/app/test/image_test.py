from src.services.detect_face import detect_faces
from src.services.recognize_face import recognize_face
from src.models.bounding_box import BoundingBox
from fastapi import APIRouter


router = APIRouter()



@router.get("/api/test/image")
def image_test(image_path: str):
    bouding_boxes: list[BoundingBox] = recognize_face(image_path)

    output_path = detect_faces("test01", image_path, bouding_boxes)

    return {
        "output_path": output_path
    }
