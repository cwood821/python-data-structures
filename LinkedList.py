# This pair of classes implements a simple, singly Linked List data structure
# More on Linked Lists here: https://en.wikipedia.org/wiki/Linked_list


class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next



class LinkedList:

    def __init__(self, firstNode):
        self.firstNode = firstNode


    def search(self, searchNode):
        curNode = self.firstNode
        # Find the beforeNode node
        while(curNode.next != None):
            if (curNode.data == searchNode.data):
                return curNode
            curNode = curNode.next
        # Reached the end, return false
        return False

    def size(self):
        curNode = self.firstNode

        # If ther first node is not null, default size to 1
        if(curNode.data != None):
            counter = 1
        else:
            counter = 0

        while(curNode.next != None):
            curNode = curNode.next
            counter = counter + 1

        return counter

    # Insert a node to the end of the list
    def insert(self, newNode):
        # Get the root node
        curNode = self.firstNode;

        while(curNode.next != None):
            curNode = curNode.next

        # The next node is None, so add the new Node here
        curNode.next = newNode

    # Insert a node after a given node
    def insertAfter(self, afterNode, newNode):
        # Get the root node
        curNode = self.firstNode;

        # Find the given node
        while(curNode.data != afterNode.data):
            curNode = curNode.next

        # Either the node was the last one, or no matching
        # node was found, so just add it to the end
        if (curNode.next == None):
            curNode.next = newNode
            return curNode.next

        # Otherwise, insert the newNode between the curNode and curNode.nextNode
        newNode.next = curNode.next
        curNode.next = newNode

    # Insert a node before a given node
    def insertBefore(self, beforeNode, newNode):
        # Get the root node
        curNode = self.firstNode;

        # If the beforeNode is the first, swap them
        if (curNode.data == beforeNode.data):
            newNode.next = curNode
            self.firstNode = newNode

        # Find the beforeNode node
        while(curNode.next.data != None and curNode.next.data != beforeNode.data):
            curNode = curNode.next

        # Insert the newNode before the curNode
        newNode.next = curNode.next
        curNode.next = newNode

    # Remove the given node from the list
    def remove(self, deleteNode):
        curNode = self.firstNode

        # If the node to delete is the first
        if (curNode.data == deleteNode.data):
            self.firstNode = curNode.next
            return

        # Iterate through the nodes
        while (curNode.next != None and curNode.next.data != deleteNode.data):
            curNode = curNode.next

        # Reached the end, the given node doesn't exist
        if (curNode.next == None):
            return False

        # Otherwise, set next to skip over the deleteNode
        curNode.next = curNode.next.next

    def printList(self):
        curNode = self.firstNode;
        # Print the root node
        print(curNode.data)
        # Print the successive nodes
        while(curNode.next != None):
            curNode = curNode.next
            print(curNode.data)
