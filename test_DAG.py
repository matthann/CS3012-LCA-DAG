import unittest
from DAG import *

class TestDAG(unittest.TestCase):

    def setUp(self):
        self.dag = DAG()

    def testInit(self):
        self.dag1 = DAG()
        self.assertTrue(self.dag1.graph == {})

    def testAddNode(self):
        self.dag.add_node(1)
        self.assertTrue(self.dag.graph == {1: set()})

    def testAddDuplicatedNode(self):
        self.dag.add_node(1)
        with self.assertRaises(KeyError) as ex:
            self.dag.add_node(1)

        err = ex.exception
        self.assertEqual(str(err), "'node 1 already exists'")

    def testAddNodeIfNotExists(self):
        self.dag.add_node(1)
        self.dag.add_node_if_not_exists(1)
        self.dag.add_node_if_not_exists(2)
        self.assertTrue(self.dag.graph == {1: set(), 2: set()})
        #nothing should happen: pass can not be tested explicitly

    def testDeleteNode(self):
        self.dag.add_node(1)
        self.dag.delete_node(1)
        self.assertTrue(self.dag.graph == {})

    def testDeleteNonExistingNode(self):
        self.dag.add_node(1)
        with self.assertRaises(KeyError) as ex:
            self.dag.delete_node(2)

        err = ex.exception
        self.assertEqual(str(err), "'node 2 does not exist'")

    def testDeleteNodeIfExists(self):
        self.dag.add_node(1)
        self.assertTrue(self.dag.graph == {1: set()})
        self.dag.delete_node_if_exists(2)
        self.assertTrue(self.dag.graph == {1: set()})
        #nothing should happen: pass can not be tested explicitly

    def testResetDAG(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.reset_graph()
        self.assertTrue(self.dag.graph == {})



# test for adding Edges, for independence , test sizes , downtsream
#  leaves lca

    def testPredecessorsOnlyOne(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1, 2)
        self.assertEqual(self.dag.predecessors(2), [1])

    def testPredecessorsMoreThanOne(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_node(3)
        self.dag.add_node(4)
        self.dag.add_edge(1, 2)
        self.dag.add_edge(3, 2)
        self.dag.add_edge(4, 2)
        self.assertEqual(self.dag.predecessors(2), [1, 3, 4])

    def testPredecessorsRoot(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1, 2)
        self.assertEqual(self.dag.predecessors(1), [])

    def testPredecessorsMoreLevels(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_node(3)
        self.dag.add_edge(1, 2)
        self.dag.add_edge(2, 3)
        self.assertEqual(self.dag.predecessors(3), [2])






if __name__ == '__main__':
    unittest.main()
