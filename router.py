from flask import Flask 
from flask import render_template

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template ("index.html")

@app.route("/breakfast")
def breakfast():
	return render_template ("breakfast.html")


@app.route("/lunch")
def lunch():
	return render_template("lunch.html")

@app.route("/dinner")
def dinner():
	return render_template("dinner.html")

app.run()