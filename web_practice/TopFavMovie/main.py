from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.exc import IntegrityError
from fav_movies_data import movies_data


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()




with app.app_context():
    for movie_data in movies_data:
        movie = Movie(
            title=movie_data["title"],
            year=movie_data["year"],
            description=movie_data["description"],
            rating=movie_data["rating"],
            ranking=movie_data["ranking"],
            review=movie_data["review"],
            img_url=movie_data["img_url"]
        )
        db.session.add(movie)
    
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print(f"Movie {movie.title} already exist in the database.")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() #convert to list
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

class RateForm(FlaskForm):
    rating = StringField("Your Rating Out of 10")
    submit = SubmitField("Done")

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


    



if __name__ == '__main__':
    app.run(debug=True)