"""
In this Module, A new Abstract Data Type called Priority Queue
is implemented using unsorted list, sorted list and heap.

Author: Shravan
Date: 19-10-2023
"""
from queue_exception import Empty
from positional_list import PositionalList

class PriorityQueueBase(object):
    """An Abstract base class for priority queue."""

    class _Item():
        """Lightweight composite to store priority queue items."""
        __slot__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key
    
    def is_empty(self):
        """Return True if the priority queue is empty otherwise false."""
        return len(self) == 0

###----------------------------Implementation Using Unsorted list---------------------###

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        minItem = self._data.first()
        nextItem = self._data.after(minItem)
        while nextItem != None:
            if nextItem.element() < minItem.element():
                minItem = nextItem
            nextItem = self._data.after(nextItem)
        return minItem
    
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()
    
    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)
    
    def add(self, key, value):
        """Add a key-value pair."""
        item = self._Item(key, value)
        self._data.add_last(item)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        item = self._find_min().element()
        return (item._key, item._value)
    
    def remove_min(self):
        """Return and remove (k,v) tuple with minimum key."""
        nodePos = self._find_min()
        nodeEle = self._data.delete(nodePos)
        return (nodeEle._key, nodeEle._value)


###----------------------------Implementation Using sorted list---------------------###

class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of elements in queue."""
        return len(self._data)
    
    def add(self, key, value):
        """Add a key-value pair."""
        newItem = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newItem < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newItem)
        else:
            self._data.add_after(walk, newItem)
    
    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        item = self._data.first().element()
        return (item._key, item._value)
    
    def remove_min(self):
        """Return and remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
    

###----------------------------Implementation Using sorted list---------------------###

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    ##------------------------------ nonpublic behaviors -----------------------------##
    def _parent(self, j):
        return (j-1)//2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j>0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)           # Recursion

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
        if self._data[small_child] < self._data[j]:
            self._swap(j, small_child)
            self._downheap(small_child)     # Recursion

    ##------------------------------ public behaviors --------------------------------##
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    # def init (self, contents=()):
    #     """Create a new priority queue.
        
    #     By default, queue will be empty. If contents is given, it should be as an
    #     iterable sequence of (k,v) tuples specifying the initial contents."""
    #     self. data = [ self. Item(k,v) for k,v in contents ] # empty by default
    #     if len(self. data) > 1:
    #         self._heapify()
    # def _heapify(self):
    #     start = self. parent(len(self) - 1) # start at PARENT of last leaf
    #     for j in range(start,-1,-1):        # going to and including the root
    #         self._downheap(j)

    def __len__(self):
        """Return the number of items in the Priority Queue."""
        return len(self)
    
    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        self._swap(0, len(self._data)-1)                  
        item = self._data.pop()                           # put minimum item at the end
        self._downheap(0)                                 # and remove it from the list;
        return (item._key, item._value)                   # then fix new root
    

