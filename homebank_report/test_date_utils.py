from datetime import date, timedelta
import pytest
from .date_utils import convert_date_from_homebank_format, convert_date_to_homebank_format

class TestDateConversion:
    def test_convert_date_from_homebank_format(self):
        homebank_date = 365  # Example homebank date value
        expected_date = date(1, 1, 1) + timedelta(days=homebank_date)
        converted_date = convert_date_from_homebank_format(homebank_date)
        assert converted_date == expected_date

    def test_convert_date_to_homebank_format(self):
        input_date = date(1, 2, 15)  # Example input date
        expected_value = (input_date - date(1, 1, 1)).days
        converted_value = convert_date_to_homebank_format(input_date)
        assert converted_value == expected_value
