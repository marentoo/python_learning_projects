from flask import Flask, render_template
import requests
from post import Post

url = "https://api.npoint.io/c790b4d5cab58020d391"
respond = requests.get(url)
all_posts = respond.json()

posts = []

for post in all_posts:
    post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts.append(post)

app = Flask(__name__)

@app.route('/')
def get_posts():
    return render_template("index.html", all_posts = posts )

@app.route('/post/<int:i>')
def show_post(i):
    requested_post = None
    for blog_post in posts:
        if blog_post.id == i:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
