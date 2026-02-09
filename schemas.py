from pydantic import BaseModel

class userCreate(BaseModel):
    username : str
    email: str
    password: str

class userLogin(BaseModel):
    email:str
    password : str

class userResponse(BaseModel):
    username:str
    email:str
    password : str

class userUpdate(BaseModel):
    username: str
    email: str

class token(BaseModel):
    access_token : str
    token_type: str


