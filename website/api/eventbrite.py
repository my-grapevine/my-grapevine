import requests
import json
from bs4 import BeautifulSoup

from website.api.event import Event
from website.api.event_manager import EventManager


class EventbriteEventManager(EventManager):

    API_URL = "https://www.eventbrite.com/d"

    def get_events(self, query=None):
        try:
            url = f"{self.API_URL}/united-kingdom/events--this-month/"
            if query:
                url += f"{query}/"
            response = requests.get(url)
            html = BeautifulSoup(response.content, 'html.parser')
            event_data = json.loads(str(html.select("[type='application/ld+json']")[0].contents[0]))
            return [Event.from_eventbrite_event(event) for event in event_data]
        except (KeyError, requests.exceptions.RequestException):
            return []

    def get_event_by_id(self, event_id):
        try:
            url = f"{self.API_URL}/united-kingdom/events--this-month/{event_id.split('-', 1)[1]}/"
            response = requests.get(url)
            html = BeautifulSoup(response.content, 'html.parser')
            event_data = json.loads(str(html.select("[type='application/ld+json']")[0].contents[0]))
            return Event.from_eventbrite_event(event_data[0])
        except (KeyError, IndexError, requests.exceptions.RequestException):
            return
