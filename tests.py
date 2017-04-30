import unittest
from market_bot import extract_symbol_from_input
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
unittest.main()