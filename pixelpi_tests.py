import unittest
import mock

from pixelpi import BaseStrip


class MockSPI(object):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def write(self, pixels):
        self.pixels = pixels


# I'm so lazy
mock_file = mock.patch('__builtin__.file', MockSPI)
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


class BaseStripTest(unittest.TestCase):
    def setUp(self):
        self.strip = DummyStrip(num_leds=3)

    def test_refresh_rate_default(self):
        self.assertEqual(self.strip.refresh_rate, 500)  # assertTrue?

    def test_refresh_rate_can_be_set(self):
        strip = DummyStrip(num_leds=1, refresh_rate=501)
        self.assertEqual(strip.refresh_rate, 501)

    def test_spi_dev_name_default(self):
        self.assertEqual(self.strip.spidev.name, '/dev/spidev0.0')

    def test_spi_dev_name_can_be_set(self):
        strip = DummyStrip(num_leds=1, spi_dev_name='foobar')
        # TODO
        self.assertEqual(strip.spidev.name, 'foobar')

    def test_write_stream_args(self):
        self.strip.write_stream('some data')
        self.assertEqual(self.strip.spidev.pixels, 'some data')


if __name__ == '__main__':
    unittest.main()
