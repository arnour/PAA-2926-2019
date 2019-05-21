import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles.binary_search_decimal import bottles


class TestBinarySearchDecimal(unittest.TestCase):

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
            (True, 6, 3)
        ))

    def test_should_find_almost_medium(self):
        assert_that(bottles(6, "100000"), equal_to(
            (True, 1, 1)
        ))

    def test_should_find_almost_medium_1(self):
        assert_that(bottles(6, "100001"), equal_to(
            (True, 6, 5)
        ))

    def test_should_find_almost_medium_3(self):
        assert_that(bottles(6, "100010"), equal_to(
            (True, 5, 4)
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
            (True, 7, 2)
        ))

    def test_should_find_lot_of_numbers(self):
        assert_that(bottles(34, "1010111010101011001010101010010010"), equal_to(
            (True, 45, 17)
        ))

    def test_should_find_lot_of_numbers_2(self):
        assert_that(bottles(34, "1111111010101011001010101010010010"), equal_to(
            (True, 43, 15)
        ))

    def test_should_find_lot_of_numbers_min(self):
        assert_that(bottles(34, "0" * 34), equal_to(
            (True, 35, 35)
        ))

    def test_should_find_lot_of_numbers_max(self):
        assert_that(bottles(34, "1" * 34), equal_to(
            (True, 34, 1)
        ))

    def test_should_find_lot_of_zeros(self):
        assert_that(bottles(6, "010010"), equal_to(
            (True, 5, 4)
        ))
