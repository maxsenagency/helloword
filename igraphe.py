import unittest
from abc import ABC

class GraphInterface(ABC):

    def add_node(self, node):
        return NotImplemented

    def node_count(self):
        return NotImplemented

    def add_edge(self, nd1, nd2):
        return NotImplemented

    def edge_count(self):
        return NotImplemented

    def edge_exists(self, nd1, nd2):
        return NotImplemented


class Graph(GraphInterface):
    #TODO : implement me
    pass


class TestGraph(unittest.TestCase):

    def test_add_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        self.assertEqual(g.node_count(), 2)

    def test_add_edge(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n2")
        self.assertEqual(g.edge_count(), 1)

    def test_add_same_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n1")
        self.assertEqual(g.node_count(), 1)

    def test_add_edge_same_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n1")
        self.assertEqual(g.edge_count(), 0)

    def test_add_edge_on_missing_node(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n2", "n3")
        self.assertEqual(g.edge_count(), 0)

    def test_edge_exists_true(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n2")
        self.assertTrue(g.edge_exists("n1", "n2"))

    def test_edge_exists_true_wrong_order(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_edge("n1", "n2")
        self.assertTrue(g.edge_exists("n2", "n1"))

    def test_edge_exists_true(self):
        g = Graph()
        g.add_node("n1")
        g.add_node("n2")
        g.add_node("n3")
        g.add_edge("n1", "n2")
        self.assertFalse(g.edge_exists("n1", "n3"))

if __name__ == '__main__':
    unittest.main()