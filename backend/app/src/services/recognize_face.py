from ultralytics import YOLO
from src.models.bounding_box import BoundingBox
import os


# 画像から顔を検出する
def recognize_face(image_path: str) -> list[BoundingBox]:
    # YOLOモデルを読み込み
    model = YOLO('assets/yolo_models/yolov8n-face.pt')

    # 顔を検出
    results = model(image_path)

    bounding_boxes: list[BoundingBox] = []

    # 顔の座標を取得
    for index, face in enumerate(results[0].boxes.xywh):
        shape = face.numpy()

        bounding_boxes.append(BoundingBox(
            id=index,
            x_center=int(shape[0]),
            y_center=int(shape[1]),
            width=int(shape[2]),
            height=int(shape[3]),
        ))

    file_name = image_path[image_path.rfind('/') + 1:]
    if file_name.endswith('.jpg'):
        os.remove(file_name)

    return bounding_boxes
