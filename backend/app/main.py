from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from src.routers import post, query, object_detection
from src.database.database import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(post.router)
app.include_router(object_detection.router)
app.include_router(query.router)

@app.get("/api/hoge")
def index1():
    return {"message": "hogehoge"}


@app.get("/api/fuga")
def index2():
    return {"message": "fugafuga"}

Base.metadata.create_all(bind=engine)


# Dockerfileからuvicorn(FastAPIサーバー）を起動する
if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
        port=3000,
        log_level="debug",)
