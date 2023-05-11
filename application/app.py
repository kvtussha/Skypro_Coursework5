from flask import Flask
from application.views.main import main_bp
from application.views.choosing import choosing_bp
from application.views.fighting import fighting_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(choosing_bp)
    app.register_blueprint(fighting_bp)
    return app
