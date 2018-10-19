import unittest
from LCA import *

class TestLCA(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructor(self):
        tree = Tree()
        self.assertEqual(tree.root, None)

    def test_empty_tree(self):
        tree = Tree()
        self.assertEqual(tree.find_LCA(1,2),None)

    def test_duplicates(self):
        tree = Tree()
        vals = [2,1,3,3]
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.find_LCA(3,3),None)
        self.assertEqual(tree.find_LCA(1,1),None)

    def test_one_node(self):
        tree = Tree()
        tree.put(2)

        self.assertEqual(tree.find_LCA(2,2),None)
        self.assertEqual(tree.find_LCA(2,1),None)

    # test order, LCA, not in tree, etc
    # test put [maybe also: delete, contains, size, median, height, max, min]

    def test_get(self):
        tree = Tree()
        vals = [2,4,1,6,5,7,8,3]
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.get(2),2)
        self.assertEqual(tree.get(5),5)

    # function tests height of tree, as well as function max (as max is used in height)
    def test_height(self):
        tree = Tree()
        self.assertEqual(tree.height(),-1)

        tree.put(7)
        self.assertEqual(tree.height(),0)

        tree.put(8)
        tree.put(3)
        self.assertEqual(tree.height(),1)

        tree.put(1)
        tree.put(2)
        self.assertEqual(tree.height(),3)

        tree.put(6)
        tree.put(4)
        tree.put(5)
        self.assertEqual(tree.height(),4)

    def test_LCA(self):

        vals = [30, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.find_LCA(3, 29), 8)
        self.assertEqual(tree.find_LCA(10, 29), 20)
        self.assertEqual(tree.find_LCA(20, 52), 30)
        self.assertEqual(tree.find_LCA(3, 62), 30)
        self.assertEqual(tree.find_LCA(3, 1), 8)
        self.assertEqual(tree.find_LCA(8, 3), 30)
        self.assertEqual(tree.find_LCA(8, 20), 30)
        self.assertEqual(tree.find_LCA(62, 52), 30)
        self.assertEqual(tree.find_LCA(10, 20), 8)
        self.assertEqual(tree.find_LCA(3, 8), 30)

        # testing when values are not in the tree:
        self.assertEqual(tree.find_LCA(4, 29), None)
        self.assertEqual(tree.find_LCA(29, 4), None)

    def test_nonstandardcharacters(self):
        vals = [12, 8, 52, 3, 20, 10, 29, 62]
        tree = Tree()
        for val in vals:
            tree.put(val)
        with self.assertRaises(TypeError):
            tree.find_LCA('a', 'b')

    def test_nonstandardcharacters_tree(self):
        vals = ['b', 'c', 'a']
        tree = Tree()
        for val in vals:
            tree.put(val)
        self.assertEqual(tree.find_LCA('a', 'c'), 'b')
        self.assertEqual(tree.find_LCA('a', 'b'), None)


if __name__ == '__main__':
    unittest.main()
