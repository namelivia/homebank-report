import pytest
from .operation_set import OperationSet
from .operation import Operation

class TestOperationSet:
    @pytest.fixture
    def sample_operations(self):
        operation1 = Operation(date=20230101, amount=100.0, account="Account1", category="Category1")
        operation2 = Operation(date=20230102, amount=-50.0, account="Account2", category="Category2")
        operation3 = Operation(date=20230103, amount=200.0, account="Account3", category="Category1")
        return [operation1, operation2, operation3]

    @pytest.fixture
    def sample_operation_set(self, sample_operations):
        return OperationSet(sample_operations)

    def test_get_balance(self, sample_operation_set):
        assert sample_operation_set.get_balance() == 250.0

    def test_get_operations_for_category(self, sample_operation_set):
        category1_operations = sample_operation_set.get_operations_for_category("Category1")
        assert len(category1_operations) == 2

    def test_get_expenses(self, sample_operation_set):
        expenses_operations = sample_operation_set.get_expenses()
        assert len(expenses_operations) == 1

    def test_get_revenues(self, sample_operation_set):
        revenues_operations = sample_operation_set.get_revenues()
        assert len(revenues_operations) == 2

    def test_get_for_category(self, sample_operation_set):
        category2_operations = sample_operation_set.get_for_category("Category2")
        assert len(category2_operations) == 1

    def test_get_top_10(self, sample_operation_set):
        pass # TODO: Implement this test

