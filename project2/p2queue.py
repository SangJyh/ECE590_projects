"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1:
Partner 2:
Date:
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        # if queue is full -> resize and return True
        if len(self.queue) <= self.rear:
            return True
        else: return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        # if queue is empty -> return True
        if self.rear == self.front:
            return True
        else: return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # double queue size
        size = len(self.queue)
        newqueue = self.queue + [None for x in range(0,size)]# doubling size
        
        #implement code to reset the queue
        k =0
        for i in self.queue:
            if i is not None:
                newqueue[k] = i # assign values only when original queue is not empty
                k+=1
        self.queue = newqueue
        self.rear = self.rear - self.front #set rear to the correct postition
        self.front = 0 #reset front
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        #push to the end of the queue
        self.queue[self.rear] = val #assign value to position rear
        self.numElems +=1
        self.rear +=1 #move rear to the next None
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        val, self.queue[self.front] = self.queue[self.front], None
        self.front +=1
        self.numElems -=1
        return val
