from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Aarav", "age": 20},
    {"id": 2, "name": "Shruti", "age": 21},
    {"id": 3, "name": "Ishaan", "age": 22}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Optional: root route just to avoid 404 if you go to "/"
# @app.route('/')
# def index():
#     return "Student API is running. Use /students endpoint."

if __name__ == '__main__':
    app.run(debug=True)
