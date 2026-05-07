from flask import Flask, render_template, request, redirect
import requests

BACKEND_URL="http://152.26.73.2:9001"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="To Do")

@app.route("/submittodoitem", methods=['POST'])
def submitToDoItem():
    iname = request.form.get("iname")
    idesc = request.form.get("idesc")

    form_data = {
        "iname": iname,
        "idesc": idesc
    }

    
    response = requests.post(
        BACKEND_URL + "/submittodoitem",
        json=form_data,
        timeout=5
    )

    data = response.json()

    if response.status_code == 200 and data.get("success"):
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)