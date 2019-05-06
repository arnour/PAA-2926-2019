import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles import check_point_height


class TestCheckPointSize(unittest.TestCase):

    def test_should_calculate_check_point_height(self):
        assert_that(check_point_height(start=1, end=100, test_bottles=2), equal_to(10))
        assert_that(check_point_height(start=10, end=20, test_bottles=2), equal_to(3))
        assert_that(check_point_height(start=21, end=33, test_bottles=2), equal_to(3))
        assert_that(check_point_height(start=80, end=80, test_bottles=2), equal_to(0))
        assert_that(check_point_height(start=1, end=1, test_bottles=2), equal_to(0))
        assert_that(check_point_height(start=79, end=125, test_bottles=2), equal_to(7))

        assert_that(check_point_height(start=1, end=100, test_bottles=3), equal_to(21))
        assert_that(check_point_height(start=10, end=20, test_bottles=3), equal_to(5))
        assert_that(check_point_height(start=21, end=33, test_bottles=3), equal_to(5))
        assert_that(check_point_height(start=80, end=80, test_bottles=3), equal_to(0))
        assert_that(check_point_height(start=1, end=1, test_bottles=3), equal_to(0))
        assert_that(check_point_height(start=79, end=125, test_bottles=3), equal_to(13))

        assert_that(check_point_height(start=1, end=100, test_bottles=4), equal_to(31))
        assert_that(check_point_height(start=10, end=20, test_bottles=4), equal_to(6))
        assert_that(check_point_height(start=21, end=33, test_bottles=4), equal_to(6))
        assert_that(check_point_height(start=80, end=80, test_bottles=4), equal_to(0))
        assert_that(check_point_height(start=1, end=1, test_bottles=4), equal_to(0))
        assert_that(check_point_height(start=79, end=125, test_bottles=4), equal_to(18))

    def test_should_calculate_check_point_height_equals_to_one_when_test_bottles_equals_one(self):
        assert_that(check_point_height(start=1, end=100, test_bottles=1), equal_to(1))
        assert_that(check_point_height(start=10, end=20, test_bottles=1), equal_to(1))
        assert_that(check_point_height(start=21, end=33, test_bottles=1), equal_to(1))
        assert_that(check_point_height(start=80, end=80, test_bottles=1), equal_to(1))
        assert_that(check_point_height(start=1, end=1, test_bottles=1), equal_to(1))
        assert_that(check_point_height(start=79, end=125, test_bottles=1), equal_to(1))
