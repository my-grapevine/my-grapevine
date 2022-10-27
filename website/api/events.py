
# THROWS ERROR WHEN DATA BEYOND SIZE OF PAGE IS SEARCHED, NEED TO USE EXCEPTIONAL HANDLING
# API can be changed for UK's events
import requests as req

response = req.get('https://app.ticketmaster.com/discovery/v2/events.json?countryCode=GB&apikey=EONIBa1etvf9rGHGYUPOnHGSfByU0y8S&size=100')
data = response.json()

import requests
from datetime import datetime, timedelta


def get_events():
    next_month = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    data = []
    for page_number in range(1, 3):
        try:
            response = requests.get(f"https://app.ticketmaster.com/discovery/v2/events?countryCode=GB&apikey=EONIBa1etvf9rGHGYUPOnHGSfByU0y8S&endDateTime={next_month}&size=200&page={page_number}")
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
            f"https://app.ticketmaster.com/discovery/v2/events/{event_id}?apikey=EONIBa1etvf9rGHGYUPOnHGSfByU0y8S")
        event = response.json()
        return {
            'id': event['id'],
            'name': event['name'],
            'image_url': event['images'][0]['url'],
            'city': event['_embedded']['venues'][0]['city']['name'],
            'dates': event['dates']['start']['localDate'],
            'venues': event['_embedded']['venues'][0]['name'],
            'classification': event['classifications'][0]['genre']['name'],
            'url': event['_embedded']['venues'][0]['url']
        }
    except (KeyError, requests.exceptions.RequestException):
        return


get_event_by_id('G5dFZ9kR2F7sh')




def get_event_details():
    event_data = []
    for event in data['_embedded']['events']:
        event_id = event['id']
        event_name = event['name']
        address = event['_embedded']['venues'][0]['address']['line1']
        venue = event['_embedded']['venues'][0]['name']
        city = event['_embedded']['venues'][0]['city']['name']
        postal_code = event['_embedded']['venues'][0]['postalCode']
        country = event['_embedded']['venues'][0]['country']['name']
        image = event['images'][0]['url']
        date_event = event['dates']['start']['localDate']

        classification_name = event['classifications'][0]['segment']['name']

        classification_genre_name = event['classifications'][0]['genre']['name']


        if "info" in event:
            event_info = event['info']
        else:
            continue
        currency = event['priceRanges'][0]['currency']
        price_range_min = event['priceRanges'][0]['min']
        price_range_max = event['priceRanges'][0]['max']

        new_event = {
            "event_id": event_id,
            # "venue": venue,
            "name": event_name,
            "location": f"{address}, {venue}, {city}, {postal_code}, {country}",
            "image": image,
            "date_event": date_event,

            "classification_name": classification_name,

            "classification_genre_name": classification_genre_name,

            "info": event_info,
            "currency": currency,
            "price_range_min": price_range_min,
            "price_range_max": price_range_max,

        }
        event_data.append(new_event)
    return event_data

def get_attraction_details():
    attraction_data = []
    for event in data['_embedded']['events']:
        #attraction_id = event['_embedded']['attractions'][0]['id']
        attraction_name = event['_embedded']['attractions'][0]['name']
        attraction_images = event['_embedded']['attractions'][0]['images'][0]['url']
        classification_category = event['_embedded']['attractions'][0]['classifications'][0]['segment']['name']
        upcoming_events = event['_embedded']['attractions'][0]['upcomingEvents']['_total']

        new_attraction = {
            "attraction_id": attraction_id,
            "attraction_name": attraction_name,
            "attraction_images": attraction_images,
            "classification_category": classification_category,
            "upcoming_events": upcoming_events,
            "attraction_fb_url": attraction_fb_url,
            "attraction_instagram_url": attraction_instagram_url
        }

        attraction_data.append(new_attraction)
    return attraction_data


def search():
    #event_search = request.args.get('artist')
    event_search = input('Enter event you want to search: ')
    ticketmaster_url = _generate_ticketmaster_url(event_search)
    response = req.get(ticketmaster_url)
    #print(response.json())
    data = response.json()

    if data['page']['totalElements'] == 0:
        print('No results found!')

    else:

        event_data = []
        for event in data['_embedded']['events']:
            new_event = {
                'name': event['name'],
                'date_event': event['dates']['start']['localDate'],
                'venue': event['_embedded']['venues'][0]['name'],
                'city': event['_embedded']['venues'][0]['city']['name'],
                'postal_code': event['_embedded']['venues'][0]['postalCode'],
                'country': event['_embedded']['venues'][0]['country']['name']
            }
            event_data.append(new_event)
        print(event_data)

        return (event_data)


#API used here is UK API
def _generate_ticketmaster_url(artist):
    modified_artist = artist.replace(' ','%20')
    ticketmaster_key = "EONIBa1etvf9rGHGYUPOnHGSfByU0y8S"
    return f"https://app.ticketmaster.com/discovery/v2/events.json?keyword={ modified_artist }&countryCode=GB&apikey={ ticketmaster_key}&size=120"

#a = search()

#print(get_event_details())