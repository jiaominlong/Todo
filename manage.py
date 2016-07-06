from app import app, db
from app.models import Todo
from flask_script import Manager

manager = Manager(app)


@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def save():
    todo = Todo(content='Study flask')
    db.session.add(todo)
    db.session.commit()


if __name__ == '__main__':
    manager.run()