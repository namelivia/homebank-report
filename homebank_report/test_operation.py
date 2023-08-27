import pytest
from .operation import Operation

class TestOperation:
    @pytest.fixture
    def sample_operation(self):
        return Operation(
            date=20230101,
            amount=100.0,
            account="Sample Account",
            category="Sample Category",
            flags="flags",
            wording="Sample Wording",
            info="Sample Info"
        )

    def test_initialization(self, sample_operation):
        assert sample_operation.date == 20230101
        assert sample_operation.amount == 100.0
        assert sample_operation.account == "Sample Account"
        assert sample_operation.category == "Sample Category"
        assert sample_operation.flags == "flags"
        assert sample_operation.wording == "Sample Wording"
        assert sample_operation.info == "Sample Info"

    def test_str_representation(self, sample_operation):
        expected_str = "Operation: date=20230101, amount=100.0, account=Sample Account, category=Sample Category, flags=flags, wording=Sample Wording, info=Sample Info"
        assert str(sample_operation) == expected_str
