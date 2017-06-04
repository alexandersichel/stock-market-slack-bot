import pandas_datareader.data as web
import datetime
from datetime import timedelta

def get_stock_data(symbol,two_days_prior = True):
    '''input stock ticker as strings, uses it to find stock data from API as dataframe (falls to google if yahoo is down'''
    current_time = datetime.date.today()
    if two_days_prior:
        current_time = datetime.datetime.now() - timedelta(days = 2)
    try:
        return web.DataReader (symbol, "yahoo", current_time, current_time)
    except:
        print ("Yahoo Failed")
        try:
            return web.DataReader (symbol, "google", current_time, current_time)
        except:
            return False

def extract_symbol_from_input(input_message):
    '''takes user inputted string as input and extracts stock symbol as output or none'''
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
    # Inolude ability to run Yahoo and Google Data
    dollar_columns = ['Open','High','Low','Close']
    df[dollar_columns] = df [dollar_columns].apply(lambda num: round(num,2))
    data_dict = df.to_dict()
    clean_string = ''
    for key in data_dict:
        timestamp_dict = data_dict[key]
        timestamp_key = list(timestamp_dict.keys())[0]
        value = str(timestamp_dict [timestamp_key])
        # clean_string += key + ': ' + value +'\n'
        clean_string += '%s: %s\n' %(key,value)
    return clean_string

    print (clean_string)


    # print (data_dict)



def generate_output (input_message):
    symbol = extract_symbol_from_input(input_message)
    if symbol:
        df = get_stock_data(symbol)
        return clean_up_df(df)
    else:
        return "Loser"


