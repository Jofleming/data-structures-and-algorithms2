from python.data_structures.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size


    def hash(self, key):
        char_sum = 0
        if type(key) is str:
            for char in key:
                char_sum += ord(char)
        elif type(key) is int:
                char_sum = key
        primed = char_sum * 599
        index = primed % self.size
        return index

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]
            current = current.next
        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        if bucket is None:
            return False
        current = bucket.head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False
        

    def keys(self):
        keys = set()
        for bucket in self.buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    keys.add(current_key)
                    current = current.next
        return keys

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = LinkedList()
        
        bucket.insert((key, value))