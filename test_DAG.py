import unittest
from DAG import *

class test_DAG(unittest.TestCase):

    def setUp(self):
        self.dag = DAG()

    def test_Init(self):
        self.dag1 = DAG()
        self.assertTrue(self.dag1.graph == {})

    def test_AddNode(self):
        self.dag.add_node(1)
        self.assertTrue(self.dag.graph == {1: set()})

    def test_AddDuplicatedNode(self):
        self.dag.add_node(1)
        with self.assertRaises(KeyError) as ex:
            self.dag.add_node(1)

        err = ex.exception
        self.assertEqual(str(err), "'node 1 already exists'")

    def test_AddNodeIfNotExists(self):
        self.dag.add_node(1)
        self.dag.add_node_if_not_exists(1)
        self.dag.add_node_if_not_exists(2)
        self.assertTrue(self.dag.graph == {1: set(), 2: set()})
        #nothing should happen: pass can not be test_ed explicitly

    def test_DeleteNode(self):
        self.dag.add_node(6)
        self.dag.delete_node(6)
        self.assertTrue(self.dag.graph == {})

    def test_DeleteNonExistingNode(self):
        self.dag.add_node(1)
        with self.assertRaises(KeyError) as ex:
            self.dag.delete_node(2)

        err = ex.exception
        self.assertEqual(str(err), "'node 2 does not exist'")

    def test_DeleteNodeIfExists(self):
        self.dag.add_node(1)
        self.assertTrue(self.dag.graph == {1: set()})
        self.dag.delete_node_if_exists(2)
        self.assertTrue(self.dag.graph == {1: set()})
        #nothing should happen: pass can not be test_ed explicitly

    def test_ResetDAG(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.reset_graph()
        self.assertTrue(self.dag.graph == {})

    def test_AddEdge(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1,2)
        self.assertTrue(self.dag.graph == {1: set([2]), 2: set()})

    def test_AddEdgeNonExistingNodes(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        with self.assertRaises(KeyError) as ex:
            self.dag.add_edge(1, 3)

        err = ex.exception
        self.assertEqual(str(err), "'one or more nodes do not exist in graph'")

    def test_AddEdgeCreateCycle(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_node(3)
        self.dag.add_edge(1, 2)
        self.dag.add_edge(2, 3)
        with self.assertRaises(DAGValidationError):
            self.dag.add_edge(3, 1)
        self.assertTrue(self.dag.graph == {1: set([2]), 2: set([3]), 3: set()})

    def test_DeleteEdge(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1, 2)
        self.dag.delete_edge(1, 2)
        self.assertTrue(self.dag.graph == {1: set(), 2: set()})

    def test_DeleteNonExistingEdge(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1, 2)
        with self.assertRaises(KeyError) as ex:
            self.dag.delete_edge(1, 3)

        err = ex.exception
        self.assertEqual(str(err), "'this edge does not exist in graph'")

# test_ for independence , sizes , downtsream
#  leaves lca

    def test_PredecessorsOnlyOne(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1, 2)
        self.assertEqual(self.dag.predecessors(2), [1])

    def test_PredecessorsMoreThanOne(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_node(3)
        self.dag.add_node(4)
        self.dag.add_edge(1, 2)
        self.dag.add_edge(3, 2)
        self.dag.add_edge(4, 2)
        self.assertEqual(self.dag.predecessors(2), [1, 3, 4])

    def test_PredecessorsRoot(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_edge(1, 2)
        self.assertEqual(self.dag.predecessors(1), [])

    def test_PredecessorsMoreLevels(self):
        self.dag.add_node(1)
        self.dag.add_node(2)
        self.dag.add_node(3)
        self.dag.add_edge(1, 2)
        self.dag.add_edge(2, 3)
        self.assertEqual(self.dag.predecessors(3), [2])

    def testFromDict(self):
        self.dag.add_node(1)
        dict1 = {2: [3, 4], 3: [], 4: [3]}
        self.dag.from_dict(dict1)
        self.assertTrue(self.dag.graph == {
                        2: set([3, 4]), 3: set(), 4: set([3])})

    def testFromDictWrongFormat(self):
        self.dag.add_node(1)
        dict2 = {2: set([3, 4]), 3: set(), 4: set([3])}
        with self.assertRaises(TypeError) as ex:
            self.dag.from_dict(dict2)

        err = ex.exception
        self.assertEqual(str(err), 'dict values must be lists')


if __name__ == '__main__':
    unittest.main()
