from unittest import TestCase, SkipTest


class TestBase(TestCase):

    _SKIP = True

    @classmethod
    def setUpClass(cls):
        if cls is TestBase or cls._SKIP:
            raise SkipTest("Base class")
        super().setUpClass()
