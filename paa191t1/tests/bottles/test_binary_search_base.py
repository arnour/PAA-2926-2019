from paa191t1.tests import TestBase
from hamcrest import (
    assert_that,
    equal_to
)


class TestBinarySearchBase(TestBase):

    _SKIP = True

    def setUp(self):
        self.bottles = lambda x, y: None

    def test_should_find_lower(self):
        assert_that(self.bottles(6, "0" * 6), equal_to(
            (True, 10, 10)
        ))

    def test_should_find_higher(self):
        assert_that(self.bottles(6, "1" * 6), equal_to(
            (True, 6, 0)
        ))

    def test_should_find_middle(self):
        assert_that(self.bottles(6, "101010"), equal_to(
            (True, 9, 5)
        ))

    def test_should_find_almost_medium(self):
        assert_that(self.bottles(6, "100000"), equal_to(
            (True, 11, 9)
        ))

    def test_should_find_almost_medium_1(self):
        assert_that(self.bottles(6, "100001"), equal_to(
            (True, 9, 7)
        ))

    def test_should_find_almost_medium_3(self):
        assert_that(self.bottles(6, "100010"), equal_to(
            (True, 10, 7)
        ))

    def test_should_find_almost_medium_4(self):
        assert_that(self.bottles(6, "001100"), equal_to(
            (True, 10, 7)
        ))

    def test_should_find_almost_lower_1(self):
        assert_that(self.bottles(6, "000001"), equal_to(
            (True, 10, 9)
        ))

    def test_should_find_almost_lower_2(self):
        assert_that(self.bottles(6, "000010"), equal_to(
            (True, 11, 9)
        ))

    def test_should_find_almost_higher(self):
        assert_that(self.bottles(6, "110000"), equal_to(
            (True, 10, 7)
        ))

    def test_should_find_lot_of_ones(self):
        assert_that(self.bottles(6, "110111"), equal_to(
            (True, 4, 1)
        ))

    def test_should_find_lot_of_numbers(self):
        assert_that(self.bottles(34, "1010111010101011001010101010010010"), equal_to(
            (True, 51, 33)
        ))

    def test_should_find_lot_of_numbers_2(self):
        assert_that(self.bottles(34, "1111111010101011001010101010010010"), equal_to(
            (True, 49, 29)
        ))

    def test_should_find_lot_of_numbers_min(self):
        assert_that(self.bottles(34, "0" * 34), equal_to(
            (True, 66, 66)
        ))

    def test_should_find_lot_of_numbers_max(self):
        assert_that(self.bottles(34, "1" * 34), equal_to(
            (True, 34, 0)
        ))

    def test_should_find_lot_of_zeros(self):
        assert_that(self.bottles(6, "010010"), equal_to(
            (True, 10, 7)
        ))
