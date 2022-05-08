class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None
        

    def __str__(self):
        temp_string = ''
        current = self.head
        while current:
            temp_string += f'{{ {current.value} }} -> '
            current = current.next
        temp_string += 'NULL'
        return temp_string
    
    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        new_node = Node(value)
        current = self.head
        if not self.head:
            self.head = new_node
            return
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, query, value):
        if not self.head:
            raise TargetError
        elif self.head.value == query:
            self.insert(value)
            return
        current = self.head
        while current:
            try:
                if current.next.value == query:
                    old_next = current.next
                    current.next = Node(value, old_next)
                    break
                current = current.next
            except:
                raise TargetError

    def insert_after(self, query, value):
        if self.head is None:
            raise TargetError
        current = self.head
        while current:
            if current.value == query:
                current.next = Node(value, current.next)
                break
            if current.next is None:
                raise TargetError
            current = current.next
        
    def includes(self, query):
        current = self.head
        while current:
            if current.value == query:
                return True
            current = current.next
        return False

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError
        length = 0
        current = self.head
        while current.next:
            length += 1
            current = current.next
        n = length - k
        if n < 0:
            raise TargetError
        new_current = self.head
        for _ in range(n):
            new_current = new_current.next
        return new_current.value

class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class TargetError(Exception):
    '''
    Custom Exception
    '''
