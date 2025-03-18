from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from src.database.database import Base

class Post(Base):
    __tablename__ = "post"  # テーブル名を指定
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String, index=True)
    img_path = Column(String, index=True)
    masked_img_path = Column(String, index=True)
    user_name = Column(String, index=True)
    comment = Column(String, index=True)
    GPT_comment = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )