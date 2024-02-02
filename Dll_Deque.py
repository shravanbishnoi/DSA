"""
This file contain a Doubly Linked List Implementation

Author: Shravan
Date: 12-10-2023

"""
from Doubly_base import _DoublyLinkedBase
from queue_exception import Empty

class Dll_Deque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Returns the first element(just after the header) from the Deque/DLL"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element
    
    def last(self):
        """Returns the last element(element just before the trailer) from the Deque/DLL"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Inserts the element e as a first element of Deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Inserts the element e at last of the Deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Returns and deletes first element of the Deque
        
        Raise Exception if the Deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Returns and deletes last element of the Deque
        
        Raise Exception if the Deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
