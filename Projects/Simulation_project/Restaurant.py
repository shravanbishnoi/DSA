"""
DSA Project

Author: Shravan
Date: 22 Nov 2023
"""

from sll_queue import Sll_queue
from Priority_Queue import HeapPriorityQueue

class Restaurant(object):
    """
    Class representing a restaurant simulation.
    """
    class _Customer(object):
        """Represents a customer"""
        __slots__ = '_id', '_time', '_burgers', '_state', '_leave'

        def __init__(self, id, t, numb):
            """Initializes a customer object"""
            self._id = id             # unique id of customer
            self._time = t            # arrival time
            self._burgers = numb      # no. of burgers to order
            self._state = "arrived"   # initial state
            self._leave = 0           # total time get burgers

    ### CLASS VARIABLE ##
    TIME = 0 # Global clock
    def __init__(self, k, m):
        self._customers =  []               # all the customers
        self._counters = []                 # all the counters
        self._m = 0                         # burgers on griddle simultaneously
        self._priorityQueue = HeapPriorityQueue(k) # keys as length, values as counter number
        self._setK(k)
        self._setM(m)
        
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
            counter = Sll_queue(self._priorityQueue._data[i])               # initializing a queue
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
            print(f"time {self.TIME}")
            self._advanceBilling()
            self._addCustomer(prevtime)
        
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
        print(f"customer id: {id} arrived at {t}")

    def customerState(self, id, t):
        """Prints the state of the customer with the given."""
        assert type(id)==int, f"{str(id)} must be an integer"
        assert type(t)==int, f"{str(t)} must be an integer"
        assert id>0, f"{str(id)} must be positive integer"
        assert t>0, f"{str(t)} must be positive integer"   # must be greater than previous
        for customer in self._customers:
            if customer._id == id:
                print(customer._state)
        return 0

    def griddleState(self, t):
        """Returns the number of burger patties on the griddle at time t."""
        pass

    def griddleWait(self, t):
        """Returns the number of burger patties waiting to be cooked at time t,
        i.e. the number of burgers for which order has been placed but cooking has not yet started.
        """
        pass
        

    def customerWaitTime(id):
        """"""
        pass

    def avgWaitTime():
        """"""
        pass

    def _advanceBilling(self):
        for index, counter in enumerate(self._counters):
            if not(counter.is_empty()):
                while ((counter.first()._leave)) == self.TIME:
                    counter.first()._state = "waiting for food"
                    print(f"Customer with id: {counter.first()._id} joined food line")
                    self._priorityQueue.update(self._priorityQueue.getIndex(counter._heapitem), -1)
                    counter.dequeue()
                    if counter.is_empty():
                        break
                    
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
                self._counters[counter].enqueue(customer)    # adding to counter queue
                customer._state = "waiting in queue"          # updating customer state
                print(f"Customer with id: {customer._id} joined counter {counter+1}")
            else:
                continue


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