from flask import Flask
from .routes import tmp
def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.Config')

    app.register_blueprint(tmp.bp)
    return app