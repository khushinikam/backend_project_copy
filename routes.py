from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas, authentication

router = APIRouter()

# @router.get("/users")

@router.post("/signup")
def signup(user: schemas.userCreate, db: Session = Depends(get_db)):
    
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=authentication.hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}


@router.post("/login", response_model=schemas.token)

def login(user: schemas.userLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user or not authentication.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    

    token = authentication.create_access_token({"subject": db_user.email})
    return {"access_token": token, "token_type": "bearer"}

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return {"message": "User deleted successfully"}