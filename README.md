# StockAPI
This is API you can use for dowloading data related to Indian stocks.

This script scraps data from rediff's money website, which hosts data related to India stocks.

To use this you must have Python 2.x.

Place this StockAPI.py file in program directory.
 
# Example 1.

    import StockAPI as stock
   
    print stock.Get_summary('TATAMOTOR')
   
    Output:
    {'Get_percent_change': 3.81,
    'Get_quote': ['587.90'],
    'Get_volume': ['639,605'],
    'Get_todays_low': '573.50',
    'Get_todays_high': '590.75', 
    'Get_previous_close': ['566.30']}
   
# Example 2.
    import StockAPI as stock
   
    print stock.Get_todays_high('TATAMOTOR')
   
    Output:
    '590.75'
   
   

