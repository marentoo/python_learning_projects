from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


this_year = datetime.datetime.today().strftime("%Y")
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html",num=random_number, year=this_year)

@app.route('/guest/<name>')
def fun(name):
    url_gender = f"https://api.genderize.io?name={name}"
    data_gender = requests.get(url_gender)
    gender_respond = data_gender.json()
    url_agify = f"https://api.agify.io?name={name}"
    data_age = requests.get(url_agify)
    age_respond = data_age.json()
    return render_template("guest.html", guest_name = name, age = age_respond['age'], gender = gender_respond['gender'])


@app.route('/blog')
def blog():
    url_npoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url_npoint)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)



if __name__ == "__main__":
    app.run(debug=True)


