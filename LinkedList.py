# This pair of classes implement a simple, singly Linked List data structure
# More on Linked Lists here: https://en.wikipedia.org/wiki/Linked_list


class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next



class LinkedList:

    def __init__(self, firstNode = Node(None, None)):
        self.firstNode = firstNode


    def search(self, searchData):
        curNode = self.firstNode
        # Find the beforeNode node
        while(curNode.next != None):
            if (curNode.data == searchData):
                return curNode
            curNode = curNode.next
        # Reached the end, return false
        return False

    def size(self):
        curNode = self.firstNode
        # If ther first node is null, return 0
        if(curNode.data == None):
            return 0

        counter = 1

        while(curNode.next != None):
            curNode = curNode.next
            counter = counter + 1

        return counter

    # Insert a node to the end of the list
    def insert(self, newData):
        # Get the root node
        curNode = self.firstNode;

        # If the first node is None, insert it there
        if (curNode.data == None):
            curNode.data = newData
            return

        # Iterate to the end of the list
        while(curNode.next != None):
            curNode = curNode.next

        # The next node is None, so add the new Node here
        curNode.next = Node(newData, None)

    # Insert a node after a given node
    def insertAfter(self, afterData, newData):
        # Get the root node
        curNode = self.firstNode;

        # Find the given node
        while(curNode.data != afterData):
            # If the next node is the last one, just add it t
            # Question: What's the expected behaviour for insertAfter at the
            # end of a list when you haven't found the search data?
            if (curNode.next == None):
                curNode.next = Node(newData, None)
                return False

            curNode = curNode.next

        # Otherwise, insert the newNode between the curNode and curNode.nextNode
        newNode = Node(newData, None)
        newNode.next = curNode.next
        curNode.next = newNode

        return newNode

    # Insert a node before a given node
    def insertBefore(self, beforeData, newData):
        # Get the root node
        curNode = self.firstNode;

        # If the beforeNode is the first, swap them
        if (curNode.data == beforeData):
            newNode = Node(newData, curNode)
            self.firstNode = newNode

        # Find the beforeNode node
        while(curNode.next.data != None and curNode.next.data != beforeData):
            curNode = curNode.next

        # Insert the newNode before the curNode
        newNode = Node(newData, curNode.next)
        # newNode.next = curNode.next
        curNode.next = newNode

    # Remove the given node from the list
    def remove(self, deleteData):
        curNode = self.firstNode

        # If the node to delete is the first
        if (curNode.data == deleteData):
            self.firstNode = curNode.next
            return

        # Iterate through the nodes
        while (curNode.next != None and curNode.next.data != deleteData):
            curNode = curNode.next

        # Reached the end, the given node doesn't exist
        if (curNode.next == None):
            return False

        # Otherwise, found it. Set next to skip over the deleteData node
        curNode.next = curNode.next.next

        return True

    def printList(self):
        curNode = self.firstNode;
        # Print the root node
        print(curNode.data)
        # Print the successive nodes
        while(curNode.next != None):
            curNode = curNode.next
            print(curNode.data)
