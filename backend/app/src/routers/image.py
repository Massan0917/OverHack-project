from fastapi import APIRouter, File, UploadFile
import datetime
import shutil


router = APIRouter()



### 画像アップロードAPI
@router.post("/api/image")
async def image( image: UploadFile = File() ):
    # TODO
    file_name = datetime.datetime.now(
        datetime.timezone(
            datetime.timedelta(hours=9),
            'JST'
        )
    ).strftime('%Y%m%d_%H%M%S') + '.jpg'

    image_path = f"static/uploads/{file_name}"
    with open(image_path, "wb") as file_object:
        shutil.copyfileobj(image.file, file_object)

    return {
        "image_path": 'http://localhost:3000/' + image_path,
    }
