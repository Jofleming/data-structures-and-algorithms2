class Queue:
    """
    A linked list that holds values which will be retrieved in order added. First in first out.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.rear = Node(value)
            self.front = self.rear

    def dequeue(self): 
        if self.front is None:
            raise InvalidOperationError
        temp_value = self.front
        self.front = self.front.next
        temp_value.next = None
        return temp_value.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        else:
            return self.front.value


    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False



class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    '''
    Custom error
    '''
