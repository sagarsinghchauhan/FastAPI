from fastapi import FastAPI 
from Database.database import engine , Base
from auth.routers import router  as auth_router
from auth.model import User
from jobs.router import router as job_router 
from jobs.model import JobApplication
from analytics.routers import  router as analytics_router


app = FastAPI()


Base.metadata.create_all(bind  = engine)

app.include_router(auth_router)
app.include_router(job_router)
app.include_router(analytics_router)


