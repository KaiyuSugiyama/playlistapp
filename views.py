"""Views in MVC has responsibility for establishing routes and rendering HTML"""
import os
import random
import requests
import json
from flask import g, jsonify, flash
from flask import render_template, request, redirect, url_for, session, Flask, Response
from model import Playlist 
from model import db, db_init

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from BlueprintsIndividual.sample_bp import kpop, jpop
# from BlueprintsIndividual.api_view import api
from BlueprintsIndividual.charlie import cz
from view.komay.app import ks
from view.chris.app import chris_bp
from view.api.app import api
from BlueprintsIndividual.devam import ds
from BlueprintsIndividual.eshaan import ep


with open('config.json') as file:
    config = json.load(file)
    print(config)
with open('backgrounds.json') as file:
    backgroundJSON = json.load(file)
    print(backgroundJSON)

app = Flask(__name__)

app.register_blueprint(kpop, url_prefix="/kpop")
app.register_blueprint(jpop, url_prefix="/jpop")
app.register_blueprint(api)
app.register_blueprint(cz)
app.register_blueprint(ks)
app.register_blueprint(chris_bp, url_prefix='/cr')
app.register_blueprint(ds)
app.register_blueprint(ep)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db_init(app)

# backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]
backgrounds = backgroundJSON['backgrounds']

pathForImages='./images/'
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/')
def index():
    background = random.choice(backgrounds)
    return render_template("index.html", background=background, websiteurl=config['websiteURL'])

@app.route('/bootstrap')
def bootstrap():
    return render_template('Bootstrap_login_example.html')


"""our own project dstufsuf as"""

@app.route('/project')
def project():
    return render_template("homesite/project.html", background=random.choice(backgrounds))

@app.route('/about')
def about():
    return render_template("aboutus.html")
@app.route('/about2')
def about2():
    return render_template("about.html")


@app.route('/browse')
def browse():
    backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/818606015494094868/812382.png"]
    review_query = Review.query.all()
    reviews = []

    for review in review_query:
        websiteurl = url_for('get_img', id=review.id)

        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'satisfaction': review.satisfaction,
            'image':  websiteurl
        }
        reviews.append(review_dict)
    return render_template("homesite/browse.html", reviews=reviews, background=random.choice(backgrounds))


@app.route('/easteregg/crossover')
def crossover():
    return render_template("easteregg/crossover.html")

@app.route('/submit', methods=["POST", 'GET'])
def submit():
    background = random.choice(backgrounds)
    if request.method == "POST":
        playlistname = request.form["playlistname"]
        if playlistname == "CURE":
            return render_template('EaEggLabNav.html')
        username = request.form["username"]
        if username == "mort":
            return render_template('aboutus.html')
        url = request.form["url"]
        submit = Playlist(playlistname=playlistname, username=username, url=url)
        db.session.add(submit)
        db.session.commit()

    return render_template("submit.html", background=background)




@app.route('/images/<int:id>')
def get_img(id):
    img = Review.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 200

    return Response(img.img, mimetype=img.mimetype)


"""
@app.route('/profile/<int:id>')
def profile(id):
    img = 2
    return render_template("homesite/profile.html", name=current_user.name)
"""

