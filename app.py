from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

# Create Database
with app.app_context():
    db.create_all()
# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Get Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()

    task_list = []

    for task in tasks:
        task_list.append({
            'id': task.id,
            'task': task.task
        })

    return jsonify(task_list)

# Add Task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or 'task' not in data:
        return jsonify({'error': 'Task required'}), 400

    new_task = Task(task=data['task'])

    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task added successfully'}), 201

# Delete Task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    task = db.session.get(Task, id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)