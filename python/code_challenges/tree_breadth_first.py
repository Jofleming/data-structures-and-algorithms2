from data_structures.queue import Queue


def breadth_first(tree):
    breadth = Queue()
    list_of_values = []

    if not tree or tree.root is None:
        return list_of_values
    if not breadth.front:
        breadth.enqueue(tree.root)
    while breadth.front:
        root = breadth.dequeue()
        list_of_values.append(root.value)
        if root.left:
            breadth.enqueue(root.left)
        if root.right:
            breadth.enqueue(root.right)
    return list_of_values
