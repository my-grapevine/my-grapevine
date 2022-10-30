import os
import requests as req

import requests
from datetime import datetime, timedelta
from flask import Blueprint                                     #Mi

events = Blueprint('events', __name__)                                         #Mi

def get_events():
    next_month = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    data = []
    for page_number in range(1, 3):
        try:
            response = requests.get(
                f"https://app.ticketmaster.com/discovery/v2/events?countryCode=GB&apikey={os.environ.get('API_KEY')}&endDateTime={next_month}&size=200&page={page_number}")
            data.extend(response.json()['_embedded']['events'])
        except (KeyError, requests.exceptions.RequestException):
            break

    image_urls = set()
    events = []
    for event in data:
        is_duplicate = any(image['url'] in image_urls for image in event['images'])
        if not is_duplicate:
            events.append({
                'id': event['id'],
                'name': event['name'],
                'image_url': event['images'][0]['url'],
                'city': event['_embedded']['venues'][0]['city']['name']
            })
            [image_urls.add(image['url']) for image in event['images']]

    return events[:24]

def get_event_by_id(event_id):
    try:
        response = requests.get(
            f"https://app.ticketmaster.com/discovery/v2/events/{event_id}?apikey={os.environ.get('API_KEY')}")
        event = response.json()
        return {
            'id': event['id'],
            'name': event['name'],
            'image_url': event['images'][0]['url'],
            'city': event['_embedded']['venues'][0]['city']['name'],
            'dates': event['dates']['start']['localDate'],
            'venues': event['_embedded']['venues'][0]['name'],
            'classification': event['classifications'][0]['genre']['name'],
            'url': event['url']
        }
    except (KeyError, requests.exceptions.RequestException):
        return


def search(query):
    event_data = []
    try:
        response = req.get(
            f"https://app.ticketmaster.com/discovery/v2/events?keyword={query}&countryCode=GB&apikey={os.environ.get('API_KEY')}&size=24")
        events = response.json()['_embedded']['events']
    except (KeyError, requests.exceptions.RequestException):
        events = []

    for event in events:
        new_event = {
            'id': event['id'],
            'name': event['name'],
            'date_event': event['dates']['start']['localDate'],
            'venue': event['_embedded']['venues'][0]['name'],
            'city': event['_embedded']['venues'][0]['city']['name'],
            'url': event['_embedded']['venues'][0]['url'],
            'image_url': event['images'][0]['url']
        }
        event_data.append(new_event)
    return event_data
