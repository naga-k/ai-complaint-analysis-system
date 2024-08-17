from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get database URL from environment variable
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}?sslmode=disable'

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello from python!"})

def get_db_connection():
    engine = create_engine(DATABASE_URL)
    return engine.connect()

@app.route('/health')
def health_check():
    try:
        # Attempt to connect to the database and execute a simple query
        with get_db_connection() as connection:
            result = connection.execute(text("SELECT 1"))
            if result.scalar() == 1:
                return jsonify({
                    "status": "healthy",
                    "database": "connected",
                    "message": "Database is responsive"
                }), 200
            else:
                raise SQLAlchemyError("Unexpected query result")
    except SQLAlchemyError as e:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "message": f"Database error: {str(e)}"
        }), 500
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "message": f"Unexpected error: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)