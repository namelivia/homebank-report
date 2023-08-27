import pytest
from .account import Account

class TestAccount:
    @pytest.fixture
    def sample_account(self):
        return Account(1, 1, 'type', 'USD', 'Sample Account', 1000.0, 0, 2000)

    def test_initialization(self, sample_account):
        assert sample_account.key == 1
        assert sample_account.pos == 1
        assert sample_account.type == 'type'
        assert sample_account.curr == 'USD'
        assert sample_account.name == 'Sample Account'
        assert sample_account.initial == 1000.0
        assert sample_account.minimum == 0
        assert sample_account.maximum == 2000

    def test_get_operation_set_between(self, sample_account):
        # Add test cases for get_operation_set_between
        pass

    def test_str_representation(self, sample_account):
        expected_str = "Account: key=1, pos=1, type=type, curr=USD, name=Sample Account, initial=1000.0, minimum=0, maximum=2000"
        assert str(sample_account) == expected_str

