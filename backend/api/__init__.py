from flask import Flask, jsonify
import psycopg2
from api.models import Venue
from api.lib.orm import find_all, find

def create_app(database, user):
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database,
        DB_USER=user
    )
    @app.route('/')
    def home():
        return 'foursquare api'

    @app.route('/venues')
    def venues():
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['DB_USER'])
        cursor = conn.cursor()
        venues = find_all(Venue, conn)
        venue_objs = [venue.__dict__ for venue in venues]
        return jsonify(venue_objs)

    @app.route('/venues/<id>')
    def show_venue(id):
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['DB_USER'])
        cursor = conn.cursor()
        venue = find(Venue, id, conn)
        return jsonify(venue.__dict__)

    return app