import unittest
from website.api.ticketmaster import TicketmasterEventManager


class TestTicketmaster(unittest.TestCase):

    def test_events_name_with_valid_id(self):
        ticketmaster_manager = TicketmasterEventManager()
        event = ticketmaster_manager.get_event_by_id('ticketmaster-G5djZ9dlI_px7')
        event_name = event.name
        self.assertEqual('Magic Mike Live', event_name)

    def test_get_events_with_valid_input_id(self):
        ticketmaster_manager = TicketmasterEventManager()
        expected_result = 'ticketmaster-G5dfZ93SBm0Tz'
        event = ticketmaster_manager.get_event_by_id('ticketmaster-G5dfZ93SBm0Tz')
        event_id = event.id
        self.assertEqual(event_id, expected_result)

    def test_ticketmaster_get_with_id_with_invalid_ids(self):
        ticketmaster_manager = TicketmasterEventManager()
        result = ticketmaster_manager.get_event_by_id('ticketmaster-G91nGUv2c')
        self.assertIsNone(result)

    def test_lookup_event_by_id(self):
        ticketmaster_manager = TicketmasterEventManager()
        data = ticketmaster_manager.get_event_by_id("ticketmaster-G5vHZ92wINvmj")
        self.assertNotEqual("ticketmaster-G5vHZ92wINUGT", data)

    def test_events(self):
        ticketmaster_manager = TicketmasterEventManager()
        self.assertNotIn('hdiogh8', ticketmaster_manager.get_events(query='London'))


if __name__ == '__main__':
    unittest.main()