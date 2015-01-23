__author__ = 'mukesh'
#In this stock data is scrapped from money.rediff for any particular stock.

import urllib
import re

base_url = 'http://money.rediff.com/companies/'


def Get_content(symbol):
    """
    Returns html content, which is used in other function.
    """
    html = base_url + symbol
    htmltext = urllib.urlopen(html).read()
    return htmltext

def Get_quote(symbol):
    """
    Returns today's price.
    """
    text = Get_content(symbol)
    regex = '<span id="ltpid" [^.]*>(.+?)</span>'
    pattern = re.compile(regex)
    result = re.findall(pattern, text)
    return result

def Get_previous_close(symbol):
    """
    Return yesterday's close price.
    """
    text = Get_content(symbol)
    regex = '<span id="PrevClose">(.+?)</span>'
    pattern = re.compile(regex)
    result = re.findall(pattern, text)
    return result


def Get_percent_change(symbol):
    """
    This gives percent change in stock price
    """
    todays = Get_quote(symbol)
    todays_data = ''.join(todays)
    previous_close = Get_previous_close(symbol)
    previous_close_data = ''.join(previous_close)
    difference = float(todays_data) - float(previous_close_data)
    change = float(difference)/float(previous_close_data)
    percent_change = change*100
    result = round(percent_change, 2)
    return result

def Get_volume(symbol):
    """
    This returns volume of stock transaction
    """
    text = Get_content(symbol)
    regex = '<span id="Volume">(.+?)</span>'
    pattern = re.compile(regex)
    result = re.findall(pattern, text)
    return result

def high_low_data(symbol):
    """
    This returns high low data which is used in high function  and low function.
    """
    text = Get_content(symbol)
    regex = '<span id="highlow" [^.]*>(.+?)</span>'
    pattern = re.compile(regex)
    data = re.findall(pattern, text)
    string = ''.join(data)
    only_digits = re.sub(r'\D', ' ', string)
    list = ' '.join(only_digits.split())
    result = list.split(' ')
    return result


def Get_todays_high(symbol):
    """
    This return today's high.
    """
    data = high_low_data(symbol)
    list = data[0:2]
    result = '.'.join(list)
    return result

def Get_todays_low(symbol):
    """
    This returns today's low.
    """
    data = high_low_data(symbol)
    list = data[2:4]
    result = '.'.join(list)
    return result


def Fifty_Two_high_low_data(symbol):
    """
    This returns high low data which is used in fifty two week high and low function.
    """
    text = Get_content(symbol)
    regex = '<span id="FiftyTwoHighlow" [^.]*>(.+?)</span>'
    pattern = re.compile(regex)
    data = re.findall(pattern, text)
    string = ''.join(data)
    only_digits = re.sub(r'\D', ' ', string)
    list = ' '.join(only_digits.split())
    result = list.split(' ')
    return result

def Get_Fifty_two_week_high(symbol):
    """
    This returns fifty two week high. 
    """
    data = Fifty_Two_high_low_data(symbol)
    list = data[0:2]
    result = '.'.join(list)
    return result

def Get_Fifty_two_week_low(symbol):
    """
    This return fifty two week low.
    """
    data = Fifty_Two_high_low_data(symbol)
    list = data[2:4]
    result = '.'.join(list)
    return result

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

