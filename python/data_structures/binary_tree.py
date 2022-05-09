class BinaryTree:
    """
    A tree of nodes, starting with a single root, that all contain a value, left, and right.
    With left and right referring to potential child nodes.
    """

    def __init__(self):
        self.root = None

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


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
