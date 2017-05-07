import unittest
from market_bot import extract_symbol_from_input, get_stock_data
import pandas as pd
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


unittest.main()
