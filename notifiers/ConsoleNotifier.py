from notifiers.Notifier import Notifier
import logging


class ConsoleNotifier(Notifier):
    def __init__(self):
        self.logger = logging.getLogger('uvicorn.info')
        self.logger.setLevel(logging.INFO)

    def notify(self, message):
        self.logger.info(message)
