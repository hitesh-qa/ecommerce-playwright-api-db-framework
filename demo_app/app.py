from flask import Flask, render_template, request, jsonify, redirect, url_for
import db

app = Flask(__name__)
DEMO_USER_ID = 1 #seeded via seed_data.sql (we'll build that next)

@app.route("/")
def index():
    products = db.get_all_products()
    return render_template("index.html", products=products)
