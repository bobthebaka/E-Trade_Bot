"""This Python script provides examples on using the E*TRADE API endpoints"""
from __future__ import print_function
import webbrowser
import json
import logging
import configparser
import sys
import requests
from rauth import OAuth1Service
from logging.handlers import RotatingFileHandler
from accounts.accounts import Accounts
from market.market import Market
import time
import pandas as pd
import wx
import wx.xrc

# loading configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# logger settings
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("python_client.log", maxBytes=5*1024*1024, backupCount=3)
FORMAT = "%(asctime)-15s %(message)s"
fmt = logging.Formatter(FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(fmt)
logger.addHandler(handler)


def oauth(self):
    """Allows user authorization for the sample application with OAuth 1"""
    etrade = OAuth1Service(
        name="etrade",
        consumer_key=config["DEFAULT"]["CONSUMER_KEY"],
        consumer_secret=config["DEFAULT"]["CONSUMER_SECRET"],
        request_token_url="https://api.etrade.com/oauth/request_token",
        access_token_url="https://api.etrade.com/oauth/access_token",
        authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
        base_url="https://api.etrade.com")





    base_url = config["DEFAULT"]["SANDBOX_BASE_URL"]


    # Step 1: Get OAuth 1 request token and secret
    request_token, request_token_secret = etrade.get_request_token(
        params={"oauth_callback": "oob", "format": "json"})

    # Step 2: Go through the authentication flow. Login to E*TRADE.
    # After you login, the page will provide a text code to enter.
    authorize_url = etrade.authorize_url.format(etrade.consumer_key, request_token)
    webbrowser.open(authorize_url)

    text_code = ""
    a = wx.TextEntryDialog(self, "Enter ID Code", "E-Trade ID CODE")
    if (a.ShowModal() == wx.ID_OK):
        text_code = a.GetValue()
    else:
        text_code = input("Please accept agreement and enter text code from browser: ")

    # Step 3: Exchange the authorized request token for an authenticated OAuth 1 session
    session = etrade.get_auth_session(request_token,
                                  request_token_secret,
                                  params={"oauth_verifier": text_code})

    main_menu(session, base_url)


def main_menu(session, base_url):
    """
    Provides the different options for the sample application: Market Quotes, Account List

    :param session: authenticated session
    """

    

    userdata =  { "time":["1","2","3","4","5"],
              "price":[1,2,3,4,5],
              "volume":[1.1,2.2,3.3,4.4,5.5]}

    dataFrame = pd.DataFrame(data=userdata)

    print (dataFrame)


    newData = pd.DataFrame(data=[["6",6,6.6],["7",7,7.7]], columns=['time','price','volume'])

    dataFrame = dataFrame.append(newData)

    print(dataFrame)

    dataFrame.to_csv(r'test.csv', index = False)

    loadDataFrame = pd.read_csv(r'test.csv')

    print(loadDataFrame)


    market = Market(session, base_url)

    for i in range(0,100):


        market.quotes("msft,appl")
        time.sleep(.25)



if __name__ == "__main__":
    oauth()
