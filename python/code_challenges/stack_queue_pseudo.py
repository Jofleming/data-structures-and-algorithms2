from data_structures.stack import Stack


class PseudoQueue:
    
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)

    def dequeue(self):
        if self.outbox.is_empty():
            while self.inbox.is_empty() == False:
                self.outbox.push(self.inbox.pop())
            return self.outbox.pop()
        else:
            return self.outbox.pop()    
