import pytest
from unittest.mock import patch, mock_open
from .options import Options


class TestOptions():
    def test_getting_configuration_values(self):
        source = {
            "GRAPHS_PATH": "/tmp/graphs",
            "NOTIFICATIONS_CONFIG_FILE": "/tmp/notifications.yml",
            "XML_FILE": "/tmp/xml_file.xml",
        }
        yaml_file_contents = """
        accounts:
            - account: "account1"
              endpoint: "endpoint1"
            - account: "account2"
              endpoint: "endpoint2"
        """
        with patch("builtins.open", mock_open(read_data=yaml_file_contents)) as mock_file:
            options = Options(source)
        assert options.get("graphs_path") == "/tmp/graphs"
        assert options.get("xml_file") == "/tmp/xml_file.xml"
        assert options.get("notifications_config_file") == "/tmp/notifications.yml"
        assert options.get("notifications")["account1"] == "endpoint1"

