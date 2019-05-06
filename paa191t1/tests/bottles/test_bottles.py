import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles import bottles


class TestBottlesK2(unittest.TestCase):

    K = 2

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=1)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 2, 2))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=100)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 20, 2))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=50)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 15, 2))
        )


class TestBottlesK3(unittest.TestCase):

    K = 3

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=1)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 3, 3))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=100)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 12, 3))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=50)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 6, 3))
        )


class TestBottlesK4(unittest.TestCase):

    K = 4

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=1)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 4, 4))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=100)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 7, 3))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = bottles(max_height=100, test_bottles=self.K, break_point=50)
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 9, 4))
        )
