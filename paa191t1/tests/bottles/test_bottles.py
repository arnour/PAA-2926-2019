from paa191t1.bottles.bottles import bottles
from paa191t1.tests.bottles.test_bottles_base import TestBottlesBaseK2, TestBottlesBaseK3, TestBottlesBaseK4
from hamcrest import (
    assert_that,
    equal_to
)

class TestBottlesK2(TestBottlesBaseK2):
    
    _SKIP = False

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="000001")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 2, 2))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="111111")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 15, 2))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="100000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 12, 2))
            )


class TestBottlesK3(TestBottlesBaseK3):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="000001")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 3, 3))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="111111")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 11, 3))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="100000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 10, 3))
        )

class TestBottlesK4(TestBottlesBaseK4):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="000001")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 4, 4))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="111111")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 10, 4))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="100000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 7, 4))
        )

    def test_should_find_break_point_at_median_position2(self):
        found, used_trials, used_bottles = self.bottles(max_height=20, test_bottles=self.K, break_point="10000000000000000000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 112, 4))
        )