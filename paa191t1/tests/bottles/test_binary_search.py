import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles.binary_search import bottles
from paa191t1.tests.bottles.test_binary_search_base import TestBinarySearchBase


class TestBinarySearch(TestBinarySearchBase):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles