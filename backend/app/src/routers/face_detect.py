from fastapi import APIRouter
import datetime
from src.services.recognize_face import recognize_face
from src.services.detect_face_confirm import detect_faces_confirm
from src.models.bounding_box import BoundingBox


router = APIRouter()



### 顔検出API
@router.get("/api/face-detect")
def face_detect(image_path: str):
    bounding_boxes: list[BoundingBox] = recognize_face(image_path)
    # TODO
    file_name = datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(hours=9),
            'JST'
        )
    ).strftime('%Y%m%d_%H%M%S')

    output_url = detect_faces_confirm(
        file_name,
        image_path,
        bounding_boxes
    )

    return {
        "bounding_boxes": bounding_boxes,
        "confirm_image_path": output_url
    }
