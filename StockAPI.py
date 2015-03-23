__author__ = 'mukesh'
# In this stock data is scrapped from money.rediff for any particular stock.

import urllib
from bs4 import BeautifulSoup

base_url = 'http://money.rediff.com/companies/'


def Get_content(symbol):
    """
    Returns html content, which is used in other function.
    """
    symbol.upper()
    url = base_url+symbol
    text = urllib.urlopen(url).read()
    soup = BeautifulSoup(text)
    return soup

def Get_quote(symbol):
    """
    Returns today's price.
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "ltpid"}).contents[0]
    except AttributeError:
        result = "The symbol you entered is not correct please check and enter again"
    return result

def Get_previous_close(symbol):
    """
    Return yesterday's close price.
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "PrevClose"}).contents[0]
    except AttributeError:
        result = "The symbol you entered is not correct please check and enter again"
    return result


def Get_percent_change(symbol):
    """
    This gives percent change in stock price
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "ChangePercent"}).contents[0]
    except AttributeError:
        result = "The symbol you entered is not correct please check and enter again"
    return result


def Get_volume(symbol):
    """
    This returns volume of stock transaction
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "Volume"}).contents[0]
    except AttributeError:
        result = "The symbol you entered is not correct please check and enter again"
    return result


def Get_todays_high(symbol):
    """
    This return today's high.
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "highlow"}).contents[0]
        final_result = result.split()
    except AttributeError:
        final_result = "The symbol you entered is not correct please check and enter again"
    return final_result[0]


def Get_todays_low(symbol):
    """
    This returns today's low.
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "highlow"}).contents[0]
        final_result = result.split()
    except AttributeError:
        final_result = "The symbol you entered is not correct please check and enter again"
    return final_result


def Get_52_week_high(symbol):
    """
    This returns 52 week high
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
        final_result = result.split()
    except AttributeError:
        final_result = "The symbol you entered is not correct please check and enter again"
    return final_result[0]

def Get_52_week_low(symbol):
    """
    This returns 52 week low
    """
    soup = Get_content(symbol)
    try:
        result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
        final_result = result.split()
    except AttributeError:
        final_result = "The symbol you entered is not correct please check and enter again"
    return final_result[2]


def Get_Market_cap(symbol):
    """
    This returns market capital of that stock
    """
    text = Get_content(symbol)
    regex = '<span id="MarketCap" [^.]*>(.+?)</span>'
    pattern = re.compile(regex)
    result = re.findall(pattern, text)
    return result

def Get_summary(symbol):
    """
    This returns summary of all the today's data related to that stock
    """
    dict = {
        'Get_quote': Get_quote(symbol),
        'Get_previous_close': Get_previous_close(symbol),
        'Get_percent_change': Get_percent_change(symbol),
        'Get_volume': Get_volume(symbol),
        'Get_todays_high': Get_todays_high(symbol),
        'Get_todays_low': Get_todays_low(symbol),
    }
    return dict

