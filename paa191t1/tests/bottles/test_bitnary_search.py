import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles.binary_search import bottles


class TestBinarySearch(unittest.TestCase):

    def test_should_find_lower(self):
        assert_that(bottles(6, 6, "0" * 6), equal_to(
            (True, 0, 1)
        ))

    def test_should_find_higher(self):
        assert_that(bottles(6, 6, "1" * 6), equal_to(
            (True, 7, 2)
        ))

    # def test_should_find_higher(self):
    #     assert_that(bottles(6, 6, "101010"), equal_to(
    #         (True, 33, 6)
    #     ))
