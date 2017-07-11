# This class implements a simple Queue data structure
# A Queue is a FIFO (first in, first out) data structure
# More on queues: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

class Queue:
    queue = []

    # Push adds a new value to the top of the queue
    def enqueue(self, item):
        self.queue.append(item);

    # Pop removes the top value from the queue
    def dequeue(self):
        if(self.size() != 0):
            # Remove and return the top value
            return self.queue.pop(0)
        # Otherwise, return None
        return None

    # Peek returns the value of the next value on the queue
    def peek(self):
        if(self.size() != 0):
            # Return the first value
            return self.queue[0]
        # Otherwise, return None
        return None

    # Size returns the number of items in the queue
    def size(self):
        return len(self.queue)

    # isEmpty returns a boolean if the queue is empty (i.e., has no items)
    def isEmpty(self):
        return self.size() == 0

    # printQueue iterates over the queue and prints the items
    def printQueue(self):
        for item in self.queue:
            print(item)
