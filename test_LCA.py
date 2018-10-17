import unittest
from LCA import *


class TestLCA(unittest.TestCase):

    def setUp(self):
        pass


class TestStringMethods(unittest.TestCase):

    def test_constructor(self):
        tree = Tree()
        self.assertEqual(tree.root, None)

    #def test_empty_tree(self):

    def test_get(self):

        tree = Tree()
        vals = [2,4,1,6,5,7,8,3]
        for val in vals:
            tree.put(val)


        self.assertEqual(tree.get(2),2)
        self.assertEqual(tree.get(5),5)
