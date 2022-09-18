from api.models import Venue, VenueCategory, Category
from api.lib.orm import save
from api.lib.db import (drop_records, drop_all_tables, 
test_conn, test_cursor, get_db, close_db)
from api import create_app
import pytest

def build_records(test_conn, test_cursor):
    venue = save(Venue(name='Los Tacos Al Pastor', price = 1, foursquare_id = '1234'), test_conn, test_cursor)
    grimaldis = save(Venue(name='Grimaldis', price = 2, foursquare_id = '4bf58dd8d48988d151941735'), test_conn, test_cursor)
    pizza = save(Category(name='Pizza'), test_conn, test_cursor)
    tourist_spot = save(Category(name='Tourist Spot'), test_conn, test_cursor)
    save(VenueCategory(venue_id = grimaldis.id, category_id = pizza.id), test_conn, test_cursor)
    save(VenueCategory(venue_id = grimaldis.id, category_id = tourist_spot.id), test_conn, test_cursor)


@pytest.fixture()
def clean_tables():
    drop_records(test_cursor, test_conn, 'venues')
    yield
    drop_records(test_cursor, test_conn, 'venues')

@pytest.fixture()
def db_conn():
    flask_app = create_app('foursquare_test', 'postgres')
    flask_app.config['DATABASE'] = 'foursquare_test'

    with flask_app.app_context():
        conn = get_db()
        cursor = conn.cursor()

    drop_all_tables(conn, cursor)
    build_records(conn, cursor)
    yield conn
    with flask_app.app_context():
        close_db()
        conn = get_db()
        cursor = conn.cursor()
        drop_all_tables(conn, cursor)
        close_db()


def test_saves_to_the_db(clean_tables):
        venue = Venue(foursquare_id = '1245', name = 'Los Tacos',
        price = 2, rating = 3.5, likes = 100, menu_url = 'www.foobar.com'
        )
        save(venue, test_conn, test_cursor)
        test_cursor.execute('SELECT * FROM venues ORDER BY id DESC LIMIT 1')
        record = test_cursor.fetchone()
        assert record[1:3] == ('1245', 'Los Tacos')

def test_initialize_with_values_of_foursquare_id_name_rating_likes():
    venue = Venue(foursquare_id = '5b2932a0f5e9d70039787cf2',
            name = 'Los Tacos', rating = 5, likes = 20, menu_url = 'foobar.com')
    assert venue.__dict__ == {'foursquare_id': '5b2932a0f5e9d70039787cf2',
        'name': 'Los Tacos', 'likes': 20, 'menu_url': 'foobar.com', 'rating': 5}

def test_find_by_foursquare_id(db_conn):
    foursquare_id = "4bf58dd8d48988d151941735"
    assert Venue.find_by_foursquare_id(foursquare_id, db_conn).name == 'Grimaldis'

def test_venue_categories(db_conn):
    foursquare_id = "4bf58dd8d48988d151941735"
    grimaldis = Venue.find_by_foursquare_id(foursquare_id, db_conn)
    cursor = db_conn.cursor()
    categories = grimaldis.categories(cursor)
    category_names = [category.name for category in categories]
    assert category_names == ['Pizza', 'Tourist Spot']