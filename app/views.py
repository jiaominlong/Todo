from app import app, db
from flask import render_template, flash, redirect
from app.models import Todo
from app.forms import Todo_form
import datetime

@app.route('/')
def index():
    form = Todo_form()
    todos = Todo.query.order_by(Todo.time.desc())
    print(todos)
    return render_template('index.html', todos=todos, form=form)



# @app.route('/add', methods=['POST',])
# def add():
#     form = Todo_form()
#     if form.validate_on_submit():
#         content = form.content.data
#         todo = Todo(content=content, time=datetime.datetime.now())
#         db.session.add(todo)
#         db.session.commit()
#         todos = Todo.query.order_by(Todo.time.desc()).all()
#         return render_template('index.html', form=form, todos=todos)
#     else:
#         todos = Todo.query.all()
#         flash(str(form.content.errors))
#         return render_template('index.html', form=form, todos=todos)

@app.route('/add', methods=['POST',])
def add():
    form = Todo_form()
    if form.validate_on_submit():
        content = form.content.data
        todo = Todo(content=content, time=datetime.datetime.now())
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        todos = Todo.query.all()
        flash(str(form.content.errors))
        return render_template('index.html', form=form, todos=todos)



@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = Todo_form()
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.status = 1
    db.session.add(todo)
    db.session.commit()
    return redirect('/')


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = Todo_form()
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.status = 0
    db.session.add(todo)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = Todo_form()
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html' ,error=error), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('404.html'), 500



