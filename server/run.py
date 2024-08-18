import os
from app import create_app
from flask_cors import CORS

# from .app.extensions import init_extensions

config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)
CORS(app, resources={r"/complaint/*": {"origins": "http://localhost:3000"}})
# init_extensions()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, use_reloader=True)