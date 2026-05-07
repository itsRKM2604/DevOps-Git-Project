from flask import Flask, request, render_template,json, redirect
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/",methods=["POST","GET"])
def add_data():
    if request.method == "POST":
        name=request.form.get("name");
        email=request.form.get("email");
        created_at = datetime.now().isoformat()

        new_data = {
            "fullname": name,
            "email": email,
            "created_at": created_at
        }

        data = load_data()
        data.append(new_data)
        save_data(data)
        return redirect("/")
    
    data = load_data()
    return render_template("index.html", data=data, msg="Welcome to User Registration Form")

if __name__ == "__main__":
    app.run(debug=True)