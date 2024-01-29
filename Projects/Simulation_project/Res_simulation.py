"""
DSA Simulation Project

Author: Shravan
Date: 22 Nov 2023
"""

from sll_queue import Sll_queue
from Priority_Queue import HeapPriorityQueue
from Dll_Deque import Dll_Deque

class Restaurant(object):
    """
    Class representing a restaurant simulation.
    """
    class _Customer(object):
        """Represents a customer"""
        __slots__ = '_id', '_time', '_burgers', '_state', '_leave'

        def __init__(self, id, t, numb):
            """Initializes a customer object"""
            self._id = id                   # unique id of customer
            self._time = t                  # arrival time
            self._burgers = numb            # no. of burgers to order
            self._state = "arrived"         # initial state
            self._leave = 0                 # total time to get burgers

    ### CLASS VARIABLE ##
    TIME = 0                                # Global clock
    def __init__(self, k, m):
        self._customers =  []               # all the customers
        self._counters = []                 # all the counters
        self._m = 0                         # burgers on griddle simultaneously
        self._priorityQueue = HeapPriorityQueue(k) # keys as length, values as counter number
        self._setK(k)
        self._setM(m)
        self._cookingQueue = Dll_Deque()
        self._burgersInLine = 0
        self._griddle = []
        self._burgersToDeliver = []
        
    def isEmpty(self):
        """Returns 1(int) if there are no further events to simulate."""
        for i in self._counters:
            if not(i.is_empty()):
                return False
        # check for others
        return 1

    def _setK(self, k):
        """Initializes k number of queues one for each counter"""
        assert type(k)==int, f"{str(k)} must be an integer"
        assert k>0, f"{str(k)} must be a positive integer"
        if len(self._counters)!=0:
            raise AssertionError("Counters can't be modified")
        for i in range(k):
            counter = Sll_queue(self._priorityQueue._data[i])        # initializing a queue
            self._counters.append(counter)                           # adds queue to _counter

    def _setM(self, m):
        """Sets the _m as m(number of patties that can be cooked simultaneously)"""
        assert type(m)==int, f"{str(m)} must be an integer"
        assert m>0, f"{str(m)} must be a positive integer"
        if self._m!=0:
            raise AssertionError("Burgers that can be cooked simultaneously can't be modified")
        self._m = m

    def advanceTime(self, t):
        """"""
        assert type(t)==int, f"{str(t)} must be an integer"
        for i in range(t):
            prevtime = self.TIME
            self.TIME += 1
            # print(f"time {self.TIME}")
            self._advanceBilling()
            # self._removePatties()
            # self._addPatties()
            self._addCustomer(prevtime)
            # self._deliverPatties()
        
    def arriveCustomer(self, id, t, numb):
        """Creates a customer object and adds it to customer record."""
        intcont = "must be an integer"
        posint = "must be positive integer"
        assert type(id)==int, f"{str(id)} {intcont}"
        assert type(t)==int, f"{str(t)} {intcont}"
        assert type(numb)==int, f"{str(numb)} {intcont}"
        assert id>0, f"{str(id)} {posint}"
        assert t>0, f"{str(t)} {posint}"
        if len(self._customers)!=0:
            assert t>=self._customers[-1]._time, f"{str(t)} must be greater than or equal to {str(self._customers[-1]._time)}"
        assert numb>0, f"{str(numb)} {posint}"
        if len(self._customers)==0:
            assert id==1, f"{str(id)} must be start with 1"
        else:
            assert len(self._customers)+1==id, f"{str(id)} must be consecutive"
        customer = self._Customer(id, t, numb)
        self._customers.append(customer)
        # print(f"customer id: {id} arrived at {t}")

    def customerState(self, id, t):
        """Prints the state of the customer with the given."""
        assert type(id)==int, f"{str(id)} must be an integer"
        assert type(t)==int, f"{str(t)} must be an integer"
        assert id>0, f"{str(id)} must be positive integer"
        assert t>0, f"{str(t)} must be positive integer"    # must be greater than previous
        for customer in self._customers:
            if customer._id == id:
                print(customer._state)
        return 0

    def griddleState(self, t):
        """Returns the number of burger patties on the griddle at time t."""
        assert type(t)==int, f"{str(t)} must be an integer"
        assert t>0, f"{str(t)} must be positive integer"   # must be greater than previous
        return len(self._griddle)

    def griddleWait(self, t):
        """Returns the number of burger patties waiting to be cooked at time t,
        i.e. the number of burgers for which order has been placed but cooking has not yet started.
        """
        return self._burgersInLine - len(self._griddle)
        

    def customerWaitTime(id):
        """"""
        pass

    def avgWaitTime():
        """"""
        pass

    def _advanceBilling(self):
        tempDeque = Dll_Deque()
        for index, counter in enumerate(self._counters):
            if not(counter.is_empty()):
                while ((counter.first()._leave)) == self.TIME:
                    counter.first()._state = "waiting for food"
                    print(f"Customer with id: {counter.first()._id} joined food line at {self.TIME}")
                    self._priorityQueue.update(self._priorityQueue.getIndex(counter._heapitem), -1)
                    customerLeft = counter.dequeue()
                    self._burgersInLine += customerLeft._burgers
                    tempDeque.insert_first(customerLeft)
                    # print("First element time: ",tempDeque.first()._time)
                    if counter.is_empty():
                        break
        if not(tempDeque.is_empty()):
            self._cookingQueue.concatenate(tempDeque)
        # print(self._burgersInLine)
        # print("Length of Cooking Queue: ",len(self._cookingQueue))

    def _addCustomer(self, prevtime):
        """Adds customer to the appropriate billing queue"""
        for customer in self._customers:
            if prevtime < customer._time <= self.TIME:
                length, counter = self._priorityQueue.min()         # counter with minimum no. of customer
                self._priorityQueue.update_rootkey(1)               # restoring heap property
                if self._counters[counter].is_empty():
                    customer._leave = customer._time + counter+1
                else:
                    customer._leave = customer._time + (length)*(counter+1) + (self._counters[counter].first()._leave - self.TIME)
                self._counters[counter].enqueue(customer)           # adding to counter queue
                customer._state = "waiting in queue"                # updating customer state
                print(f"Customer with id: {customer._id} joined counter {counter+1} at {self.TIME}")
            else:
                continue
        

    def _removePatties(self):
        """Removes cooked patties from the griddle."""
        if len(self._griddle)!=0:
            while (self._griddle[0]+10==self.TIME):
                self._griddle.pop(0)
                self._burgersInLine -= 1
                # print(len(self._cookingQueue))
                self._cookingQueue.first()._burgers -= 1
                if self._cookingQueue.first()._burgers == 0:
                    customerLeft = self._cookingQueue.delete_first()
                    customerLeft._leave = self.TIME + 1
                    self._burgersToDeliver.append(customerLeft)
                    # print("G",len(self._griddle))
                if len(self._griddle)==0:
                    break

    
    def _addPatties(self):
        """Puts on patties on the griddle till the griddle is at its max capacity."""
        while self.griddleState(self.TIME) < self._m:
            self._griddle.append(self.TIME)

    def _deliverPatties(self):
        if len(self._burgersToDeliver)!=0:
            while (self._burgersToDeliver[0]._leave)==self.TIME:
                customerLeft = self._burgersToDeliver.pop(0)
                customerLeft._state = "Order completed! Left the building."
                if len(self._burgersToDeliver) == 0:
                    break


