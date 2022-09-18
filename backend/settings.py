from dotenv import load_dotenv
import os
load_dotenv()



DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
TEST_DB_NAME = os.getenv('TEST_DB_NAME')
TEST_DB_USER = os.getenv('TEST_DB_USER')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
DATE = os.getenv('DATE')