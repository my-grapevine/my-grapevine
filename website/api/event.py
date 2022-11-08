import os


class Event:

    def __init__(self, id, name, image_url, external_url, venue, city, latitude, longitude, start_date, end_date=None, genre=None, description=None):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.external_url = external_url
        self.venue = venue
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.start_date = start_date
        self.end_date = end_date
        self.genre = genre
        self.description = description



    @property
    def google_map_url(self):
        if not self.latitude or not self.longitude:
            return None
        else:
            return f"https://www.google.com/maps/embed/v1/place?key={os.environ.get('GOOGLE_MAPS_KEY')}&q={self.latitude},{self.longitude}&zoom=18"

    @classmethod
    def from_ticketmaster_event(cls, event):
        return cls(
            id=f"ticketmaster-{event['id']}",
            name=event['name'],
            image_url=event['images'][0]['url'],
            external_url=event['url'],
            venue=event['_embedded']['venues'][0]['name'],
            city=event['_embedded']['venues'][0]['city']['name'],
            latitude=event['_embedded']['venues'][0]['location']['latitude'],
            longitude=event['_embedded']['venues'][0]['location']['longitude'],
            start_date=event['dates']['start']['localDate'],
            end_date=event['dates']['end']['localDate'] if 'end' in event['dates'] else None,
            genre=event['classifications'][0]['genre']['name'] if 'classifications' in event else None,
        )

    @classmethod
    def from_eventbrite_event(cls, event):
        return cls(
            id=f"eventbrite-{event['url'].rsplit('/', 1)[-1]}",
            name=event['name'],
            image_url=event['image'],
            external_url=event['url'],
            venue=event['location']['name'],
            city=event['location']['address']['addressLocality'],
            latitude=event['location']['geo']['latitude'],
            longitude=event['location']['geo']['longitude'],
            start_date=event['startDate'],
            end_date=event['endDate'],
            description=event['description'],
        )

    @classmethod
    def from_art_fund_event(cls, event):
        return cls(
            id=f"artfund-{event['attributes']['slug']}",
            name=event['attributes']['title'],
            image_url=event['attributes']['image']['src'] if 'src' in event['attributes']['image'] else event['attributes']['image']['srcset']['md'],
            external_url=f"https://www.artfund.org/explore/exhibitions/{event['attributes']['startDate'].replace('-', '/')}/{event['attributes']['slug']}",
            venue=event['attributes']['museum']['title'],
            city=event['attributes']['museum']['town'],
            latitude=event['attributes']['museum']['location'][0],
            longitude=event['attributes']['museum']['location'][1],
            start_date=event['attributes']['startDate'],
            end_date=event['attributes']['endDate'],
            genre=', '.join(event['attributes']['search']['eventType']),
            description=event['attributes']['subTitle'],
        )

