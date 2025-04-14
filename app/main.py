from fastapi import FastAPI
from app.routers import problems
from app.database import engine
from app.models import problem as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(problems.router)