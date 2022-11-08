import os
import requests
from datetime import datetime, timedelta

from website.api.event import Event
from website.api.event_manager import EventManager


class TicketmasterEventManager(EventManager):

    API_URL = "https://app.ticketmaster.com/discovery/v2/events"
    API_KEY = os.environ.get('TICKETMASTER_API_KEY')

    def get_events(self, query=None):
        next_month = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

        data = []
        for page_number in range(1, 4):
            try:
                url = f"{self.API_URL}?countryCode=GB&apikey={self.API_KEY}&endDateTime={next_month}&size=200&page={page_number}"
                if query:
                    url += f"&keyword={query}"
                response = requests.get(url)
                data.extend(response.json()['_embedded']['events'])
            except (KeyError, requests.exceptions.RequestException):
                break

        image_urls = set()
        events = []
        for event in data:
            is_duplicate = any(image['url'] in image_urls for image in event['images'])
            if not is_duplicate and 'location' in event['_embedded']['venues'][0]:
                events.append(Event.from_ticketmaster_event(event))
                [image_urls.add(image['url']) for image in event['images']]

        return events[:24]

    def get_event_by_id(self, event_id):
        try:
            url = f"{self.API_URL}/{event_id.split('-', 1)[1]}?apikey={self.API_KEY}"
            response = requests.get(url)
            event = response.json()
            return Event.from_ticketmaster_event(event)
        except (KeyError, requests.exceptions.RequestException):
            return


