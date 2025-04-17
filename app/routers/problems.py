from fastapi import APIRouter, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.problem import Problem

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/new")
async def new_problem(request: Request):
    return templates.TemplateResponse("new_problem.html", {"request": request})

@router.post("/submit")
async def submit_problem(request: Request, title: str = Form(...), description: str = Form(...)):
    problem = {"title": title, "description": description, "responses": []}
    problems_db.append(problem)
    return RedirectResponse(url="/", status_code=303)

@router.get("/problem/{id}")
async def view_problem(request: Request, id: int):
    if id < 0 or id >= len(problems_db):
        return templates.TemplateResponse("index.html", {"request": request, "problems": problems_db})
    return templates.TemplateResponse("problem_detail.html", {
        "request": request,
        "problem": problems_db[id],
        "id": id
    })

@router.post("/problem/{id}/respond")
async def respond_problem(request: Request, id: int, response: str = Form(...)):
    if 0 <= id < len(problems_db):
        problems_db[id]["responses"].append(response)
    return RedirectResponse(url=f"/problem/{id}", status_code=303)
