from paa191t1.pph.pph_n_log_n import pph_n_lg_n
from paa191t1.tests.pph import TestPPH


class TestPPHNLGN(TestPPH):

    _SKIP = False

    def setUp(self):
        self.pph = pph_n_lg_n
        self.pivot = None
