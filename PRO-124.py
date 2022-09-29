from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

tasks = [
    {
        "id": 1,
        "Student": "Anjana",
        "Class": "C-125",
        "done": False
    },
    {
        "id": 2,
        "Student": "Anirudh",
        "Class": "C-120",
        "done": False
    }
]

@app.route("/app-data", methods=["POST"])

def app_data():
    if not request.json:
        return jsonify(
            {
                "status": "error",
                "message": "Please provide the data."
            }, 400
        )

    task = {
        "id": tasks[-1][id] + 1,
        "Student": request.json["Student"],
        "Class": request.json.get("Class", ""),
        "done": False
    }
    tasks.append(task)
    return jsonify(
        {
            "status": "success",
            "message": "Task has been added."
        }
    )

@app.route("/get-data")

def get_data():
    return jsonify(
        {
            "data": tasks
        }
    )

if (__name__ == "__main__"):
    app.run(debug = True)