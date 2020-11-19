import json
import logging
from logging.handlers import RotatingFileHandler

# logger settings
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("python_client.log", maxBytes=5 * 1024 * 1024, backupCount=3)
FORMAT = "%(asctime)-15s %(message)s"
fmt = logging.Formatter(FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(fmt)
logger.addHandler(handler)


class Market:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def quotes(self,symbols):
        """
        Calls quotes API to provide quote details for equities, options, and mutual funds

        :param self: Passes authenticated session in parameter
        """
        #symbols = input("\nPlease enter Stock Symbol: ")

        # URL for the API endpoint
        url = self.base_url + "/v1/market/quote/" + symbols + ".json"

        # Make API call for GET request
        response = self.session.get(url)
        logger.debug("Request Header: %s", response.request.headers)

        if response is not None and response.status_code == 200:

            parsed = json.loads(response.text)
            logger.debug("Response Body: %s", json.dumps(parsed, indent=4, sort_keys=True))

            # Handle and parse response
            print("")
            data = response.json()
            if data is not None and "QuoteResponse" in data and "QuoteData" in data["QuoteResponse"]:
                for quote in data["QuoteResponse"]["QuoteData"]:
                    print(quote)
                    
            return data

        else:
            logger.debug("Response Body: %s", response)
            print("Error: Quote API service error")
            return None
