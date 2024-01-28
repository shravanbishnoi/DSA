"""
In this Module, A new Abstract Data Type called Tree and
Tree's specialization Binary Tree with implementation using
LinkedList.

Author: Shravan
Date: 05-10-2023
"""
from sll_queue import Sll_queue

class Tree(object):
    """Abstract base class representing a tree structure."""

    ##-------------------------- nested Position class ----------------------##
    class Position(object):
        """
        An abstraction representing the location of a single element.
        """
        def element(self):
            """Returns the element stored at this position"""
            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            raise NotImplementedError("must be implemented by subclass")
        
        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not(self==other)
        
    ##---------- abstract methods that concrete subclass must support ---------##
    def root(self):
        """Return Position representing the tree s root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")
    
    def parent(self, p):
        """Return Position representing p s parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")
    
    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass")
    
    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        raise NotImplementedError("must be implemented by subclass")
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")
    
    def positions(self):
        """Generates an iteration of all positions of tree T."""
        raise NotImplementedError("must be implemented by subclass")
    
    def __iter__():
        """Generates an iteration of tree's elements."""
        raise NotImplemented("must be implemented by subclass")
    
    ##---------- concrete methods implemented in this class ----------##
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root()==p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p)==0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height1(self):
        """Returns the height of the tree"""
        return max(self.depth(i) for i in self.positions() if self.is_leaf(i))
    
    def _height2(self, p):
        """Returns the height of the tree"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        
        If p is None, return the height of the entire tree."""
        if p is None:
            p = self.root()
        return self. height2(p)                              # start height2 recursion
    
    def __iter__(self):
        """Generates an iteration of the tree's elements."""
        for p in self.positions():                           # use same order as positions()
            yield p.element()                                # but yield each element
    
    ##------------------Preorder traversal for Trees-------------------##
    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):    # start recursion
                yield p
    
    def _subtree_preorder(self, p):
        """Generates a preorder  iteration of positions in subtree rooted at p."""
        yield p                                              # visit p before its subtrees
        for children in self.children(p):                    # for each child c
            for other in self._subtree_preorder(children):   # do preorder of children’s subtree
                yield other                                  # yielding each to our caller
                
    
    def positions(self):
        """Generates an iteration of the tree's positions"""
        return self.preorder()                               # return entire preorder iteration
    
    ##------------------ Postorder traversal for Trees -------------------##
    def postorder(self):
        """Generates a postorder iteration of the positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):   # start recursion
                yield p

    def _subtree_postorder(self, p):
        """Generates a postorder iteration of the positions in subtree rooted at p."""
        for c in self.children(p):                           # for each child c
            for other in self._subtree_postorder(c):         # do postorder of c’s subtree
                yield other                                      # yielding each to our caller
        yield p                                              # visit p after its subtrees

    ##------------------ Breadth-First traversal for Trees -------------------##
    def breadthfirst(self):
        """Generates a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            queue = Sll_queue()                              # Queue for storing positions not yet visited
            queue.enqueue(self.root())                       # Starting with root
            while not queue.is_empty():
                p = queue.dequeue()                          # remove from front of the queue
                yield p                                      # report this position
                for child in self.children(p):
                    queue.enqueue(child)                     # add children to back of queue

    
    def _height(self):
        """Returns the height of the tree."""
        pass


    # ##------------------Preorder traversal for Trees-------------------##
    # def preorder(self):
    #     """Generate a preorder iteration of positions in the tree."""
    #     if not self.is_empty():
    #         temp =  []
    #         print(self.root()._node._element)
    #         for p in self._subtree_preorder(self.root(), temp):
    #             print(p._node._element)
    #             self._subtree_preorder(self.root(), temp)
    #     return temp

    # def _subtree_preorder(self, p, temp):
    #     """Generates a preorder  iteration of positions in subtree rooted at p."""
    #     if p not in temp:
    #         temp.append(p)
    #         for child in self.children(p):                    # for each child c
    #             print(child._node._element)
    #             self._subtree_preorder(child, temp)
    #     # return temp
        


