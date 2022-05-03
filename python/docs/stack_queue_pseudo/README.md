# Challange Summary

To create a new class called pseudo queue that acts like the queue we made before, but under the hood uses two stacks.

## Whiteboard Process
![pseudo-queue-whiteboard](White-Board.png)


## Approach and Efficiency

The approach I took was what we talked about in class. Initalizing with an inbox and outbox that are each a stack. I will then enqueue into the inbox. In order to return a value wanted, I pop and push from the inbox to the outbox, which will reverse the order to what we want. I finally pop and return from the outbox. We decided in class that it would be better to just check if the outbox is empty before emptying the inbox into it, that way you don't have to empty the outbox back into the inbox every time.

For enqueue big O of time is 1 and space is 1. It just takes in a single value and handles that single value.
For dequeue big O of time is N and space is 1. It potentially has to go through N amount in the inbox. It doesn't add anything though.
For the entire class big O of time is N and space is N. Worst case would be having to add an infinitely long list.