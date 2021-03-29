from flask import request, jsonify
from app import app, db
from app.models import Todo

@app.route("/")
def index():
    return "hellow"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    todos = Todo.query.all()
    for todo in todos:
        tasks.append(todo.task)
    return jsonify({'tasks': tasks}), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json.get('task'):
        return jsonify({'error': 'cannot add task'}), 400
    todo = Todo(task = request.json.get('task'))
    db.session.add(todo)
    db.session.commit()
    return jsonify({'msg': 'task added'}), 200

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    todo = Todo.query.get(task_id)
    if not todo:
        return jsonify({'error': 'invalid id'}), 404
    updated_task = request.json.get('task')
    if not updated_task:
        return jsonify({'error': 'invalid task'}), 400
    todo.task = updated_task
    db.session.commit()
    return jsonify({'msg': 'task updated'}), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    todo = Todo.query.get(task_id)
    if not todo:
        return jsonify({'error': 'invalid id'}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'msg': 'task removed'}), 200