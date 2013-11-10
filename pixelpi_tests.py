import unittest
import mock

from pixelpi import BaseStrip

# I'm so lazy
mock_file = mock.patch('__builtin__.file', return_value='mock_file')
mock_file.start()


class DummyStrip(BaseStrip):
    """Dummy implementation of `BaseStrip`"""
    pass


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_num_leds_can_be_set(self):
        strip = DummyStrip(num_leds=99)
        self.assertEqual(strip.num_leds, 99)

    def test_refresh_rate_default(self):
        strip = DummyStrip(num_leds=1)
        self.assertEqual(strip.refresh_rate, 500)  # assertTrue?

    def test_refresh_rate_can_be_set(self):
        strip = DummyStrip(num_leds=1, refresh_rate=501)
        self.assertEqual(strip.refresh_rate, 501)

    def test_spi_dev_name_default(self):
        strip = DummyStrip(num_leds=1)
        self.assertEqual(strip.spidev, 'mock_file')

    def test_spi_dev_name_can_be_set(self):
        strip = DummyStrip(num_leds=1, spi_dev_name='momomo')
        # TODO
        self.assertEqual(strip.spidev, 'mock_file')


if __name__ == '__main__':
    unittest.main()
