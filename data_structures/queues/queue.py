"""
Queue Implementation using Collections.deque

A queue is a linear data structure that follows the FIFO (First In, First Out) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue).

Time Complexities:
- Enqueue: O(1)
- Dequeue: O(1)
- Front/Rear: O(1)
- Search: O(n)

Space Complexity: O(n)

Common Applications:
- Process scheduling in operating systems
- Breadth-First Search (BFS) in graphs
- Handling requests in web servers
- Print queue management
"""

from collections import deque

class Queue:
    def __init__(self, capacity=None):
        """Initialize an empty queue with optional capacity limit"""
        self.items = deque()
        self.capacity = capacity
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        if self.capacity is not None and len(self.items) >= self.capacity:
            raise Exception("Queue overflow: Queue is full")
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise Exception("Queue underflow: Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]
    
    def rear(self):
        """Return the rear item without removing it"""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def is_full(self):
        """Check if the queue is full (only relevant if capacity is set)"""
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def search(self, item):
        """Search for an item and return its position from front (0-based)"""
        try:
            return list(self.items).index(item)
        except ValueError:
            return -1
    
    def display(self):
        """Display the queue contents (front to rear)"""
        return list(self.items)

class CircularQueue:
    """
    Circular Queue implementation using a fixed-size array
    More memory efficient than regular queue for fixed-size scenarios
    """
    def __init__(self, capacity):
        """Initialize circular queue with fixed capacity"""
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0
    
    def enqueue(self, item):
        """Add an item to the rear of the circular queue"""
        if self.is_full():
            raise Exception("Circular queue overflow: Queue is full")
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.count += 1
    
    def dequeue(self):
        """Remove and return the front item from the circular queue"""
        if self.is_empty():
            raise Exception("Circular queue underflow: Queue is empty")
        
        item = self.items[self.front]
        self.items[self.front] = None
        
        if self.count == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.count -= 1
        return item
    
    def is_empty(self):
        """Check if the circular queue is empty"""
        return self.count == 0
    
    def is_full(self):
        """Check if the circular queue is full"""
        return self.count == self.capacity
    
    def size(self):
        """Return the number of items in the circular queue"""
        return self.count
    
    def display(self):
        """Display the circular queue contents"""
        if self.is_empty():
            return []
        
        result = []
        current = self.front
        for _ in range(self.count):
            result.append(self.items[current])
            current = (current + 1) % self.capacity
        return result

# Example usage
if __name__ == "__main__":
    # Regular Queue
    print("=== Regular Queue ===")
    queue = Queue()
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue.display())
    print("Queue size:", queue.size())
    
    # Check front and rear
    print("Front element:", queue.front())
    print("Rear element:", queue.rear())
    
    # Dequeue elements
    dequeued = queue.dequeue()
    print(f"Dequeued element: {dequeued}")
    print("Queue after dequeue:", queue.display())
    
    # Search for element
    position = queue.search(30)
    print(f"Element 30 is at position: {position}")
    
    # Circular Queue
    print("\n=== Circular Queue ===")
    cq = CircularQueue(5)
    
    # Fill the circular queue
    for i in range(1, 6):
        cq.enqueue(i * 10)
    print("Circular queue (full):", cq.display())
    
    # Dequeue and enqueue to show circular behavior
    cq.dequeue()
    cq.dequeue()
    print("After 2 dequeues:", cq.display())
    
    cq.enqueue(60)
    cq.enqueue(70)
    print("After adding 60, 70:", cq.display())