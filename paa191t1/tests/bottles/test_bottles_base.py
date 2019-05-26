from paa191t1.tests import TestBase


class TestBottlesBaseK2(TestBase):

    _SKIP = True
    K = 2


class TestBottlesBaseK3(TestBase):

    _SKIP = True

    K = 3

    def setUp(self):
        self.bottles = lambda x, y, z: None


class TestBottlesBaseK4(TestBase):

    _SKIP = True

    K = 4

    def setUp(self):
        self.bottles = lambda x, y, z: None
