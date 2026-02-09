from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas, authentication

router = APIRouter()

# get all users 

@router.get("/users", response_model=list[schemas.userResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# create users signup

@router.post("/signup")
def signup(user: schemas.userCreate, db: Session = Depends(get_db)):
    
    new_user = models.User(
        username=user.username, email=user.email, password=authentication.hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

# users can login with same credentials

@router.post("/login", response_model=schemas.token)

def login(user: schemas.userLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    token = authentication.access_token({"subject": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

# update username, email of a user by its respective id

@router.put("/update/{user_id}", response_model=schemas.userResponse)
def update_user(
    user_id: int, user: schemas.userUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    else:
        db_user.username = user.username
        db_user.email = user.email

        db.commit()
        db.refresh(db_user)

        return db_user

# delete a user by its respective id

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User does not exist")
    else:
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}