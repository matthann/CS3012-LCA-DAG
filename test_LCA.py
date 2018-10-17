import unittest
from LCA import *



class TestLCA(unittest.TestCase):

    def setUp(self):
        pass


class TestStringMethods(unittest.TestCase):

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

        self.assertEqual(tree.find_common(2,2),None)
        self.assertEqual(tree.find_common(2,1),None)


    # test order, LCA, not in tree, etc
    # test put [maybe also: delete, contains, size, median, height, max, min]

    def test_get(self):

        tree = Tree()
        vals = [2,4,1,6,5,7,8,3]
        for val in vals:
            tree.put(val)

        self.assertEqual(tree.get(2),2)
        self.assertEqual(tree.get(5),5)
