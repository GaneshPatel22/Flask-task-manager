from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

task_list = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(task_list)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_list.append(data['task'])
    return jsonify({'message': 'Task added successfully'}), 201

@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(task_list):
        task_list.pop(index)
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Invalid index"}), 404

if __name__ == '__main__':
    app.run(debug=True)

    
    