from notifiers.Notifier import Notifier
import logging

FILE_ERROR = "Error writing to file."


class FileNotifier(Notifier):
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = logging.getLogger('uvicorn.error')
        self.logger.setLevel(logging.ERROR)

    def notify(self, message):
        try:
            with open(self.file_path, "a+") as file:
                file.write(message + "\n")
        except Exception:
            self.logger.error(FILE_ERROR)