###------------------------------------------ BINARY TREE -------------------------------------------###

class BinaryTree(Tree):
    """a binary tree is a specialization of a tree that supports three
    
    additional accessor methods is implemented"""
    
    ##----------------------- Additional accessor methods --------------------------##
    def left(self, p):
        """Return the position that represents the left child of p,
        or None if p has no left child.
        
        Return None if p does not have a left child"""
        raise NotImplementedError("must be implemented by subclass")
    
    def right(self, p):
        """Return a Position representing p s right child.
        
        Return None if p does not have a right child."""
        raise NotImplementedError("must be implemented by subclass")

    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                 # Parent must be root node
            return None                    # Root node does not have siblings
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    ##------------------ Inorder traversal for binary trees -------------------##
    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:                               # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                                                    # Visit p between its subtrees
        if self.right(p) is not None:                              # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder the default
    def positions(self):
        """Generates an iteration of the tree's positions."""
        return self.inorder()                                      # make inorder the default


###--------------------------- LinkedBinaryTree implementation ----------------------------------###

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    ##---------------------------------- Node Class ------------------------##
    class _Node(object):
        """Represent a Node entity"""

        __slots__ = "_element", "_parent", "_left", "_right"
        def __init__(self, element, parent=None, left=None, right=None):
            """Initializes a Node object"""
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An Abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Initializes a Position object"""
            self._container = container
            self._node = node

        def element(self):
            """Returns the element of the object"""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Returns associated node if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError(p, "must me a proper Position type.")
        if p._container is not self:
            raise ValueError(p, "does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError(p, "is no longer valid")
        return p._node
    
    def _make_position(self, node):
        """Return Position instance for given node(or None if no node)."""
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0
    
    ##-----------------------Public Accessors-------------------------------##
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def root(self):
        """Return the root position of the tree."""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Return the position of p's parent (or None if p is root)."""
        return self._make_position(self._validate(p)._parent)
    
    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        return self._make_position(self._validate(p)._left)
    
    def right(self, p):
        """Return the postion of p's right child (or None if no right child)."""
        return self._make_position(self._validate(p)._right)
    
    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        childCount = 0
        if node._left is not None:
            childCount += 1
        if node._right is not None:
            childCount += 1
        return childCount
    
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        
        Raise ValueError if tree nonempt"""
        if self._root is not None:
            raise ValueError("Root already Exist.")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        
        Return the postion of the new node.
        Raise ValueError if Position p is invalid or p already has a left child."""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError(p, "already has left child.")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child."""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError(p, "already has right child.")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        oldElement = node._element
        node._element = e
        return oldElement
    
    def _delete(self, p):
        """Delete the node at position p, and replace it with its child, if any.
        
        Return the element that had been stored at position p.
        Raise ValuerError if position p is invalid or p has two children."""
        node = self._validate(p)
        nodeElement = node._element
        if self.num_children(p)==2:
            raise ValueError(p, "has two children")
        child = node._left if node._left else node._right # might be None
        if child is not None:
            child._parent = node._parent
        if node is self.root():
            self._root = child    # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = parent     # deprecating
        return nodeElement
    
    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Position must be a leaf")
        if not type(self) is type(t1) is type(t2):      # all 3 trees must be same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():                           # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None                             # set t1 instance to empty
            t1._size = 0                                # size becomes zero for t1 
        if not t2.is_empty():                           # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None                             # set t2 instance to empty
            t2._size = 0                                # size becomes zero for t2


###-----------------------Testing-----------------------------####

if __name__ == '__main__':
    tree = LinkedBinaryTree()
    tree._add_root(1)
    node2 = tree._add_left(tree.root(), 2)
    node3 = tree._add_right(tree.root(), 3)
    node4 = tree._add_left(node2, 4)
    node5 = tree._add_right(node2, 5)
    node6 = tree._add_left(node3, 6)
    node7 = tree._add_right(node3, 7)
    node8 = tree._add_right(node7, 8)
    print("Number of the nodes in the tree: ", len(tree))
    print("Height of the Binary Tree: ", tree._height1())