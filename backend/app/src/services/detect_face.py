import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from src.models.bounding_box import BoundingBox
import urllib
import cv2
import os
import random



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

    # 合成（例: 中心(200, 150)、幅100、高さ80）
    for box in bounding_boxes:
        # スタンプ画像を読み込む
        stamp_path = __select_stamp()
        stamp = cv2.imread(stamp_path, cv2.IMREAD_UNCHANGED)
        image = __detect_one_face(image, stamp, box)

    # 画像を保存
    output_path = f"static/masked/{file_name}.jpg"
    cv2.imwrite(output_path, image)

    output_url = "http://localhost:3000/" + output_path
    return output_url



# 1つの顔にスタンプを貼り付ける
def __detect_one_face(image, stamp, box: BoundingBox):

    # 画像をリサイズ
    stamp = cv2.resize(stamp, (box.width, box.height))

    if stamp.shape[2] == 4:  # 透過PNG対応
        stamp_bgr = stamp[:, :, :3]  # BGRチャンネル
        stamp_alpha = stamp[:, :, 3] / 255.0  # アルファチャンネル（0～1に正規化）
    else:
        stamp_bgr = stamp
        stamp_alpha = np.ones((box.height, box.width))  # アルファがない場合は完全不透明

    # 貼り付ける領域の座標を計算
    x1, y1 = box.x_center - box.width // 2, box.y_center - box.height // 2
    x2, y2 = x1 + box.width, y1 + box.height

    image_part = image[y1:y2, x1:x2]

    for c in range(3):  # B, G, R それぞれのチャンネルで合成
        image_part[:, :, c] = (stamp_bgr[:, :, c] * stamp_alpha + image_part[:, :, c] * (1 - stamp_alpha)).astype(np.uint8)


    # 背景画像の該当部分を前景画像に置き換え
    image[y1:y2, x1:x2] = image_part

    return image



# スタンプを選択
def __select_stamp() -> str:

    images_dir = "assets/images"

    if random.random() < 0.1:
        # レアスタンプ
        images_dir += "/rare"
    else:
        # 通常スタンプ
        images_dir += "/normal"


    if not os.path.exists(images_dir) or not os.path.isdir(images_dir):
        raise FileNotFoundError(f"Directory '{images_dir}' not found.")

    images = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png'))]

    if not images:
        raise FileNotFoundError("No images found in the directory.")

    return os.path.join(images_dir, random.choice(images))