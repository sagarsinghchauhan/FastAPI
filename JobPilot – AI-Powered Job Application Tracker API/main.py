from fastapi import FastAPI 
from Database.database import engine , Base
from auth.routers import router 
from auth.model import User
app = FastAPI()

Base.metadata.create_all(bind  = engine)

app.include_router(router)
