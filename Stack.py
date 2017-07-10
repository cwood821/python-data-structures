# This class implements a simple Stack data structure
# A Stack is a LIFO (for last in, first out) data structure
# More on stacks: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

class Stack:
    stack = []

    # Push adds a new value to the top of the stack
    def push(self, item):
        self.stack.insert(0, item);

    # Pop removes the top value from the stack
    def pop(self):
        if(self.size() != 0):
            # Remove and return the top value
            return self.stack.pop(0)
        # Otherwise, return None
        return None

    # Peek returns the value of the next value on the stack
    def peek(self):
        if(self.size() != 0):
            # Return the top value
            return self.stack[0]
        # Otherwise, return None
        return None

    # Size returns the number of items in the stack
    def size(self):
        return len(self.stack)

    # isEmpty returns a boolean if the stack is empty (i.e., has no items)
    def isEmpty(self):
        return self.size() == 0

    # printStack iterates over the stack and prints the items
    def printStack(self):
        for item in self.stack:
            print(item)
