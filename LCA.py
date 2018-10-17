
# Assignment: Given a Binary Tree and two inputs. Write a program to find their lowest common ancestor.

class Node(object):

    # Constructor
    def__init__(self, val):
    self.val = val
    self.left = None
    self.right = None

    def __lt__(self,val):
        return self.val < val

    def __gt__(self,val):
        return self.val > val

    def __eq__(self,val):
        return self.val == val


class Tree(object):

    def__init__(self):
    self.root = None

    def put(self,val):
        if not (self.node_exists(val)):
            self.root = self._put(self.root,val)

    def _put(self,node,val):
        if node is None:
            node = Node(val)

        if val < node:
            node.left = self._put(self.root,val)
        elif val > node:
            node.right = self._put(node.right,val)
        else:
            node.val = val

        return node
