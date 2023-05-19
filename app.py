from flask import Flask, render_template, request, url_for
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

db = {}
@app.route('/registration', methods=["GET","POST"])
def register():
    if request.method == "POST":
        data = request.form
        with open('users', 'w+') as file:
            db[data["username"]] = data
            file.write(json.dumps(db))
        return data
    return render_template("registration.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        data = request.form
        with open('users', 'r') as file:
            file = file.read()
            file = json.loads(file)
            if data['username'] in file:
                if file[data['username']]['password'] == data['password']:
                    return "Successful Login"
                return "Invalid Password"
            return "Wrong Credentials"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)