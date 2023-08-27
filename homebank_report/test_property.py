import pytest
from .property import Property

class TestProperty:
    @pytest.fixture
    def sample_property(self):
        return Property(
            title="Sample Property",
            curr="USD",
            auto_smode=True,
            auto_weekday=3
        )

    def test_initialization(self, sample_property):
        assert sample_property.title == "Sample Property"
        assert sample_property.curr == "USD"
        assert sample_property.auto_smode is True
        assert sample_property.auto_weekday == 3

    def test_str_representation(self, sample_property):
        expected_str = "Property: title=Sample Property, curr=USD, auto_smode=True, auto_weekday=3"
        assert str(sample_property) == expected_str
