import pytest
from .currency import Currency

class TestCurrency:
    @pytest.fixture
    def sample_currency(self):
        return Currency(
            key=1,
            flags=0,
            iso="USD",
            name="US Dollar",
            symb="$",
            syprf="s",
            dchar=".",
            gchar=",",
            frac=2,
            rate=1.0,
            mdate="2023-01-01"
        )

    def test_initialization(self, sample_currency):
        assert sample_currency.key == 1
        assert sample_currency.flags == 0
        assert sample_currency.iso == "USD"
        assert sample_currency.name == "US Dollar"
        assert sample_currency.symb == "$"
        assert sample_currency.syprf == "s"
        assert sample_currency.dchar == "."
        assert sample_currency.gchar == ","
        assert sample_currency.frac == 2
        assert sample_currency.rate == 1.0
        assert sample_currency.mdate == "2023-01-01"

    def test_str_representation(self, sample_currency):
        expected_str = "Currency: key=1, flags=0, iso=USD, name=US Dollar, symb=$, syprf=s, dchar=., gchar=,, frac=2, rate=1.0, mdate=2023-01-01"
        assert str(sample_currency) == expected_str
