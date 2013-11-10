import unittest
import mock

from pixelpi import BaseStrip, BLACK, WHITE, GRAY


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
    chip_type = 'DUMMY9000'

    def calculate_gamma(self):
        return range(256)


class BaseStripTest(unittest.TestCase):
    def setUp(self):
        self.strip = DummyStrip()

    def test_chip_type_attribute_comes_from_class(self):
        self.assertEqual(self.strip.chip_type, 'DUMMY9000')
        strip = DummyStrip(chip_type='LOL1337')
        self.assertEqual(strip.chip_type, 'DUMMY9000')

    def test_num_leds_can_be_set(self):
        strip = DummyStrip(num_leds=99)
        self.assertEqual(strip.num_leds, 99)

    def test_refresh_rate_can_be_set(self):
        strip = DummyStrip(refresh_rate=501)
        self.assertEqual(strip.refresh_rate, 501)

    def test_spi_dev_name_default(self):
        self.assertEqual(self.strip.spidev.name, '/dev/spidev0.0')

    def test_spi_dev_name_can_be_set(self):
        strip = DummyStrip(spi_dev_name='foobar')
        # TODO
        self.assertEqual(strip.spidev.name, 'foobar')

    def test_write_stream_args(self):
        self.strip.write_stream('some data')
        self.assertEqual(self.strip.spidev.pixels, 'some data')

    def test_gamma(self):
        self.assertEqual(len(self.strip.gamma), 256)

    def test_filter_pixel(self):
        self.assertEqual(self.strip.filter_pixel(WHITE, 1), WHITE)
        self.assertEqual(self.strip.filter_pixel(WHITE, 0.502), GRAY)  # XXX
        self.assertEqual(self.strip.filter_pixel(WHITE, 0), BLACK)


if __name__ == '__main__':
    unittest.main()
