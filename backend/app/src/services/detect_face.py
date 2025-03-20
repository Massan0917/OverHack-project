import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from src.models.bounding_box import BoundingBox
import urllib
import cv2



# 画像の顔を保護する
def detect_faces(
    file_name: int,
    input_path: str,
    bounding_boxes: list[BoundingBox],
) -> bool:

    # 画像を読み込む
    url = urllib.parse.unquote(input_path)
    response = urllib.request.urlopen(url)
    image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # スタンプ画像を読み込む
    stamp = cv2.imread("assets/images/stamp_test.png", cv2.IMREAD_UNCHANGED)

    # 合成（例: 中心(200, 150)、幅100、高さ80）
    for box in bounding_boxes:
        image = __detect_one_face(image, stamp, box)

    # 画像を保存
    output_path = f"static/masked/{file_name}.jpg"
    cv2.imwrite(output_path, image)

    output_url = "http://localhost:3000/" + output_path
    return output_url



def __detect_one_face(image, stamp, box: BoundingBox):
    # 画像を BGR に変換（透過情報がない場合は無視）
    if stamp.shape[2] == 4:
        stamp = cv2.cvtColor(stamp, cv2.COLOR_BGRA2BGR)

    # 画像をリサイズ
    stamp = cv2.resize(stamp, (box.width, box.height))

    # 貼り付ける領域の座標を計算
    x1, y1 = box.x_center - box.width // 2, box.y_center - box.height // 2
    x2, y2 = x1 + box.width, y1 + box.height

    # 範囲を超えないように制限
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(image.shape[1], x2), min(image.shape[0], y2)

    # 背景画像の該当部分を前景画像に置き換え
    image[y1:y2, x1:x2] = stamp[:y2-y1, :x2-x1]

    return image
