from unittest.mock import Mock, patch
from .notifications import Notifications
from homebank_report.options import Options


class TestNotifications:
    @patch("homebank_report.notifications.notifications.requests")
    def test_sending_a_notification(self, m_requests):
        options = Options({
             "GRAPHS_PATH": "test_graphs_path",
             "NOTIFICATIONS_SERVICE_ENDPOINT": "notifications_service_endpoint",
             "XML_FILE": "xml_file"
         })
        notification = "some_notification"
        Notifications.send(options, notification)
        m_requests.post.assert_called_once_with(
            url="notifications_service_endpoint",
            json={"body": "some_notification"},
        )
