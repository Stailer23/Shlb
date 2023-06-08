from os import environ
from dotenv import load_dotenv
load_dotenv()
DB_USER = environ.get('POSTGRES_USER')
DB_PORT = environ.get('DB_PORT')
DB_PASS = environ.get('POSTGRES_PASSWORD')
DB_HOST = environ.get('DB_HOST')
DB_NAME = environ.get('POSTGRES_DB')

REAL_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TEST_DATABASE_URL = "postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5010/postgres_test"