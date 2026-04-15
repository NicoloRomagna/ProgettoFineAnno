import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='nicolò',
        DATABASE=os.path.join(app.instance_path, 'lego.sqlite'),
    )

    from . import main
    app.register_blueprint(main.bp)

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
