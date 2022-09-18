from api.adapters.category_builder import CategoryBuilder
from api.models import Category, Venue, venue_category
from api.lib.db import drop_all_tables, test_conn, test_cursor
from api.lib.orm import save
from decimal import Decimal
import pytest
import psycopg2

response_venue = {'id': '5b2932a0f5e9d70039787cf2', 'name': 'Los Tacos Al Pastor', 'contact': {'phone': '3479160190', 'formattedPhone': '(347) 916-0190'}, 'location': {'address': '141 Front St', 'crossStreet': 'Pearl St', 'lat': 40.70243624175102, 'lng': -73.98753900608666, 'labeledLatLngs': [{'label': 'display', 'lat': 40.70243624175102, 'lng': -73.98753900608666}], 'postalCode': '11201', 'cc': 'US', 'neighborhood': 'DUMBO', 'city': 'New York', 'state': 'NY', 'country': 'United States', 'formattedAddress': ['141 Front St (Pearl St)', 'New York, NY 11201', 'United States']}, 'canonicalUrl': 'https://foursquare.com/v/los-tacos-al-pastor/5b2932a0f5e9d70039787cf2', 
'categories': [{'id': '4bf58dd8d48988d151941735', 'name': 'Taco Place', 'pluralName': 'Taco Places', 'shortName': 'Tacos', 'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/taco_', 'suffix': '.png'}, 'primary': True}, 
{'id': '4bf58dd8d48988d151941735', 'name': 'Quick Bite', 'pluralName': 'Quick Bite', 'shortName': 'Tacos', 'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/taco_', 'suffix': '.png'}, 'primary': True}
],
 'verified': False, 'stats': {'tipCount': 7}, 'url': 'http://lostacosalpastor.com', 'price': {'tier': 1, 'message': 'Cheap', 'currency': '$'}, 'likes': {'count': 53, 'groups': [{'type': 'others', 'count': 53, 'items': []}], 'summary': '53 Likes'}, 'dislike': False, 'ok': False, 'rating': 7.3, 'ratingColor': 'C5DE35', 'ratingSignals': 75, 'delivery': {'id': '857049', 'url': 'https://www.seamless.com/menu/los-tacos-al-pastor-141a-front-st-brooklyn/857049?affiliate=1131&utm_source=foursquare-affiliate-network&utm_medium=affiliate&utm_campaign=1131&utm_content=857049', 'provider': {'name': 'seamless', 'icon': {'prefix': 'https://fastly.4sqi.net/img/general/cap/', 'sizes': [40, 50], 'name': '/delivery_provider_seamless_20180129.png'}}}, 'allowMenuUrlEdit': True, 'beenHere': {'count': 0, 'unconfirmedCount': 0, 'marked': False, 'lastCheckinExpiredAt': 0}, 'specials': {'count': 0, 'items': []}, 'photos': {'count': 25, 'groups': [{'type': 'venue', 'name': 'Venue photos', 'count': 25, 'items': [{'id': '612d22a01925ba00620a0cad', 'createdAt': 1630347936, 'source': {'name': 'Swarm for iOS', 'url': 'https://www.swarmapp.com'}, 'prefix': 'https://fastly.4sqi.net/img/general/', 'suffix': '/16805980_YfuGuyPX7KKzFlaTldLEB_zgMT0G0gOTHWv5z8SM-RU.jpg', 'width': 1440, 'height': 1920, 'visibility': 'public'}]}]}, 'reasons': {'count': 1, 'items': [{'summary': 'Lots of people like this place', 'type': 'general', 'reasonName': 'rawLikesReason'}]}, 'hereNow': {'count': 0, 'summary': 'Nobody here', 'groups': []}, 'createdAt': 1529426592, 'tips': {'count': 7, 'groups': [{'type': 'others', 'name': 'All tips', 'count': 7, 'items': [{'id': '5cedcda5bed4830039f875db', 'createdAt': 1559088549, 'text': 'Imposter of Los Tacos No 1 and nowhere as good.', 'type': 'user', 'canonicalUrl': 'https://foursquare.com/item/5cedcda5bed4830039f875db', 'lang': 'en', 'likes': {'count': 0, 'groups': []}, 'logView': True, 'agreeCount': 4, 'disagreeCount': 2, 'todo': {'count': 0}, 'user': {'firstName': 'Dustin', 'lastName': 'L', 'address': '', 'city': '', 'state': '', 'countryCode': 'US'}}]}]}, 'shortUrl': 'https://4sq.com/2tk1uK3', 'timeZone': 'America/New_York', 'listed': {'count': 34, 'groups': [{'type': 'others', 'name': 'Lists from other people', 'count': 34, 'items': [{'id': '5b3479d3f62f2b002c702e14', 'name': 'New York to try and past loved list', 'description': '', 'type': 'others', 'user': {'firstName': 'Gabor', 'lastName': 'D', 'countryCode': 'US'}, 'editable': False, 'public': True, 'collaborative': False, 'url': '/user/41159744/list/new-york-to-try-and-past-loved-list', 'canonicalUrl': 'https://foursquare.com/user/41159744/list/new-york-to-try-and-past-loved-list', 'createdAt': 1530165715, 'updatedAt': 1642819216, 'photo': {'id': '55f8a719498e6d8c375d6511', 'createdAt': 1442359065, 'prefix': 'https://fastly.4sqi.net/img/general/', 'suffix': '/3023340_rrJcxK8SauFYnQT_TltTGnfylLWI6QQNhchZHPgGpqE.jpg', 'width': 1080, 'height': 1350, 'visibility': 'public'}, 'followers': {'count': 0}, 'listItems': {'count': 198, 'items': [{'id': 'v5b2932a0f5e9d70039787cf2', 'createdAt': 1550438588}]}}, {'id': '5a7fe1ae18d43b3c603a6767', 'name': 'Mexican', 'description': '', 'type': 'others', 'user': {'firstName': 'Brittany', 'lastName': 'G', 'countryCode': 'US'}, 'editable': False, 'public': True, 'collaborative': False, 'url': '/user/372242289/list/mexican', 'canonicalUrl': 'https://foursquare.com/user/372242289/list/mexican', 'createdAt': 1518330286, 'updatedAt': 1574633025, 'photo': {'id': '52796815498edcaf717b7e15', 'createdAt': 1383688213, 'prefix': 'https://fastly.4sqi.net/img/general/', 'suffix': '/2825916_45mHfm2uqrD3VJvvLMdRI7H-ZIflNHvBJsVlbz6uMQI.jpg', 'width': 640, 'height': 640, 'visibility': 'public'}, 'followers': {'count': 0}, 'listItems': {'count': 26, 'items': [{'id': 'v5b2932a0f5e9d70039787cf2', 'createdAt': 1538188767}]}}, {'id': '5a4e3ca1b2958f1507819c88', 'name': 'Places To Go', 'description': '', 'type': 'others', 'user': {'firstName': 'Ben', 'lastName': 'K', 'countryCode': 'US'}, 'editable': False, 'public': True, 'collaborative': False, 'url': '/user/464855082/list/places-to-go', 'canonicalUrl': 'https://foursquare.com/user/464855082/list/places-to-go', 'createdAt': 1515076769, 'updatedAt': 1623458558, 'photo': {'id': '51656f20011c7cf87d42fdf3', 'createdAt': 1365602080, 'prefix': 'https://fastly.4sqi.net/img/general/', 'suffix': '/19824_A-VfUBhfPCkEX7VRdk1_83I3dO5jppuK82rRe6zV_gQ.jpg', 'width': 620, 'height': 465, 'visibility': 'public'}, 'followers': {'count': 0}, 'listItems': {'count': 327, 'items': [{'id': 'v5b2932a0f5e9d70039787cf2', 'createdAt': 1603494788}]}}, {'id': '5bd335ca123a19002cf70afa', 'name': 'New Hood', 'description': '', 'type': 'others', 'user': {'firstName': 'Sandra', 'lastName': 'R', 'countryCode': 'US'}, 'editable': False, 'public': True, 'collaborative': False, 'url': '/sroobs/list/new-hood', 'canonicalUrl': 'https://foursquare.com/sroobs/list/new-hood', 'createdAt': 1540568522, 'updatedAt': 1568063563, 'followers': {'count': 0}, 'listItems': {'count': 48, 'items': [{'id': 'v5b2932a0f5e9d70039787cf2', 'createdAt': 1551246014}]}}]}]}, 'hours': {'status': 'Open until 10:00 PM', 'richStatus': {'entities': [], 'text': 'Open until 10:00 PM'}, 'isOpen': True, 'isLocalHoliday': False, 'dayData': [], 'timeframes': [{'days': 'Mon–Sun', 'includesToday': True, 'open': [{'renderedTime': '9:00 AM–10:00 PM'}], 'segments': []}]}, 'popular': {'status': 'Likely open', 'richStatus': {'entities': [], 'text': 'Likely open'}, 'isOpen': True, 'isLocalHoliday': False, 'timeframes': [{'days': 'Today', 'includesToday': True, 'open': [{'renderedTime': 'Noon–9:00 PM'}], 'segments': []}, {'days': 'Wed', 'open': [{'renderedTime': 'Noon–9:00 PM'}], 'segments': []}, {'days': 'Thu', 'open': [{'renderedTime': 'Noon–4:00 PM'}, {'renderedTime': '6:00 PM–9:00 PM'}], 'segments': []}, {'days': 'Fri', 'open': [{'renderedTime': '11:00 AM–9:00 PM'}], 'segments': []}, {'days': 'Sat', 'open': [{'renderedTime': '1:00 PM–7:00 PM'}], 'segments': []}, {'days': 'Sun', 'open': [{'renderedTime': 'Noon–7:00 PM'}], 'segments': []}, {'days': 'Mon', 'open': [{'renderedTime': 'Noon–9:00 PM'}], 'segments': []}]}, 'seasonalHours': [], 'defaultHours': {'status': 'Open until 10:00 PM', 'richStatus': {'entities': [], 'text': 'Open until 10:00 PM'}, 'isOpen': True, 'isLocalHoliday': False, 'dayData': [], 'timeframes': [{'days': 'Mon–Sun', 'includesToday': True, 'open': [{'renderedTime': '9:00 AM–10:00 PM'}], 'segments': []}]}, 'pageUpdates': {'count': 0, 'items': []}, 'inbox': {'count': 0, 'items': []}, 'attributes': {'groups': [{'type': 'price', 'name': 'Price', 'summary': '$', 'count': 1, 'items': [{'displayName': 'Price', 'displayValue': '$', 'priceTier': 1}]}, {'type': 'payments', 'name': 'Credit Cards', 'summary': 'Credit Cards', 'count': 7, 'items': [{'displayName': 'Credit Cards', 'displayValue': 'Yes'}]}, {'type': 'outdoorSeating', 'name': 'Outdoor Seating', 'summary': 'Outdoor Seating', 'count': 1, 'items': [{'displayName': 'Outdoor Seating', 'displayValue': 'Yes'}]},
 {'type': 'serves', 'name': 'Menus', 'summary': 'Lunch & Dinner', 'count': 8, 'items': [{'displayName': 'Lunch', 'displayValue': 'Lunch'}, {'displayName': 'Dinner', 'displayValue': 'Dinner'}]}]}, 'bestPhoto': {'id': '612d22a01925ba00620a0cad', 'createdAt': 1630347936, 'source': {'name': 'Swarm for iOS', 'url': 'https://www.swarmapp.com'}, 'prefix': 'https://fastly.4sqi.net/img/general/', 'suffix': '/16805980_YfuGuyPX7KKzFlaTldLEB_zgMT0G0gOTHWv5z8SM-RU.jpg', 'width': 1440, 'height': 1920, 'visibility': 'public'}, 'colors': {'highlightColor': {'photoId': '612d22a01925ba00620a0cad', 'value': -10985408}, 'highlightTextColor': {'photoId': '612d22a01925ba00620a0cad', 'value': -1}, 'algoVersion': 3}}

