from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_suspicious(self, request):
        pass

    @abstractmethod
    def notify(self, request):
        pass