###-----------------------Testing-----------------------------####

if __name__ == '__main__':
    s = Restaurant(2,5)
    s.arriveCustomer(1,1,1)
    s.arriveCustomer(2,1,1)
    s.arriveCustomer(3,1,3)
    s.arriveCustomer(4,2,1)
    s.arriveCustomer(5,2,1)
    s.arriveCustomer(6,3,1)
    s.arriveCustomer(7,3,1)
    s.advanceTime(1)
    s.advanceTime(2)
    s.advanceTime(3) 
    s.advanceTime(4)
    s.advanceTime(5)
    s.advanceTime(6)


































# import queue

# class Restaurant(object):
#     """
#     Class representing a restaurant simulation.
#     """
#     class _Customer(object):
#         """Represents a customer"""

#         def __init__(self, id, t, numb):
#             """Initializes a customer object"""
#             self.id = id             # unique id
#             self.time = t            # arrival time
#             self.burgers = numb      # no. of burgers to order
#             self.state = "arrived"   # first state

#     ### CLASS VARIABLE ##
#     TIME = 0 # Global clock
#     def __init__(self):
#         self._customers =  []        # all the customers
#         self._counters = []          # all the counters
#         self._m = 0                  # burgers on griddle simultaneously

#     def isEmpty(self):
#         """Returns 1(int) if there are no further events to simulate."""
#         for i in self._counters:
#             if not(i.empty()):
#                 return False
#         return 1

