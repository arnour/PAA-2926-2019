import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles.bit_array import BitArray


class TestBitArray(unittest.TestCase):

    def test_should_shift_right(self):
        bits = BitArray("110")
        expected = BitArray("011")
        assert_that(bits >> 1, equal_to(expected))

    def test_should_shift_left(self):
        bits = BitArray("110")
        expected = BitArray("100")
        assert_that(bits << 1, equal_to(expected))

    def test_should_print_as_bits(self):
        bits = BitArray("100")
        expected = "BitArray('100')"
        assert_that(bits.__repr__(), equal_to(expected))
