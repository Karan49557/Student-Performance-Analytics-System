from flask import Flask, jsonify, render_template, request
import time

app = Flask(__name__)

# In-memory database (Initial mock students)
students_db = [
    {"id": 1, "name": "Aarav Sharma", "score": 92},
    {"id": 2, "name": "Priya Verma", "score": 85},
    {"id": 3, "name": "Rohan Patel", "score": 68},
    {"id": 4, "name": "Neha Gupta", "score": 45},
    {"id": 5, "name": "Kabir Singh", "score": 32}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/students", methods=["GET", "POST"])
def manage_students():
    global students_db
    if request.method == "POST":
        data = request.json
        new_student = {
            "id": data.get("id", int(time.time() * 1000)),
            "name": data.get("name"),
            "score": float(data.get("score"))
        }
        students_db.append(new_student)
        return jsonify({"success": True, "students": students_db}), 201
    
    return jsonify(students_db)

@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students_db
    students_db = [s for s in students_db if s["id"] != student_id]
    return jsonify({"success": True, "students": students_db})

@app.route("/api/students/clear", methods=["POST"])
def clear_students():
    global students_db
    students_db = []
    return jsonify({"success": True, "students": students_db})

if __name__ == "__main__":
    app.run(debug=True)