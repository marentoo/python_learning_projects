from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def home():
    return '<h1 style="text-align: center"> Guess the number between 0 and 9</h1>'\
        "<p><img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif></p>"

genated_number = random.randint(1, 9)

@app.route("/<int:number>")
def guess(number):
    if number < genated_number:
        return '<h1 style = "color: red;" > it\'s too low </h1>'\
'<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif width="500" height="600">'

    if number > genated_number:
        return '<h1 style = "color: red;" > it\'s too high </h1>'\
'<img src = https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif width="500" height="600">'

    else:
        return '<b><h1 style = "color: green;"> bingo </h1></b>'\
'<img src = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif width="500" height="600">'

if __name__ == "__main__":
    app.run(debug=True)