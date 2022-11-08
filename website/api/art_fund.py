import requests
from datetime import date, timedelta

from website.api.event import Event
from website.api.event_manager import EventManager


class ArtFundEventManager(EventManager):

    API_URL = "https://gears.artfund.org/search"

    def get_events(self, query=None):
        today = date.today().strftime("%Y-%m-%d")
        next_month = (date.today() + timedelta(days=30)).strftime("%Y-%m-%d")
        try:
            url = f"{self.API_URL}?contentTypes[]=museums&contentTypes[]=exhibitions&contentTypes[]=events&sort=&filter=contentChannels%3Dhas%3Dweb%3BstartDate%3Dlte%3D{today}%3BendDate%3Dgte%3D{next_month}%3B&limit=20&offset=0"
            if query:
                url += f"&search={query}"
            response = requests.get(url)
            event_data = response.json()['data']
            return [Event.from_art_fund_event(event) for event in event_data if 'image' in event['attributes'] and 'location' in event['attributes']['museum']]
        except (KeyError, requests.exceptions.RequestException):
            return []

    def get_event_by_id(self, event_id):
        today = date.today().strftime("%Y-%m-%d")
        next_month = (date.today() + timedelta(days=30)).strftime("%Y-%m-%d")
        try:
            url = f"{self.API_URL}?contentTypes[]=museums&contentTypes[]=exhibitions&contentTypes[]=events&sort=&filter=contentChannels%3Dhas%3Dweb%3BstartDate%3Dlte%3D{today}%3BendDate%3Dgte%3D{next_month}%3B&limit=20&offset=0"
            url += f"&search={event_id.split('-', 1)[1]}"
            response = requests.get(url)
            return Event.from_art_fund_event(response.json()['data'][0])
        except (KeyError, IndexError, requests.exceptions.RequestException):
            return

