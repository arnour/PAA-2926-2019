from paa191t1.bottles.binary_search_decimal import bottles
from paa191t1.tests.bottles.test_binary_search_base import TestBinarySearchBase


class TestBinarySearchDecimal(TestBinarySearchBase):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles
