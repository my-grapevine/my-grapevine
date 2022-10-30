# import requests as req
# from flask import Flask
#import os
#
# app = Flask(__name__)
#
# @app.get("/")
# def home():
#
#     response = req.get(f'https://app.ticketmaster.com/discovery/v2/events.json?apikey={os.environ.get("API_KEY")})
#     data = response.json()
#     event_data = []
#     for event in data['_embedded']['events']:
#         event_id = event['id']
#         event_name = event['name']
#         address = event['_embedded']['venues'][0]['address']['line1']
#         venue = event['_embedded']['venues'][0]['name']
#         city = event['_embedded']['venues'][0]['city']['name']
#         postal_code = event['_embedded']['venues'][0]['postalCode']
#         country = event['_embedded']['venues'][0]['country']['name']
#         image = event['images'][0]['url']
#         date_event = event['dates']['start']['localDate']
#         classification_id = event['classifications'][0]['segment']['id']
#         event_category = event['classifications'][0]['segment']['name']
#         classification_genre_id = event['classifications'][0]['genre']['id']
#         classification_genre_name = event['classifications'][0]['genre']['name']
#         classification_subGenre_id = event['classifications'][0]['subGenre']['id']
#         event_subcategory = event['classifications'][0]['subGenre']['name']
#
#         if "info" in event:
#             event_info = event['info']
#         else:
#             continue
#         currency = event['priceRanges'][0]['currency']
#         price_range_min = event['priceRanges'][0]['min']
#         price_range_max = event['priceRanges'][0]['max']
#         seatmap = event['seatmap']['staticUrl']
#         generalRule = event['_embedded']['venues'][0]['generalInfo']['generalRule']
#         attraction_id = event['_embedded']['attractions'][0]['id']
#         attraction_name = event['_embedded']['attractions'][0]['name']
#         attraction_images = event['_embedded']['attractions'][0]['images'][0]['url']
#         classification_category = event['_embedded']['attractions'][0]['classifications'][0]['segment']['name']
#         upcoming_events = event['_embedded']['attractions'][0]['upcomingEvents']['_total']
#         attraction_fb_url = event['_embedded']['attractions'][0]['externalLinks']['facebook'][0]['url']
#         attraction_instagram_url = event['_embedded']['attractions'][0]['externalLinks']['instagram'][0]['url']
#         new_event = {
#             "event_id": event_id,
#             # "venue": venue,
#             "name": event_name,
#             "location": f"{address}, {venue}, {city}, {postal_code}, {country}",
#             "image": image,
#             "date_event": date_event,
#             "classification_id": classification_id,
#             "event_category": event_category,
#             "classification_genre_id": classification_genre_id,
#             "classification_genre_name": classification_genre_name,
#             "classification_subGenre_id": classification_subGenre_id,
#             "event_subcategory": event_subcategory,
#            # "classification_type_id": classification_type_id,
#             #"classification_type_name": classification_type_name,
#             #"classification_subType_id": classification_subType_id,
#            # "classification_subType_name": classification_subType_name,
#             "info": event_info,
#             "currency": currency,
#             "price_range_min": price_range_min,
#             "price_range_max": price_range_max,
#             "seatmap": seatmap,
#             "generalRule": generalRule,
#             "attraction_id": attraction_id,
#             "attraction_name": attraction_name,
#             "attraction_images": attraction_images,
#             "classification_category": classification_category,
#             "upcoming_events": upcoming_events,
#             "attraction_fb_url": attraction_fb_url,
#             "attraction_instagram_url": attraction_instagram_url
#         }
#         event_data.append(new_event)
#     #print(event_data)
#     return event_data
#     # return data['_embedded']['events']
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)