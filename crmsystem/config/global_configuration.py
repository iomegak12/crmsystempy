import os

from crmsystem.models import CRMSystemError
from crmsystem.utilities import ErrorProvider
from crmsystem.constants import GlobalConstants

ERRORS = [
    {"errorKey": 1, "errorId": "GLOCONF001",
        "errorMessage": "Invalid Customer Service URL Specified!"},
]


class GlobalConfiguration:
    configuration = {}

    @staticmethod
    def get_configuration():
        isConfigurationNotNull = GlobalConfiguration.configuration is not None
        configurationLength = GlobalConfiguration.configuration.__len__()

        if isConfigurationNotNull and configurationLength > 0:
            return GlobalConfiguration.configuration

        customerServiceUrl = os.environ.get(
            GlobalConstants.CUSTOMER_SERVICE_URL, None)

        if customerServiceUrl is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        GlobalConfiguration.configuration[GlobalConstants.CUSTOMER_SERVICE_URL] = customerServiceUrl

        flaskDebug = os.environ.get(GlobalConstants.FLASK_DEBUG, "0")
        GlobalConfiguration.configuration[GlobalConstants.FLASK_DEBUG] = flaskDebug

        return GlobalConfiguration.configuration
