import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles.binary_search import bottles


class TestBinarySearch(unittest.TestCase):

    def test_should_find_lower(self):
        assert_that(bottles(6, "0" * 6), equal_to(
            (True, 7, 7)
        ))

    def test_should_find_higher(self):
        assert_that(bottles(6, "1" * 6), equal_to(
            (True, 6, 1)
        ))

    def test_should_find_middle(self):
        assert_that(bottles(6, "101010"), equal_to(
            (True, 6, 1)
        ))

    def test_should_find_almost_medium(self):
        assert_that(bottles(6, "100000"), equal_to(
            (True, 1, 1)
        ))

    def test_should_find_almost_medium_1(self):
        assert_that(bottles(6, "100001"), equal_to(
            (True, 6, 1)
        ))

    def test_should_find_almost_medium_3(self):
        assert_that(bottles(6, "100010"), equal_to(
            (True, 5, 1)
        ))

    def test_should_find_almost_medium_4(self):
        assert_that(bottles(6, "001100"), equal_to(
            (True, 4, 3)
        ))

    def test_should_find_almost_lower_1(self):
        assert_that(bottles(6, "000001"), equal_to(
            (True, 6, 6)
        ))

    def test_should_find_almost_lower_2(self):
        assert_that(bottles(6, "000010"), equal_to(
            (True, 5, 5)
        ))

    def test_should_find_almost_higher(self):
        assert_that(bottles(6, "110000"), equal_to(
            (True, 2, 1)
        ))

    def test_should_find_lot_of_ones(self):
        assert_that(bottles(6, "110111"), equal_to(
            (True, 7, 1)
        ))

    def test_should_find_lot_of_numbers(self):
        assert_that(bottles(34, "1010111010101011001010101010010010"), equal_to(
            (True, 49, 1)
        ))

    def test_should_find_lot_of_zeros(self):
        assert_that(bottles(6, "010010"), equal_to(
            (True, 5, 2)
        ))
