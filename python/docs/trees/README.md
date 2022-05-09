# Trees

## Challenge

To create a Node class that contains properties for value, left child, and right child. Then to create a Binary Tree class using Nodes. This class should have a pre-order, in order, and post order which all return an array of the values in the tree in the order they walk through it. Lastly create a Binary Search Tree class that is a sub-class of the Binary Tree. It should contain an Add and Contains methods. Add should add a new Node in the correct location according to a Binary Search Tree's rules. Contains should be able to look for a given value in the tree and return True if it is there and False if it is not.

## Approach & Efficiency

The time and space of `Add` is 1, since it just creates one node and adds it to the tree. Space of `Contains`is 1 and time is n, this is because it just returns a boolean but has to walk potentially n spaces looking for a value. For the methods in Binary Tree they are all space n, time n. Since they walk through the entire tree, appending the values to a list.

## API

### Binary Tree:

Pre order: Defines a walk function for this method. Then recursively calls it to move through the tree and append the values to a list. At the end returns the list. Will talk through and append in the order of root -> left -> right

In order: Defines a walk function for this method. Then recursively calls it to move through the tree and append the values to a list. At the end returns the list. Will talk through and append in the order of left -> root -> right

Post Order: Defines a walk function for this method. Then recursively calls it to move through the tree and append the values to a list. At the end returns the list. Will talk through and append in the order of left -> right -> root

### Binary Search Tree:

Add: Will take in a value to add, navigate through the Binary Search Tree using the rules of lower values to the left, higher to the right. Until it finds a space to put a new node. It will then add that value to the tree in a Node using that space.

Contains: Will take in a value to search for. It will then use the lower values to the left/higher values to the right rule to navigate through the tree until it finds the value or the end of a leaf. If the value is in the tree it will return True. If not it will return False. If the tree is empty it will also return False.