import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin


class TestBitCoin(TestCase):

    @patch('bitcoin.get_b_data')
    def test_convert_dollars(self, mock_bitcoin_api):

        mock_bitcoin_api.return_value = {"time":{"updated":"Nov 19, 2020 22:00:00 UTC",
            "updatedISO":"2020-11-19T22:00:00+00:00",
            "updateduk":"Nov 19, 2020 at 22:00 GMT"},
            "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin",
            "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"17,962.7805","description":"United States Dollar","rate_float":17962.7805},
            "GBP":{"code":"GBP","symbol":"&pound;","rate":"13,532.0990","description":"British Pound Sterling","rate_float":13532.099},
            "EUR":{"code":"EUR","symbol":"&euro;","rate":"15,121.6075","description":"Euro","rate_float":15121.6075}}}


        expected_dollars = 1796278.05
        dollars = bitcoin.convert_b_to_d(100)
        self.assertEqual(expected_dollars, dollars)


if __name__ == '__main__':
    unittest.main()