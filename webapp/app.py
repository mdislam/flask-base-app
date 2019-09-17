from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
# from api import api
from api import api_blueprint


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config.SWAGGER_UI_JSONEDITOR = True
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    # api.init_app(app)

    return app
