import random

from website.api.event_manager import EventManager
from website.api.ticketmaster import TicketmasterEventManager
from website.api.eventbrite import EventbriteEventManager
from website.api.art_fund import ArtFundEventManager


class CombinedEventManager(EventManager):

    def __init__(self):
        self.event_managers = {
            'ticketmaster': TicketmasterEventManager(),
            'eventbrite': EventbriteEventManager(),
            'artfund': ArtFundEventManager()
        }

    def get_events(self, query=None):
        events = []
        for event_manager in self.event_managers.values():
            events.extend(event_manager.get_events(query))
        random.shuffle(events)
        return events

    def get_event_by_id(self, event_id):
        source = event_id.split('-', 1)[0]
        event_manager = self.event_managers.get(source)
        if event_manager:
            return event_manager.get_event_by_id(event_id)
