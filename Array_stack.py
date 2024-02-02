"""
This is a script containing Stack class
In this module a Array based stack is implemented

Author: Shravan
Date: 02-09-2023
"""
from stack_exception import Empty


####---------------------------Array based stack implementation-------------------####
class ArrayStack(object):
	"""LIFO stack implementation using python list as an underlying storage"""

	def __init__(self):
		"""Creates an empty stack"""
		self._data = []

	def __len__(self):
		"""Returns the number of elements in the stack"""
		return len(self._data)

	def is_empty(self):
		"""Returns true if the stack is empty otherwise false"""
		return len(self._data)==0

	def top(self):
		"""
		Returns (but do not remove)the element at the top of the stack

		Raise Empty exception if the stack is empty
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data[-1]

	def push(self, e):
		"""Adds element e to the stack"""
		self._data.append(e)

	def pop(self):
		"""
		Return and remove the element at the top of the stack

		Raise Empty exception if the stack is empty
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._data.pop()


#-------------------Testing----------------------#

if __name__ == '__main__':
	print("Testing started: ")
	obj = ArrayStack()
	print("Length at starting: ",len(obj))
	print("Is Empty: ", obj.is_empty())
	for i in range(50):
		obj.push(i)
	print("Length after pushing 50 elements: ",len(obj))
	print("Is Empty: ", obj.is_empty())
	print("Top: ", obj.top())
	for i in range(50):
		obj.pop()
	print("Testing completed")
