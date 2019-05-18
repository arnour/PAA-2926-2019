from paa191t1.pph import pph_n_2
from paa191t1.tests.pph import TestPPH


class TestPPHN2(TestPPH):

    _SKIP = False

    def setUp(self):
        self.pph = pph_n_2
