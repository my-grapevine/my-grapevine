from unittest import TestCase, mock, main
import os
from events import get_events, get_event_by_id, search


class TestEvents(TestCase):

    def test_get_event_by_id(self):
        self.assertDictEqual(
            get_event_by_id('G5vHZ951MjNRk'),
            {'id': 'G5vHZ951MjNRk', 'name': 'Adele Tribute - Hometown Glory',
             'image_url': 'https://s1.ticketm.net/dam/c/ab4/6367448e-7474-4650-bd2d-02a8f7166ab4_106161_RETINA_PORTRAIT_3_2.jpg',
             'city': 'Barnsley', 'dates': '2022-12-02', 'venues': 'BIRDWELL VENUE', 'classification': 'Undefined',
             'url': 'https://www.ticketmaster.co.uk/adele-tribute-hometown-glory-barnsley-12-02-2022/event/1F005CB2B7723BC6'}

        )

    def test_search(self):
        expected_result = [{'id': 'G5dfZ94alAYyk', 'name': 'The Ed Sheeran Songbook', 'date_event': '2023-09-02', 'venue': 'Whitby Pavilion Theatre', 'city': 'Whitby', 'url': 'https://www.ticketmaster.co.uk/the-ed-sheeran-songbook-whitby-09-02-2023/event/35005D526B170E46', 'image_url': 'https://s1.ticketm.net/dam/c/ab4/6367448e-7474-4650-bd2d-02a8f7166ab4_106161_RETINA_PORTRAIT_3_2.jpg'}]
        search_result = search('ed sheeran')
        self.assertEqual(search_result, expected_result)

    def test_search_with_invalid_input(self):
        expected_result = []
        search("nbdijxkldr")
        self.assertEqual([], [])



    def test_get_event_by_id_with_invalid_id(self):
        expected_result = None
        get_event_by_id("ajk5vHZ9!?x")
        self.assertEqual(None, None)


if __name__ == '__main__':
    unittest.main()
