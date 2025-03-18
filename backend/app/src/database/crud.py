from sqlalchemy.orm import Session
import src.database.models as models
import src.database.schemas as schemas

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post: schemas.Post):
    db.query(models.Post).filter(models.Post.id == post_id).update(post.dict())
    db.commit()
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Post).offset(offset).limit(limit).all()

def delete_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).delete()
