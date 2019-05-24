from paa191t1.bottles.bottles_binary import bottles
from paa191t1.tests.bottles.test_bottles_base import TestBottlesBaseK2, TestBottlesBaseK4

class TestBottlesBinaryK2(TestBottlesBaseK2):
    
    _SKIP = False

    def setUp(self):
        self.bottles = bottles

class TestBottlesBinaryK4(TestBottlesBaseK4):

    _SKIP = False

    def setUp(self):
        self.bottles = bottles
