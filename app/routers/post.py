from .. import models, schemas
from typing import List
from fastapi import Response, HTTPException, status, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# Get all post
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post


# Create post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict()
                           )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Get single post
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print("get", post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return post


# Delete Post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update
@router.put("/{id}", response_model=schemas.Post)
def updated_post(id: int, newly_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_query.update(newly_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
