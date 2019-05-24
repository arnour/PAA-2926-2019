from paa191t1.tests import TestBase
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles.bottles import bottles


class TestBottlesBaseK2(TestBase):

    _SKIP = True
    K = 2

    def setUp(self):
        self.bottles = lambda x, y, z: None

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


class TestBottlesBaseK3(TestBase):

    _SKIP = True
    K = 3

    def setUp(self):
        self.bottles = lambda x, y, z: None
    
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


class TestBottlesBaseK4(TestBase):

    _SKIP = True
    K = 4

    def setUp(self):
        self.bottles = lambda x, y, z: None

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
