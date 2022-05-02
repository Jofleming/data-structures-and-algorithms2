class Stack:
    """
    A linked list of values that resolves Last in First Out.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value, self.top)
        self.top = node

    def pop(self):
        if not self.top:
            raise InvalidOperationError('Method not allowed on empty collection')
        value_holder = self.top
        self.top = self.top.next
        return value_holder.value


    def peek(self):
        if not self.top:
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class InvalidOperationError(Exception):
    '''
    Insert custom exception.
    '''
    pass
