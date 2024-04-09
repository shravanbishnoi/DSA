"""
In this module, I have implemented linked binary tree.

Author: Shravan
Date: 01-04-2024
"""

class BinaryTree:

    class _Node:
        def _init_(self, element, parent=None, lchild=None, rchild=None):
            self.element = element
            self.parent = parent
            self.lchild = lchild
            self.rchild = rchild

    def _init_(self):
        self._root = None
        self._size = 0

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root already exists')
        self._root = self._Node(e)
        self._size += 1
        return self._root

    def add_lchild(self, p, e):
        if p.lchild is not None:
            raise ValueError('Left child already exists')
        p.lchild = self._Node(e, parent=p)
        self._size += 1
        return p.lchild

    def add_rchild(self, p, e):
        if p.rchild is not None:
            raise ValueError('Right child already exists')
        p.rchild = self._Node(e, parent=p)
        self._size += 1
        return p.rchild

    def delete(self, p):
        if self.num_children(p) == 2:
            raise ValueError('Cannot delete node with two children')
        
        parent = p.parent
        child = p.lchild if p.lchild else p.rchild

        if child is not None:
            child.parent = parent

        if p == self._root:
            self._root = child
        else:
            if parent.lchild == p:
                parent.lchild = child
            else:
                parent.rchild = child

        element = p.element
        p.parent = p.lchild = p.rchild = None
        self._size -= 1
        return element

    def root(self):
        return self._root.element

    def parent(self, p):
        return p.parent.element

    def left(self, p):
        return p.lchild.element

    def right(self, p):
        return p.rchild.element

    def num_children(self, p):
        count = 0
        if p.lchild is not None:
            count += 1
        if p.rchild is not None:
            count += 1
        return count

    def _len_(self):
        return self._size

# # Example:
# tree = BinaryTree()       # create a Binary tree instance
# root = tree.add_root(5)   # add root
# left_child = tree.add_lchild(root, 10)
# right_child = tree.add_rchild(root, 3)

# print("Root:", tree.root())  # Output: 5
# print("Left Child:", tree.left(root))  # Output: 10
# print("Right Child:", tree.right(root))  # Output: 3
# print("Number of children of root:", tree.num_children(root))  # Output: 2
# print("Total number of nodes:", len(tree))  # Output: 3