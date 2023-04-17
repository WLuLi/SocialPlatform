from flask import Flask
from flask_cors import CORS
from app.config import configs
from app.extensions.extensions import db
from app.functions.operate import operate_bp

def create_app(config_name=None):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(configs[config_name])

    app.register_blueprint(operate_bp, url_prefix="/operate")

    db.init_app(app)
    
    return app