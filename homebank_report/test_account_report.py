import pytest
from .account_report import AccountReport

class TestAccountReport:
    @pytest.fixture
    def sample_report(self):
        return AccountReport(
            name="Sample Report",
            balance=1000.0,
            expenses_graph_path="expenses.png",
            revenue_graph_path="revenue.png",
            evolution_graph_path="evolution.png"
        )

    def test_initialization(self, sample_report):
        assert sample_report.name == "Sample Report"
        assert sample_report.balance == 1000.0
        assert sample_report.expenses_graph_path == "expenses.png"
        assert sample_report.revenue_graph_path == "revenue.png"
        assert sample_report.evolution_graph_path == "evolution.png"

    def test_str_representation(self, sample_report):
        expected_str = "AccountReport: name=Sample Report, balance=1000.0, expenses_graph_path=expenses.png, revenue_graph_path=revenue.png, evolution_graph_path=evolution.png"
        assert str(sample_report) == expected_str
