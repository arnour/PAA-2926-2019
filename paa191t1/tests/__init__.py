from unittest import TestCase, SkipTest


class TestBase(TestCase):

    @classmethod
    def setUpClass(cls):
        if cls.__name__ == 'TestBase' or cls.__name__.endswith('Base'):
            raise SkipTest("Base class")
        super().setUpClass()
