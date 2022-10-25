
# THROWS ERROR WHEN DATA BEYOND SIZE OF PAGE IS SEARCHED, NEED TO USE EXCEPTIONAL HANDLING
# API can be changed for UK's events
import requests as req

response = req.get('https://app.ticketmaster.com/discovery/v2/events.json?countryCode=GB&apikey={'API KEY'}&size=100')
data = response.json()

def get_event_details():
    event_data = []
    for event in data['_embedded']['events']:
        #event_id = event['id']
        event_name = event['name']
        #address = event['_embedded']['venues'][0]['address']['line1']
        venue = event['_embedded']['venues'][0]['name']
        city = event['_embedded']['venues'][0]['city']['name']
        postal_code = event['_embedded']['venues'][0]['postalCode']
        country = event['_embedded']['venues'][0]['country']['name']
        image = event['images'][0]['url']
        date_event = event['dates']['start']['localDate']
        #classification_id = event['classifications'][0]['segment']['id']
        classification_name = event['classifications'][0]['segment']['name']
        #classification_genre_id = event['classifications'][0]['genre']['id']
        classification_genre_name = event['classifications'][0]['genre']['name']
        #classification_subGenre_id = event['classifications'][0]['subGenre']['id']
        #classification_subGenre_name = event['classifications'][0]['subGenre']['name']

        if "info" in event:
            event_info = event['info']
        else:
            continue
        currency = event['priceRanges'][0]['currency']
        price_range_min = event['priceRanges'][0]['min']
        price_range_max = event['priceRanges'][0]['max']
        #seatmap = event['seatmap']['staticUrl']
        #generalRule = event['_embedded']['venues'][0]['generalInfo']['generalRule']
        new_event = {
            "event_id": event_id,
            # "venue": venue,
            "name": event_name,
            "location": f"{address}, {venue}, {city}, {postal_code}, {country}",
            "image": image,
            "date_event": date_event,
            #"classification_id": classification_id,
            "classification_name": classification_name,
            #"classification_genre_id": classification_genre_id,
            "classification_genre_name": classification_genre_name,
           # "classification_subGenre_id": classification_subGenre_id,
            #"classification_subGenre_name": classification_subGenre_name,
            #"info": event_info,
            "info": event_info,
            "currency": currency,
            "price_range_min": price_range_min,
            "price_range_max": price_range_max,
            #"seatmap": seatmap,
            #"generalRule": generalRule,
        }
        event_data.append(new_event)
    return event_data

"""
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

"""
def search():
    #event_search = request.args.get('artist')
    event_search = input('Enter event you want to search: ')
    ticketmaster_url = _generate_ticketmaster_url(event_search)
    response = req.get(ticketmaster_url)
    #print(response.json())
    data = response.json()
    for event in data['_embedded']['events']:
        print(event['name'])
    return event['name']


#API used here is UK API
def _generate_ticketmaster_url(artist):
    modified_artist = artist.replace(' ','%20')
    ticketmaster_key = "{API KEY}"
    return f"https://app.ticketmaster.com/discovery/v2/events.json?keyword={ modified_artist }&countryCode=GB&apikey={ ticketmaster_key}&size=120"

#a = search()

print(get_event_details())
