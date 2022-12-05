import os

from flask import Flask, render_template, redirect
from webapp.database import init_db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    # This creates and configures the app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'belongr.db'))

    db = SQLAlchemy(app)
    db.app = app

    if test_config is None:
        # This loads the instance configuration, if it exists, when not testing.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # This loads the test configuration if passed in.
        app.config.from_mapping(test_config)

    # This ensures the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return redirect("index.html")

    from . import application
    app.register_blueprint(application.bp)

    db.init_app(app)

    init_db()

    return app
    