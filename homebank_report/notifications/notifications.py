import os
import requests
import logging

logger = logging.getLogger(__name__)


class Notifications:
    @staticmethod
    def send(options, message: str):
        logger.info("Sending notifications")
        data = {"body": message}
        response = requests.post(
            url=options.get("notifications_service_endpoint"), json=data
        )
        logger.info(response.text)
