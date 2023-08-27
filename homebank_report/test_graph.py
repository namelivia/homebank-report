import pytest
from unittest.mock import Mock, patch
import numpy as np

from .graph import generate_evolution_graph
from .options import Options

class TestGenerateEvolutionGraph:
    @patch('homebank_report.graph.plt')
    def test_generate_evolution_graph(self, mock_plt):
        # Set up the mock behavior
        mock_plt.figure.return_value = Mock()
        mock_plt.savefig.return_value = None
        
        account_name = "Test Account"
        options = Options({
             "GRAPHS_PATH": "test_graphs_path",
             "NOTIFICATIONS_SERVICE_ENDPOINT": "notifications_service_endpoint",
             "XML_FILE": "xml_file"
         })
        operations = Mock()
        operations.operations = [Mock(amount=100), Mock(amount=-50), Mock(amount=200)]
        
        # Call the function being tested
        result = generate_evolution_graph(account_name, options, operations)
        
        # Assertions
        assert result != ''
        mock_plt.figure.assert_called_once_with(figsize=(8, 8))
        #TODO: Fix this assertion
        #mock_plt.plot.assert_called_once_with(np.cumsum([100, -50, 200]))
        mock_plt.title.assert_called_once_with(f'{account_name}: Evolución')
        mock_plt.savefig.assert_called_once()
