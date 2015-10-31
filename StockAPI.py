__author__ = 'mukesh'
# In this stock data is scrapped from one of the Indian markets website for any particular stock.

import urllib
from bs4 import BeautifulSoup
import re

base_url = 'http://money.rediff.com/companies/'


class StockAPI:

    def __init__(self, symbol):
        self.symbol = symbol

    def get_content(self):
        """
        Returns html content, which is used in other function.
        """
        self.symbol.upper()
        url = base_url+self.symbol
        text = urllib.urlopen(url).read()
        soup = BeautifulSoup(text, "html.parser")
        return soup

    def get_quote(self):
        """
        Returns today's price.
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "ltpid"}).contents[0]
        except AttributeError:
            result = "The symbol you entered is not correct please check and enter again"
        return result

    def get_previous_close(self):
        """
        Return yesterday's close price.
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "PrevClose"}).contents[0]
        except AttributeError:
            result = "The symbol you entered is not correct please check and enter again"
        return result

    def get_percent_change(self):
        """
        This gives percent change in stock price
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "ChangePercent"}).contents[0]
        except AttributeError:
            result = "The symbol you entered is not correct please check and enter again"
        return result

    def get_volume(self):
        """
        This returns volume of stock transaction
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "Volume"}).contents[0]
        except AttributeError:
            result = "The symbol you entered is not correct please check and enter again"
        return result

    def get_todays_high(self):
        """
        This return today's high.
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "highlow"}).contents[0]
            final_result = result.split()
        except AttributeError:
            final_result = "The symbol you entered is not correct please check and enter again"
        return final_result[0]

    def get_todays_low(self):
        """
        This returns today's low.
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "highlow"}).contents[0]
            final_result = result.split()
        except AttributeError:
            final_result = "The symbol you entered is not correct please check and enter again"
        return final_result

    def get_52_week_high(self):
        """
        This returns 52 week high
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
            final_result = result.split()
        except AttributeError:
            final_result = "The symbol you entered is not correct please check and enter again"
        return final_result[0]

    def get_52_week_low(self):
        """
        This returns 52 week low
        """
        soup = self.get_content()
        try:
            result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
            final_result = result.split()
        except AttributeError:
            final_result = "The symbol you entered is not correct please check and enter again"
        return final_result[2]

    def get_Market_cap(self):
        """
        This returns market capital of that stock
        """
        text = self.get_content()
        regex = '<span id="MarketCap" [^.]*>(.+?)</span>'
        pattern = re.compile(regex)
        result = re.findall(pattern, text)
        return result

    def get_summary(self):
        """
        This returns summary of all the today's data related to that stock
        """
        details = {
            'Get_quote': self.get_quote(),
            'Get_previous_close': self.get_previous_close(),
            'Get_percent_change': self.get_percent_change(),
            'Get_volume': self.get_volume(),
            'Get_todays_high': self.get_todays_high(),
            'Get_todays_low': self.get_todays_low(),
        }
        return details

