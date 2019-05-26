from paa191t1.dijkstra.datastructs.avl import AVL
from paa191t1.tests.dijkstra.test_dijkstra import TestDijkstraBase


class TestDijkstraAVL(TestDijkstraBase):

    def setUp(self):
        self.struct = AVL()