@pytest.fixture()
def conn():
    test_conn = psycopg2.connect(dbname = 'foursquare_test', 
            user = 'postgres', password = 'postgres')
    cursor = test_conn.cursor()
    drop_all_tables(test_conn, cursor)
    yield test_conn
    drop_all_tables(test_conn, cursor)

@pytest.fixture()
def clean_tables():
    drop_all_tables(test_conn, test_cursor)
    yield
    drop_all_tables(test_conn, test_cursor)

def test_initializes_with_the_response_venue(clean_tables):
    builder = CategoryBuilder(response_venue)
    assert isinstance(builder.response_venue, dict) == True
    assert builder.response_venue == response_venue

def test_select_attributes(clean_tables):
    builder = CategoryBuilder(response_venue)
    assert builder.select_attributes() == ['Taco Place', 'Quick Bite']

def test_find_or_create_by_creates_when_new_category(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM categories;')
    begin_cat_num = cursor.fetchone()
    builder = CategoryBuilder({})

    builder.find_or_create_categories(['Taco Places'], conn, cursor)
    cursor.execute('SELECT COUNT(*) FROM categories;')
    end_cat_num = cursor.fetchone()
    assert end_cat_num[0] == begin_cat_num[0] + 1

def test_find_or_create_by_finds_when_existing_category(conn):
    cursor = conn.cursor()
    category = save(Category(name = 'Taco Places'), conn, cursor)
    builder = CategoryBuilder({})
    new_categories = builder.find_or_create_categories(['Taco Places'], conn, cursor)
    assert category.id == new_categories[0].id

def test_creates_venue_categories_to_associate_the_venue_to_the_categories(conn):
    cursor = conn.cursor()
    venue = save(Venue(foursquare_id = '5b2932a0f5e9d70039787cf2',
            name = 'Los Tacos', rating = 5, likes = 20, menu_url = 'foobar.com'), conn, cursor)
    taco_category = save(Category(name = 'Taco Places'), conn, cursor)
    quick_bites_category = save(Category(name = 'Quick Bites'), conn, cursor)
    categories = [taco_category, quick_bites_category]
    builder = CategoryBuilder({})
    builder.create_venue_categories(venue, categories, conn, cursor)
    categories = venue.categories(cursor)
    assert set([category.name 
    for category in categories]) == set(['Quick Bites', 'Taco Places'])
