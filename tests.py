import unittest, sys
from market_bot import extract_symbol_from_input, get_stock_data, clean_up_df, generate_output
import pandas as pd
from slack_api import get_websocket_url
# self.assertTime()
# selfassert(False)
# selfassertEqual(,)

class TestSuite(unittest.TestCase):

    def test_extract_symbol(self):
        self.assertFalse(extract_symbol_from_input(''))
        self.assertFalse(extract_symbol_from_input('@hackerteamb1bot give me for #aapl'))
        self.assertEqual(extract_symbol_from_input('@hackerteamb1bot give me stocks for #aapl'),"aapl")
        self.assertFalse(extract_symbol_from_input('random stock hashtag # test'))
        self.assertEqual(extract_symbol_from_input('stock #aapl #ge'), 'aapl')
#       TODO
    def test_get_stock_data(self):
        output_data = get_stock_data('aapl')
        self.assertTrue(isinstance(output_data, pd.DataFrame) )
        self.assertTrue ('Open' in output_data.columns )
    def test_clean_up_df(self):
        df = get_stock_data('aapl')
        clean_up_df(df)
    def test_python_version (self):
        self.assertTrue(sys.version_info.major >= 3)
    def test_generate_output(self):
        print (generate_output("@hackerteambot stock #appl"))



unittest.main(verbosity = True)
