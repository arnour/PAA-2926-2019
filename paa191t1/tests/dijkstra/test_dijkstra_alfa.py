from paa191t1.dijkstra.datastructs.alfa_tree import AlfaTree
from paa191t1.tests.dijkstra.test_dijkstra import TestDijkstraBase


class TestDijkstraAlfa(TestDijkstraBase):

    _SKIP = False

    def setUp(self):
        self.struct = AlfaTree()
