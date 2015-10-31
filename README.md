# StockAPI
This is API you can use for fetching data related to Indian stocks.

This script scraps data from one of the Indian financial website, which hosts data related to Indian stocks.

To use this you must have Python 2.x.

Place this StockAPI.py file in program directory.
 
# Example 1.

    from StockAPI import StockAPI

    stock = StockAPI("TATAMOTOR")
    summary = stock.get_summary()
    print(summary)
   
    Output:
    {'Get_percent_change': 3.81,
    'Get_quote': ['587.90'],
    'Get_volume': ['639,605'],
    'Get_todays_low': '573.50',
    'Get_todays_high': '590.75', 
    'Get_previous_close': ['566.30']}
   
# Example 2.
    from StockAPI import StockAPI

    stock = StockAPI("TCS")
    price = stock.get_quote()
    print(price)

   
    Output:
    '2497.30'
   
   

