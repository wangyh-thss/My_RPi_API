# encoding=utf-8

import sys
from flask import Flask
from app import views
from app.foundation import csrf

reload(sys)
sys.setdefaultencoding('utf-8')

DEFAULT_APP_NAME = 'app'


def create_app():
    app = Flask(DEFAULT_APP_NAME)
    app.config.from_object('config')
    configure_blueprint(app, views.MODULES)
    # configure_handlers(app)
    configure_csrf(app)
    return app


def configure_handlers(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        pass


def configure_blueprint(app, modules):
    for m in modules:
        if isinstance(m, tuple):
            app.register_blueprint(m[0], url_prefix=m[1])
        else:
            app.register_blueprint(m)


def configure_csrf(app):
    csrf.init_app(app)


app = create_app()

