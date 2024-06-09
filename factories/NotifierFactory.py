from configuration import LOGS_PATH
from notifiers.ConsoleNotifier import ConsoleNotifier

from notifiers.FileNotifier import FileNotifier

FILE_NOTIFY_TYPE = "file"


class NotifierFactory():
    notifier = None

    @staticmethod
    def get_notifier(notifierType):
        if notifierType == FILE_NOTIFY_TYPE:
            if NotifierFactory.notifier is None:
                NotifierFactory.notifier = FileNotifier(LOGS_PATH)
            return NotifierFactory.notifier
        else:
            if NotifierFactory.notifier is None:  # the console will serve as the default notifier
                NotifierFactory.notifier = ConsoleNotifier()
            return NotifierFactory.notifier
