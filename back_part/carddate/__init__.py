from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

import config
db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    
    from . import models

    # 블루프린트
    from .views import main_views, login_views, card_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(login_views.bp)
    app.register_blueprint(card_views.bp)

    return app