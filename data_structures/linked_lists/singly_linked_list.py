"""
Singly Linked List Implementation

A linked list is a linear data structure where elements are stored in nodes,
and each node contains data and a reference to the next node.

Time Complexities:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) at arbitrary position
- Deletion: O(1) at head, O(n) at arbitrary position

Space Complexity: O(n)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_at_head(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def insert_at_position(self, position, data):
        """Insert a new node at the given position"""
        if position < 0 or position > self.size:
            raise Exception("Position out of bounds")
        
        if position == 0:
            self.insert_at_head(data)
            return
        
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at_head(self):
        """Delete the first node"""
        if not self.head:
            raise Exception("List is empty")
        
        self.head = self.head.next
        self.size -= 1
    
    def delete_at_tail(self):
        """Delete the last node"""
        if not self.head:
            raise Exception("List is empty")
        
        if not self.head.next:
            self.head = None
            self.size -= 1
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.size -= 1
    
    def delete_by_value(self, value):
        """Delete the first node with the given value"""
        if not self.head:
            return False
        
        if self.head.data == value:
            self.delete_at_head()
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False
    
    def search(self, value):
        """Search for a value and return its position"""
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1
    
    def display(self):
        """Display all elements in the list"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def get_size(self):
        """Return the size of the list"""
        return self.size
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None

# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    
    # Insert elements
    ll.insert_at_head(10)
    ll.insert_at_head(20)
    ll.insert_at_tail(30)
    ll.insert_at_position(1, 15)
    print("Linked List:", ll.display())
    print("Size:", ll.get_size())
    
    # Search for element
    position = ll.search(15)
    print(f"Element 15 found at position: {position}")
    
    # Delete elements
    ll.delete_by_value(15)
    print("After deleting 15:", ll.display())
    
    ll.delete_at_head()
    print("After deleting head:", ll.display())
    
    ll.delete_at_tail()
    print("After deleting tail:", ll.display())