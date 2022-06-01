from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    common_numbers = []

    ht = Hashtable()
    for num in tree_a.pre_order():
        ht.set(num, num)

    for num in tree_b.pre_order():
        if ht.contains(num):
            if num not in common_numbers:
                common_numbers.append(num)

    return common_numbers

