from application import app, db
from application.models import Task_table
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for

@app.route('/')

@app.route('/home')
def home():
    all_tasks = Task_table.query.all()
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)

@app.route("/create", methods=["GET", "POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Task_table(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title="Create a Task",form = form)


@app.route('/complete/<int:id>')
def complete(id):
    task_to_change = Task_table.query.filter_by(task_id = id).first()
    task_to_change.task_status = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task_to_change = Task_table.query.filter_by(task_id = id).first()
    task_to_change.task_status = False
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = TaskForm()
    task_to_change = Task_table.query.filter_by(task_id = id).first()
    if request.method == "POST":
        task_to_change.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Task", task=task_to_change)

@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    task_to_delete = Task_table.query.filter_by(task_id=id).first()
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("home"))
