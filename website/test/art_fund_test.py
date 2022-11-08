import unittest
from website.api.art_fund import ArtFundEventManager


class TestArt_fund(unittest.TestCase):

    def test_get_events_with_valid_input_test_1(self):
        artfund_manager = ArtFundEventManager()
        expected_result = 'To Be Read at Dusk: Dickens, Ghosts and the Supernatural'
        event = artfund_manager.get_events('london')[0]
        event_name = event.name
        self.assertNotEqual(event_name, expected_result)

    def test_get_events_with_invalid_input(self):
        artfund_manager = ArtFundEventManager()
        expected_result = 'Althea McNish: Colour is Mine'
        event = artfund_manager.get_events('london')[0]
        event_name = event.name
        self.assertNotIn(event_name, expected_result)

    def test_get_events_with_valid_input(self):
        artfund_manager = ArtFundEventManager()
        expected_result = 'Althea McNish: Colour is Mine'
        event = artfund_manager.get_event_by_id('artfund-althea-mcnish-colour-is-mine')
        event_name = event.name
        self.assertEqual(event_name, expected_result)

    def test_get_with_id_with_invalid_ids(self):
        artfund_manager = ArtFundEventManager()
        result = artfund_manager.get_event_by_id('k65juv2c')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()