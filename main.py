from fastapi import FastAPI
from database import BaseClass, engine
from routes import router

print("Connection start")

BaseClass.metadata.create_all(bind=engine)

print("Connection built")

app = FastAPI()

app.include_router(router)

@app.get("/")
async def home():
    return {"status":" routes working fine"}