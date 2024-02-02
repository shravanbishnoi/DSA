'''
This is a script containing Queue class
In this module a array based queue is implemented

Author: Shravan
Date: 07-09-2023
'''
from queue_exception import Empty

####-----------------------------------Array based queue----------------------------####
class ArrayQueue(object):
	"""
	FIFO queue implementation using python list as an underlying storage
	"""
	CAPACITY = 10

	def __init__(self):
		"""Creates an empty Queue"""
		self._data = [None]*ArrayQueue.CAPACITY
		self._size = 0 # no. of elements
		self._front = 0 # int represents index of first element in _data

	def __len__(self):
		"""Returns the number of elements in the Queue"""
		return self._size

	def is_empty(self):
		"""Returns true if the Queue is empty otherwise false"""
		return self._size==0

	def first(self):
		"""
		Returns (but do not remove)the first element of the Queue

		Raise Empty exception if the Queue is empty
		"""
		if self.is_empty():
			raise Empty("Queue is empty")
		return self._data[self._front]

	def enqueue(self, e):
		"""Adds element e to the Queue"""
		if self._size==len(self._data):
			self._resize(2*len(self._data))
		blank_idx = (self._front + self._size)%len(self._data)
		self._data[blank_idx] = e
		self._size += 1

	def dequeue(self):
		"""
		Return and remove the first element of the Queue
		
		Raise Empty exception if the Queue is empty
		"""
		if self.is_empty():
			raise Empty("Queue is empty")
		value = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1)%len(self._data)
		self._size -= 1
		if 0<self._size<len(self._data)//4:
			self._resize(len(self._data)//2)
		return value

	def _resize(self, cap):
		"""
		Resizes the _data to double
		"""
		old_data = self._data
		self._data = [None]*cap
		front = self._front
		for i in range(self._size):
			self._data[i] = old_data[front]
			front = (front + 1)%len(old_data)
		self._front = 0


###-----------------------Testing-----------------------------####

if __name__ == '__main__':
	print("Testing started: ")
	obj = ArrayQueue()
	print("Length at starting: ",len(obj))
	print("Is Empty: ", obj.is_empty())
	for i in range(50):
		obj.enqueue(i)
	print("Length after Enqueuing 50 elements: ",len(obj))
	print("Is Empty: ", obj.is_empty())
	print("First element: ", obj.first())
	for i in range(50):
		obj.dequeue()

	print("Testing completed")
