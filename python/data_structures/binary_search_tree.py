from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """


    def add(self, value):

        def walk(root, new_node):
            if not root:
                return
            if new_node.value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node
            

        node_to_add = Node(value)

        if not self.root:
            self.root = Node(value)
            return
            
        walk(self.root, node_to_add)


