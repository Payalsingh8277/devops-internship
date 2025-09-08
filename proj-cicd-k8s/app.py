from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return "Welcome to Student Management App on Kubernetes!"

@app.route('/add', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added", "students": students})

@app.route('/list', methods=['GET'])
def list_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

