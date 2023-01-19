from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..import database, schemas, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    '''
    {
       "username" : "any name or email",  #OAuth2PasswordRequestForm it doesn't care email or name, it should be name
       "password" : "password"
    }
    '''
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

        # create a token
        # return a token

    access_token = oauth2.create_Access_Token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
