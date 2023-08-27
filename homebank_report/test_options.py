import pytest
from .options import Options


class TestOptions():
    def test_getting_configuration_values(self):
        source = {
            "GRAPHS_PATH": "/tmp/graphs",
             "NOTIFICATIONS_SERVICE_ENDPOINT": "notifications_service_endpoint",
            "XML_FILE": "/tmp/xml_file.xml",
        }
        options = Options(source)
        assert options.get("graphs_path") == "/tmp/graphs"
        assert options.get("xml_file") == "/tmp/xml_file.xml"
        assert options.get("notifications_service_endpoint") == "notifications_service_endpoint"
