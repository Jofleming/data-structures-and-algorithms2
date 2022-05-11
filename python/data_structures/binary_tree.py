from data_structures.queue import Queue

class BinaryTree:
    """
    A tree of nodes, starting with a single root, that all contain a value, left, and right.
    With left and right referring to potential child nodes.
    """

    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)

    def pre_order(self):
        '''
        
        '''
        def walk(root, values):
            # If empty return. This is base case
            if not root:
                return
            # Append value to list
            values.append(root.value)
            # Recursively go left
            walk(root.left, values)
            # Recursively go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        '''
        Add in the order of left, root, right.
        '''
        def walk(root, values):
            # Base case
            if not root:
                return
            # Recursively go left
            walk(root.left, values)
            # Append value of node
            values.append(root.value)
            # Recursively go right
            walk(root.right, values)
        
        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        '''
        Order is left, right, append.
        '''
        ordered_values = []

        def walk(root, values):
            if not root:
                return
            walk(root.left, values)
            walk(root.right, values)
            values.append(root.value)
        
        walk(self.root, ordered_values)

        return ordered_values

    def find_maximum_value(self):

        def walk(root, values):
            if not root:
                return values
            if root.value > values:
                values = root.value
            values = walk(root.left, values)
            values = walk(root.right, values)
            return values

        max_value = walk(self.root, 0)

        return max_value

    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)



class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
