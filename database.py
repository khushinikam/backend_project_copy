from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://postgres:root@localhost:5432/auth_db"


engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    bind= engine
)

BaseClass = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()



        