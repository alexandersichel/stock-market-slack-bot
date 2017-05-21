import pandas_datareader.data as web
import datetime
from datetime import timedelta

def get_stock_data(symbol,two_days_prior = True):
    current_time = datetime.date.today()
    if two_days_prior:
        current_time = datetime.datetime.now() - timedelta(days = 2)
    try:
        return web.DataReader (symbol, "yahoo", current_time, current_time)
    except:
        try:
            return web.DataReader (symbol, "google", current_time, current_time)
        except:
            return False

def extract_symbol_from_input(input_message):
    if "stock" in input_message and '#' in input_message:
        hashtag_index = input_message.find('#')
        space_index = input_message[hashtag_index:].find(' ')
        if space_index == -1:
            symbol = input_message[hashtag_index + 1:]
        else:
            symbol = input_message[hashtag_index + 1:hashtag_index + space_index]
        return symbol

def clean_up_df(df):
# outputs string; price rounds to hundreds; string should look nice
    print(df)
    dollar_columns = ['Open','High','Low','Close','Adj Close']
    df[dollar_columns] = df [dollar_columns].apply(lambda num: round(num,2))


def generate_output (input_message):
    symbol = extract_symbol_from_input(input_message)
    if symbol:
        data = get_stock_data(symbol)
        return str(data)
    else:
        return "Loser"


