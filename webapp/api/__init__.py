from flask import Blueprint
from flask_restplus import Api

from app_api import app_ns

api_blueprint = Blueprint('api_blueprint', __name__)

api = Api(api_blueprint,
          version='1.0.0-alpha',
          title='Flask Restplus Blueprint Application',
          doc='/doc',
          description='Documentationf for the Rest API end points',
          contact='Mesbahul Islam',
          contact_email='mesbahul.islam@dreambroker.com')

api.add_namespace(app_ns)