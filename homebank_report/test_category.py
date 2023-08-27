import pytest
from .category import Category

class TestCategory:
    @pytest.fixture
    def sample_category(self):
        return Category(key=1, name="Sample Category")

    def test_initialization(self, sample_category):
        assert sample_category.key == 1
        assert sample_category.name == "Sample Category"

    def test_str_representation(self, sample_category):
        expected_str = "Category: key=1, name=Sample Category"
        assert str(sample_category) == expected_str
