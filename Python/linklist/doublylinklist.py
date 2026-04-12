"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(k) Initializes the deque with size k.
insertFront(value) Inserts an item at the front. Returns true if the operation is successful.
insertLast(value) Adds an item at the rear. Returns true if the operation is successful.
deleteFront() Deletes an item from the front. Returns true if the operation is successful.
deleteLast() Deletes an item from the rear. Returns true if the operation is successful.
getFront() Gets the front item. If empty, return -1.
getRear() Gets the last item. If empty, return -1.
isEmpty() Checks whether the deque is empty.
isFull() Checks whether the deque is full.
Example

Input:
[
  "MyCircularDeque",
  "insertLast",
  "insertLast",
  "insertFront",
  "insertFront",
  "getRear",
  "isFull",
  "deleteLast",
  "insertFront",
  "getFront"
]
[[3],[1],[2],[3],[4],[],[],[],[4],[]]

Output:
[null,true,true,true,false,2,true,true,true,4]
"""


class Node:
    def __init__(self, k: int = 0):
        self.front = None
        self.rear = None
        self.size = k

