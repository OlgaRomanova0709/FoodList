# import necessary libraries
from flask import (Flask,render_template,jsonify,request,redirect)

from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)

#dishes = []


class Food(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    cuisine = db.Column(db.String(64))
    ingredients = db.Column(db.String(64))

    def __repr__(self):
        return '<Food %r>' % (self.name)

@app.route("/clean_data")
def setup():
    # Recreate database
    db.drop_all()
    db.create_all()
    return "Your data has been cleaned!"


@app.route("/add_data", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        name = request.form["name"]
        cuisine = request.form["cuisine"]
        ingredients = request.form["ingredients"]
        food = Food(name=name, cuisine=cuisine, ingredients=ingredients)
        db.session.add(food)
        db.session.commit()

        return "Your data has been submitted!"
    return render_template("form.html")

@app.route("/delete_data", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        name = request.form["name"]
        db.session.query(Food.name, Food.cuisine, Food.ingredients).filter_by(name=name).delete() 
        db.session.commit()

    return render_template("form2.html")

@app.route("/view_data")
def list_food():
    results = db.session.query(Food.name, Food.cuisine, Food.ingredients).all()
    meal = []
    for result in results:
        meal.append({
            "name": result[0],
            "cuisine": result[1],
            "ingredients": result[2]
        })

    return render_template("index_table.html", meal=meal)

@app.route("/ingredient", methods=["GET", "POST"])
def ingredient():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        results = db.session.query(Food.name, Food.cuisine, Food.ingredients).all()
        meal = []
        for result in results:
            res=result[2].split(",")       
            for i in res:
                if i==ingredient:
                    meal.append({
                        "name": result[0],
                        "cuisine": result[1],
                        "ingredients": result[2]
                    })
        return render_template("index_table.html", meal=meal)
    return render_template("form3.html")

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
