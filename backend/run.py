from settings import DB_NAME, DB_USER
from api import create_app
app = create_app(DB_NAME, DB_USER)

app.run(debug = True)