from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.problem import Problem

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def show_problems(request: Request, db: Session = Depends(get_db)):
    problems = db.query(Problem).all()
    return templates.TemplateResponse("index.html", {"request": request, "problems": problems})

@router.post("/problems")
def add_problem(title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
    new_problem = Problem(title=title, description=description)
    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)
    return RedirectResponse("/", status_code=303)