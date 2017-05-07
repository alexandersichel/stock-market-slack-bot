import pandas_datareader.data as web
import datetime
from datetime import timedelta

def get_stock_data(symbol,two_days_prior = True):
    current_time = datetime.date.today()
    if two_days_prior:
        current_time = datetime.datetime.now() - timedelta(days = 2)
    return web.DataReader (symbol, "yahoo", current_time, current_time)
print (get_stock_data("aapl"))

def extract_symbol_from_input(input_message):
    if "stock" in input_message and '#' in input_message:
        hashtag_index = input_message.find('#')
        space_index = input_message[hashtag_index:].find(' ')
        if space_index == -1:
            symbol = input_message[hashtag_index + 1:]
        else:
            symbol = input_message[hashtag_index + 1:hashtag_index + space_index]
        return symbol

def generate_output (input_message):
    symbol = extract_symbol_from_input(input_message)
    if symbol:
        data = get_stock_data(symbol)
        return str(data)
    else:
        return "Loser"


