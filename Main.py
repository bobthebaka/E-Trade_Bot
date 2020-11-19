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
import wx
import wx.xrc
import EtradeWindowAbstract


class mainFrame(EtradeWindowAbstract.MyFrame1):



    def __init__(self, parent):
        EtradeWindowAbstract.MyFrame1.__init__(self, parent)
        # loading configuration file
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        # logger settings
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler("python_client.log", maxBytes=5 * 1024 * 1024, backupCount=3)
        self.FORMAT = "%(asctime)-15s %(message)s"
        self.fmt = logging.Formatter(self.FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
        self.handler.setFormatter(self.fmt)
        self.logger.addHandler(self.handler)
        self.session = None
        self.run = False

    # Virtual event handlers, overide them in your derived class

    def Connect_Click(self, event):
       self.oauth()


    def Do_Run_Click(self, event):
        if self.session != None:
            self.run = True

    def oauth(self):
        """Allows user authorization for the sample application with OAuth 1"""
        etrade = OAuth1Service(
            name="etrade",
            consumer_key=self.config["DEFAULT"]["CONSUMER_KEY"],
            consumer_secret=self.config["DEFAULT"]["CONSUMER_SECRET"],
            request_token_url="https://api.etrade.com/oauth/request_token",
            access_token_url="https://api.etrade.com/oauth/access_token",
            authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
            base_url="https://api.etrade.com")

        self.base_url = self.config["DEFAULT"]["SANDBOX_BASE_URL"]

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
        self.session = etrade.get_auth_session(request_token,
                                          request_token_secret,
                                          params={"oauth_verifier": text_code})

        self.market = Market(self.session, self.base_url)

    def TimerTick(self, event):
        if self.run == True:
            self.market.quotes("msft,appl")

if __name__ == "__main__":
    app = wx.App()
    window = mainFrame(None)

    window.Show(True)
    app.MainLoop()