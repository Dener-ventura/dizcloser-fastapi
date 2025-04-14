from fastapi import FastAPI
from app.routers import problems

app = FastAPI()

app.include_router(problems.router)

@app.get("/")
def read_root():
    return {"message": "Hello, Dizcloser!"}