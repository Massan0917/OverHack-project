from fastapi import APIRouter
from ultralytics import YOLO

router = APIRouter()

class BoundingBox():

    def __init__(
        self,
        id: int,
        x_center: int,
        y_center: int,
        width: int,
        height: int
):
        self.id = id
        self.x_center = x_center
        self.y_center = y_center
        self.width = width
        self.height = height



### 物体検出API
@router.get("/api/face-detect")
def face_detect(image_path: str):
    bounding_boxes = __find_mask_area('/app/images/upload/' + image_path)
    return {
        "bounded_boxes": bounding_boxes
    }



def __find_mask_area(image_path: str) -> list[BoundingBox]:
    model = YOLO('assets/yolo_models/yolov8n-face.pt')

    results = model(image_path)

    bounding_boxes = []

    for index, face in enumerate(results[0].boxes.xywh):
        shape = face.numpy()

        bounding_boxes.append(BoundingBox(
            id=index,
            x_center=int(shape[0]),
            y_center=int(shape[1]),
            width=int(shape[2]),
            height=int(shape[3]),
        ))

    return bounding_boxes
