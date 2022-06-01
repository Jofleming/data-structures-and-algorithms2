from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    A linked list that holds values which will be retrieved in order added. First in first out.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new = Node(value, None)
        if self.is_empty():
            self.front = new
        else:
            self.rear.next = new
        self.rear = new

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

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

