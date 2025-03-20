from pydantic import BaseModel

class BoundingBox(BaseModel):
    id: int
    x_center: int
    y_center: int
    width: int
    height: int