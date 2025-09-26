"""
Array Operations - Basic array manipulation examples

Arrays are one of the most fundamental data structures. They store elements 
in contiguous memory locations and provide O(1) access time by index.

Time Complexities:
- Access: O(1)
- Search: O(n)
- Insertion: O(n) - due to shifting elements
- Deletion: O(n) - due to shifting elements
"""

class ArrayOperations:
    def __init__(self, size=10):
        """Initialize array with given size"""
        self.data = [None] * size
        self.size = 0
        self.capacity = size
    
    def insert(self, index, value):
        """Insert element at given index"""
        if self.size >= self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise Exception("Index out of bounds")
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        
        self.data[index] = value
        self.size += 1
    
    def delete(self, index):
        """Delete element at given index"""
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]
        
        self.size -= 1
        self.data[self.size] = None
    
    def search(self, value):
        """Search for a value and return its index"""
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def get(self, index):
        """Get element at given index"""
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        return self.data[index]
    
    def display(self):
        """Display the array elements"""
        return [self.data[i] for i in range(self.size)]

# Example usage
if __name__ == "__main__":
    arr = ArrayOperations()
    
    # Insert elements
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    print("Array after insertions:", arr.display())
    
    # Search for element
    index = arr.search(20)
    print(f"Element 20 found at index: {index}")
    
    # Delete element
    arr.delete(1)
    print("Array after deletion:", arr.display())
    
    # Access element
    print(f"Element at index 0: {arr.get(0)}")