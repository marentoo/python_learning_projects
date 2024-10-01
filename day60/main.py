from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def post_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1> Name: {name} and pass: {password} </h1>"
    # return "💪 Success! Form submitted"



if __name__ =="__main__":
    app.run(debug=True)