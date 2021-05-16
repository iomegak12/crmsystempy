import json
from flask import Flask
from flask_cors import CORS

from crmsystem.config import GlobalConfiguration
from crmsystem.constants import GlobalConstants
from crmsystem.services import CustomerService
from crmsystem.utilities import CustomerEncoder

configuration = GlobalConfiguration.get_configuration()
flaskApp = Flask(__name__)

CORS(flaskApp)

flaskApp.config["DEBUG"] = int(configuration[GlobalConstants.FLASK_DEBUG])


class CRMSystemApi:
    @staticmethod
    @flaskApp.route("/", methods=["GET"])
    def home():
        return "<h1> CRM System Home </h1>"

    @staticmethod
    @flaskApp.route("/api/v1/customers/", methods=["GET"])
    def get_customers():
        service = CustomerService()
        customerProfiles = service.get_customers()

        return json.dumps(customerProfiles, cls=CustomerEncoder)
