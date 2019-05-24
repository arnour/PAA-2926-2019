from paa191t1.bottles.bottles import bottles
from paa191t1.tests.bottles.test_bottles_base import TestBottlesBaseK2, TestBottlesBaseK3, TestBottlesBaseK4

class TestBottlesK2(TestBottlesBaseK2):
    
    _SKIP = False

    def setUp(self):
        self.bottles = bottles

class TestBottlesK3(TestBottlesBaseK3):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles


class TestBottlesK4(TestBottlesBaseK4):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles
