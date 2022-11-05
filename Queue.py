# Queue

class Queue:
  def __init__(self,size):
    self.queue = [None]*size
    self.front = 0
    self.rear = 0
    self.size = size
    self.available = size
 
  def enqueue(self, item):
    if self.available == 0:
      print('Queue Overflow!')
    else:
      self.queue[self.rear] = item
      self.rear = (self.rear + 1) % self.size
      self.available -= 1
 
  def dequeue(self):
    if self.available == self.size:
      print('Queue Underflow!')
    else:
      self.queue[self.front] = None
      self.front = (self.front + 1) % self.size
      self.available += 1
 
  def peek(self):
    print(self.queue[self.front])
 
  def print_queue(self):
    print(self.queue)
 
 
queue1 = Queue(4)
queue1.enqueue(10)
queue1.peek()
queue1.enqueue(20)
queue1.dequeue()
queue1.peek()
 
queue1.print_queue()


## PriorityQueue

from queue import PriorityQueue
 
class PQueue(PriorityQueue):
    def peek(self):
        return self.queue[0]
 
myQueue = PQueue()
myQueue.put(12)
myQueue.put(2)
myQueue.put(1)
myQueue.put(7) 
print(myQueue.peek())

# """Make a Queue class using a list!
# Hint: You can use any Python list method
# you'd like! Try to write each one in as 
# few lines as possible.
# Make sure you pass the test cases too!"""

# class Queue:
#     def __init__(self, head=None):
#         self.storage = [head]

#     def enqueue(self, new_element):
#         self.storage.append(new_element)

#     def peek(self):
#         return self.storage[0]

#     def dequeue(self):
#         return self.storage.pop(0)
    
# # Setup
# q = Queue(1)
# q.enqueue(2)
# q.enqueue(3)

# # Test peek
# # Should be 1
# print (q.peek())

# # Test dequeue
# # Should be 1
# print (q.dequeue())

# # Test enqueue
# q.enqueue(4)
# # Should be 2
# print (q.dequeue())
# # Should be 3
# print (q.dequeue())
# # Should be 4
# print (q.dequeue())
# q.enqueue(5)
# # Should be 5
# print (q.peek())