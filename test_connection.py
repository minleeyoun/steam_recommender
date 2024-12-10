from sqlalchemy import create_engine

DATABASE_URL = "postgresql://admin:admin@localhost:5432/steam_recommender_db"
engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
