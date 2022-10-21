import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin

class TestExchangeRates(TestCase):

    @patch('bitcoin.request_rates')
    def test_dollars_to_target(self, mock_rates):
        mock_rate = .2342   # Any number will do.  
        # As long as the JSON contains the data the program needs, it does not need to be a complete response
        example_api_response = {'base': 'USD', 'date': '2019-02-04', 'rates': {'BITCOIN': mock_rate}}  
        mock_rates.side_effect = [ example_api_response ] 
        # 100 dollars is 1234.567 Euros at this made up exchange rate 
        converted = bitcoin.convert_dollars_to_target(100, 'BITCOIN')
        self.assertEqual(1234.567, converted)


    # Alternative test - patch the requests's libraries json() method
    # Which one do you prefer?
    @patch('requests.Response.json')
    def test_dollars_to_target_2(self, mock_requests_json):
        mock_rate = 123.4567
        example_api_response = {"rates":{"ETHEREUM": mock_rate},"base":"USD","date":"2020-10-02"}
        mock_requests_json.return_value = example_api_response
        converted = bitcoin.convert_dollars_to_target(100, 'ETHEREUM')
        expected = 12345.67
        self.assertEqual(expected, converted)

    # todo - test error conditions 
    # Currency symbol is not found,
    # Dollar value is not a number,
    # Connection errors to exchange rate API,
    # what else?


if __name__ == '__main__':
    unittest.main()
