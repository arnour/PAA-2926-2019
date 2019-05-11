from paa191t1.dijkstra.datastructs.vector import Vector
from paa191t1.tests.dijkstra.test_dijkstra import TestDijkstraBase


class TestDijkstraVector(TestDijkstraBase):

    _SKIP = False

    def setUp(self):
        self.struct = Vector()
