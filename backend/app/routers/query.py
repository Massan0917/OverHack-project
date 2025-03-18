from fastapi import APIRouter

router = APIRouter()

### 画像閲覧API
@router.get("/api/face-detect")
async def query():
    return {
        "posts": [
                {
                    "id": 1,
                    "user-name": "user1",
                    "comment": "comment1",
                    "masked-img-Spath": "image1.jpg",
                },
            ],
    }