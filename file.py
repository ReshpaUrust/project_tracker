from sqlalchemy import create_engine

DB_USER = 'student_web_2024'
DB_PASSWORD = 'qwerty1234'
DB_HOST = 'dc-webdev.bmstu.ru'
DB_PORT = '8080'
DB_NAME = 'hotel'

db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(db_url)

connection = engine.connect()

print(connection)