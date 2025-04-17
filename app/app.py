from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Simulação do banco de dados em memória
problems = []

@app.route("/")
def home():
    return render_template("index.html", problems=problems)

@app.route("/new")
def new_problem():
    return render_template("new_problem.html")

@app.route("/submit", methods=["POST"])
def submit_problem():
    title = request.form["title"]
    description = request.form["description"]
    problems.append({
        "title": title,
        "description": description,
        "responses": []
    })
    return redirect("/")

@app.route("/problem/<int:id>")
def view_problem(id):
    problem = problems[id]
    return render_template("problem_detail.html", problem=problem, id=id)

@app.route("/problem/<int:id>/respond", methods=["POST"])
def respond_problem(id):
    response = request.form["response"]
    problems[id]["responses"].append(response)
    return redirect(f"/problem/{id}")

if __name__ == "__main__":
    app.run(debug=True)
