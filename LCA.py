
# Assignment: Given a Binary Tree and two inputs. Write a program to find their lowest common ancestor.

class Node(object):

    # Constructor
    def __init__(self, val):
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

    def __init__(self):
        self.root = None

    def put(self,val):
        if not (self.node_exists(val)):
            self.root = self._put(self.root,val)

    def _put(self,node,val):
        if node is None:
            node = Node(val)

        if val < node:
            node.left = self._put(node.left,val)
        elif val > node:
            node.right = self._put(node.right,val)
        else:
            node.val = val

        return node

    def get(self,val):
        return self._get(self.root,val)

    def _get(self,node,val):
        while not node is None:
            if val < node:
                node = node.left
            elif val > node:
                node = node.right
            else:
                return node.val

        return None

    def find_LCA(self,a,b):
        if a == b:
            return
        else:
            return self._find_LCA(self.root,a,b)

    def _find_LCA(self,node,a,b):
        if node is None:
            return None
        # Traverse right until a diverge occurs
        if a > node and b > node:
            if node.right is None: return None

            # if right node is 'a' or 'b' then LCA has been found
            if node.right == a or node.right == b:
                return node.val

            return self._find_LCA(node.right,a,b)

        # Traverse left until a diverge occurs
        elif a < node and b < node:
            if node.left is None: return None

            # if left node is 'a' or 'b' then LCA has been found
            if node.left == a or node.left == b:
                return node.val

            return self._find_LCA(node.left,a,b)

        # root does not have a common ancestor
        elif a == self.root or b == self.root:
            return None

        else:
            # diverge of tree traversal occurs here
            # current node is a potential common ancestor
            # so verify that a and b are legitimate node_exists
            if self._node_exists(node,a):
                if self._node_exists(node,b):
                    return node.val
                else:
                    return None
            else:
                return None

    def node_exists(self,val):
        return self._node_exists(self.root,val)

    def _node_exists(self,node,val):
        return not self._get(node,val) is None

    def height(self):
        return self._height(self.root)

    def _height(self,node):
        if (node == None):
            return -1;
        else:
            return 1 + max(self._height(node.left),self._height(node.right))

    def max(node):
        if (node.right != None): return max(node.right)
        return node
