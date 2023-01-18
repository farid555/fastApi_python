from .. import models, schemas, utils
from fastapi import HTTPException, status, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


# Get all user
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    user = db.query(models.User).all()
    return user


# Create User
@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user.dict())
    # hash the password - user.password

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict()
                           )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get user by id

@router.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    print("get_id", user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return user
