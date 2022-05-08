# Stacks and Queues

## Challenge

To implement a stack and a queue class. Both should have an enqueue/push, dequeue/pop, peek, and is empty methods. They both should use a Node under the hood.

## Approach & Efficiency

Using the provided tests, created single responsibility methods.

For the methods, they are all O(1) for time and space. As they do single operations on a queue or stack.  
The class itself can hold n nodes and if creating a n long stack/queue from nothing would take n steps.

## API

Queue:
enqueue - enters a new node at the end of the queue.
dequeue - remove the top of the queue
peek - view the value of the first node in the queue
is_empty - checks to see if the queue is empty. Returns True or False.

Stack:
push - pushes a new node onto the top of the stack
pop - removes the node on the top of the stack
peek - returns the value of the top of the stack
is_empty - checks to see if the stack is empty. Returns True or False.