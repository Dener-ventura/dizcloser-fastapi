from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Simulando banco temporário
problems_db = []

@router.get("/", response_class=HTMLResponse)
def show_problems(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "problems": problems_db})

@router.post("/problems")
def add_problem(title: str = Form(...), description: str = Form(...)):
    new_id = len(problems_db) + 1
    problems_db.append({"id": new_id, "title": title, "description": description})
    return RedirectResponse("/", status_code=303)