import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from src.models.bounding_box import BoundingBox
import requests
import urllib
from io import BytesIO



# 画像の顔を保護する
def detect_faces(
    file_name: int,
    input_path: str,
    bounding_boxes: list[BoundingBox],
) -> bool:
    # 画像を読み込み
    url = urllib.parse.unquote(input_path)
    response = requests.get(url)
    file_contents = BytesIO(response.content)
    image = img.imread(file_contents, format="jpg").copy()

    for box in bounding_boxes:
        __detect_one_face(image, box)

    # 画像を保存
    output_path = f"static/masked/{file_name}.jpg"
    plt.imsave(f"{output_path}", image)

    output_url = "http://localhost:3000/" + output_path

    return output_url

def __detect_one_face(image: np.ndarray, box: BoundingBox) -> np.ndarray:
    # TODO

    color = (1,0,0)

    if image.dtype == np.uint8:
        color = tuple(int(c * 255) for c in color)  # 0-255 に変換
    elif image.dtype == np.float32 or image.dtype == np.float64:
        color = tuple(c for c in color)  # そのまま使用

    x, y, w, h = box.x_center, box.y_center, box.width, box.height

    # 塗りつぶす領域の開始・終了座標を計算
    x1, x2 = max(0, x - w // 2), min(image.shape[1], x + w // 2)
    y1, y2 = max(0, y - h // 2), min(image.shape[0], y + h // 2)

    # 指定領域を塗りつぶし
    image[y1:y2, x1:x2, :3] = color

    return image