#     def _setK(self, k):
#         """Initializes k number of queues one for each counter"""
#         assert type(k)==int, f"{str(k)} must be an integer"
#         assert k>0, f"{str(k)} must be a positive integer"
#         if len(self._counters)!=0:
#             raise AssertionError("Counters can't be modified")
#         for i in range(k):
#             self._counters.append(queue.Queue())

#     def _setM(self, m):
#         """Sets the _m as m(number of patties that can be cooked simultaneously)"""
#         assert type(m)==int, f"{str(m)} must be an integer"
#         assert m>0, f"{str(m)} must be a positive integer"
#         if self._m!=0:
#             raise AssertionError("Burgers that can be cooked simultaneously can't be modified")
#         self._m = m

#     def advanceTime(self, t):
#         """"""
#         assert type(t)==int, f"{str(t)} must be an integer"
#         prevtime = self.TIME
#         self.TIME += t
#         self._advanceBilling()
#         self._addCustomer(prevtime)
        

#     def arriveCustomer(self, id, t, numb):
#         """Creates a customer object and adds it to customer record."""
#         intcont = "must be an integer"
#         posint = "must be positive integer"
#         assert type(id)==int, f"{str(id)} {intcont}"
#         assert type(t)==int, f"{str(t)} {intcont}"
#         assert type(numb)==int, f"{str(numb)} {intcont}"
#         assert id>0, f"{str(id)} {posint}"
#         assert t>0, f"{str(t)} {posint}"
#         if len(self._customers)!=0:
#             assert t>=self._customers[-1].time, f"{str(t)} must be greater than or equal to {str(self._customers[-1].time)}"
#         assert numb>0, f"{str(numb)} {posint}"
#         if len(self._customers)==0:
#             assert id==1, f"{str(id)} must be start with 1"
#         else:
#             assert len(self._customers)+1==id, f"{str(id)} must be consecutive"
#         customer = self._Customer(id, t, numb)
#         self._customers.append(customer)

#     def customerState(self, id, t):
#         """"""
#         assert type(id)==int, f"{str(id)} must be an integer"
#         assert type(t)==int, f"{str(t)} must be an integer"
#         assert id>0, f"{str(id)} must be positive integer"
#         assert t>0, f"{str(t)} must be positive integer"
#         for customer in self._customers:
#             if customer.id==id:
#                 pass
#                 # do we need to increase time for individual
#         return 0

#     def griddleState(t):
#         """"""
#         pass

#     def griddleWait(t):
#         """"""
#         pass

#     def customerWaitTime(id):
#         """"""
#         pass

#     def avgWaitTime():
#         """"""
#         pass

#     def _advanceBilling(self):
#         for counter in range(len(self._counters)):
#             if not(self._counters[counter].empty()):
#                 while (self._counters[counter].queue[0].time)+(counter+1) <= self.TIME:
#                     self._counters[counter].queue[0].state = "waiting for food"
#                     self._counters[counter].get()
#                     if self._counters[counter].empty():
#                         break

#     def _addCustomer(self, prevtime):
#         """Adds customer to the appropriate billing queue"""
#         for customer in self._customers:
#             if prevtime<customer.time<=self.TIME:
#                 shortestQueue = self._counters[0]
#                 for counter in self._counters:
#                     if counter.qsize()<shortestQueue.qsize():
#                         shortestQueue = counter
#                     else:
#                         continue
#                 shortestQueue.put(customer)
#                 customer.state = "waiting in queue"
#             else:
#                 continue


# ###-----------------------Testing-----------------------------####

# if __name__ == '__main__':
#     res = Restaurant()
#     res._setK(4)
#     res._setM(5)
#     res.isEmpty()
#     # print(res.isEmpty())
#     for i in range(10):
#         res.arriveCustomer(i+1, i+10, i+1)
#     res.advanceTime(15)
#     for i in res._counters:
#         print(i.qsize())
#     print("Success")
