import unittest
from website.api.eventbrite import EventbriteEventManager


class TestEventbrite(unittest.TestCase):

    def test_get_events_with_invalid_input(self):
        eventbrite_manager = EventbriteEventManager()
        expected_result = 'November Wirral Beer Festival'
        event = eventbrite_manager.get_events('POTS N PINTS at The Belvedere, Weymouth.')[0]
        event_name = event.name
        self.assertNotEqual(event_name, expected_result)

    def test_get_events_with_valid_input(self):
        eventbrite_manager = EventbriteEventManager()
        expected_result = 'Weymouth'
        event = eventbrite_manager.get_events('POTS N PINTS at The Belvedere, Weymouth.')[0]
        event_city = event.city
        self.assertEqual(event_city, expected_result)


    def test_get_with_id_with_invalid_ids(self):
        eventbrite_manager = EventbriteEventManager()
        result = eventbrite_manager.get_event_by_id('k91nGUv2c')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()