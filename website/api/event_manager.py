from abc import ABC, abstractmethod


class EventManager(ABC):

    @abstractmethod
    def get_events(self, query=None):
        pass

    @abstractmethod
    def get_event_by_id(self, event_id):
        pass
