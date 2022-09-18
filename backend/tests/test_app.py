import pytest
from flask import json
from api import create_app
from api.models.venue import Venue
from api.lib.db import drop_records, get_db, close_db
from api.lib.orm import save


@pytest.fixture(scope = 'module')
def app():
    flask_app = create_app('foursquare_test', 'postgres')

    with flask_app.app_context():
        conn = get_db()
        cursor = conn.cursor()
        drop_records(cursor, conn, 'venues')
        drop_records(cursor, conn, 'categories')
        build_records(conn, cursor)

        conn.commit()
        close_db()
    yield flask_app

    with flask_app.app_context():
        close_db()
        conn = get_db()
        cursor = conn.cursor()
        drop_records(cursor, conn, 'venues')
        drop_records(cursor, conn, 'categories')
        close_db()


def build_records(conn, cursor):
    famiglia = Venue(foursquare_id = '1234', name = 'La Famiglia', price = 1,
            rating = 2, likes = 3, menu_url = 'lafamig.com')
    mogador = Venue(foursquare_id = '5678', name = 'Cafe Mogador', 
            price = 3, rating = 4, likes = 15, menu_url = 'cafemogador.com')
    save(famiglia, conn, cursor)
    save(mogador, conn, cursor)
    

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_root_url(app, client):
    response = client.get('/')
    assert b'foursquare api' in response.data

def test_restaurants_index(app, client):
    response = client.get('/venues')
    json_response = json.loads(response.data)

    assert len(json_response) == 2
    
    assert json_response[0]['name'] == 'La Famiglia'
    assert json_response[1]['name'] == 'Cafe Mogador'
    assert set(json_response[0].keys()) == set(['id', 'foursquare_id', 'name', 'price',
     'rating', 'likes', 'menu_url'])

def test_restaurants_show(app, client):
    with app.app_context():
        conn = get_db()
        cursor = conn.cursor()
    
    cursor.execute('select * from venues order by id desc limit 1;')
    last_venue_id = cursor.fetchone()[0]
    
    response = client.get(f'/venues/{last_venue_id}')
    json_response = json.loads(response.data)
    last_record_id = json_response['id'] == last_venue_id