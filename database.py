import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    connection.close()
    print("Postgres working")
        

except Exception as e:
    print("Postgres connection not successful",e)


sessionLocal = sessionmaker(
    bind = engine
)

BaseClass = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()



        