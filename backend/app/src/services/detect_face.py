import numpy
from matplotlib import pyplot, image
from src.models.bounding_box import BoundingBox



# 画像の顔を保護する
def detect_faces(
    input_path: str,
    output_path: str,
    bounding_boxes: list[BoundingBox],
) -> bool:
    # 画像を読み込み
    img = image.imread(input_path).copy()

    for box in bounding_boxes:
        __detect_one_face(img, box)

    # 画像を保存
    pyplot.imsave(output_path, img)

    return True

def __detect_one_face(img: numpy.ndarray, box: BoundingBox) -> numpy.ndarray:

    color = (1,0,0)

    if img.dtype == numpy.uint8:
        color = tuple(int(c * 255) for c in color)  # 0-255 に変換
    elif img.dtype == numpy.float32 or img.dtype == numpy.float64:
        color = tuple(c for c in color)  # そのまま使用

    x, y, w, h = box.x_center, box.y_center, box.width, box.height

    # 塗りつぶす領域の開始・終了座標を計算
    x1, x2 = max(0, x - w // 2), min(img.shape[1], x + w // 2)
    y1, y2 = max(0, y - h // 2), min(img.shape[0], y + h // 2)

    # 指定領域を塗りつぶし
    img[y1:y2, x1:x2, :3] = color

    return img
