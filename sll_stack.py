"""
This is a module containing Stack class
In this module a Singly Linked List based stack is implemented

Author: Shravan
Date: 11-09-2023
"""
from stack_exception import Empty

####---------------------------Singly Linked List based stack implementation-------------------####

class Sll_stack(object):
    """
    LIFO stack implementation based on singly linked list as an underlying storage
    """

    class Node(object):
        """
        This class represents a light weight object which is building block for a SLL
        """
        def __init__(self, e=None, add=None):
            """
            Initializes a Node object
            """
            self._element = e
            self._next = add
        
        def setnext(self, add):
            """Sets add to next of the current element"""
            self._next = add

        def setelement(self, e1):
            """Sets e1 as a element of the node"""
            self._element = e1

        def getnext(self):
            """Returns the address of the next node"""
            return self._next
        
        def getelement(self):
            """Returns the element of the node"""
            return self._element

    def __init__(self):
        """
        Initializes a SLL object
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """Returns the length of the SLL"""
        return self._size
    
    def is_empty(self):
        """Returns True if the SLL is empty otherwise  False"""
        return self._size==0
    
    def top(self):
        """Returns(but do not remove) the top of the stack"""
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._head.getelement()
    
    def push(self, e):
        """Adds e to stack"""
        node_obj = Sll_stack.Node(e, self._head)
        self._head = node_obj
        self._size += 1
    def pop(self):
        """Returns also removes the top element from the stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        value = self._head.getelement()
        self._head = self._head.getnext()
        self._size -= 1
        return value
    
    # ### Practice Problem Q. 1
    # ### Q.1 Write a program to reverse a Singly Linked List (SLL).
    # def reverse(self):
    #     """Returns a New SLL reverse of the given"""
    #     var = self._head
    #     new_lst = Sll_stack()
    #     while var!=None:
    #         new_lst.push(var.getelement())
    #         var = var.getnext()
    #     return new_lst
    
    
 

###-----------------------Testing-----------------------------####
if __name__ == '__main__':
    print("Testing started: ")
    obj = Sll_stack()
    print("Length at starting: ",len(obj))
    print("Is Empty: ", obj.is_empty())
    for i in range(50):
        obj.push(i)
    print("Length after pushing 50 elements: ",len(obj))
    print("Is Empty: ", obj.is_empty())
    print("Top: ", obj.top())
    for i in range(50):
        obj.pop()
    print("Length after poping 50 elements: ",len(obj))
    print("Is Empty: ", obj.is_empty())
        
        
    print("Testing completed")
	