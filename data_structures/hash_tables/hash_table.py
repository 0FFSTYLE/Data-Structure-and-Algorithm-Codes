"""
Hash Table (Hash Map) Implementation

A hash table is a data structure that implements an associative array abstract data type,
a structure that can map keys to values using a hash function.

Time Complexities (Average Case):
- Search: O(1)
- Insertion: O(1)
- Deletion: O(1)

Time Complexities (Worst Case):
- Search: O(n) - when all keys hash to same bucket
- Insertion: O(n)
- Deletion: O(n)

Space Complexity: O(n)

Collision Handling: Separate Chaining (using linked lists)
"""

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        """Initialize hash table with given capacity"""
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def _hash(self, key):
        """Simple hash function using built-in hash() and modulo"""
        return hash(key) % self.capacity
    
    def _resize(self):
        """Resize hash table when load factor exceeds threshold"""
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [None] * self.capacity
        
        # Rehash all existing key-value pairs
        for head in old_buckets:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next
    
    def put(self, key, value):
        """Insert or update a key-value pair"""
        # Resize if load factor > 0.75
        if self.size >= self.capacity * 0.75:
            self._resize()
        
        index = self._hash(key)
        
        if self.buckets[index] is None:
            # No collision, create new node
            self.buckets[index] = HashNode(key, value)
            self.size += 1
        else:
            # Handle collision with chaining
            current = self.buckets[index]
            while True:
                if current.key == key:
                    # Update existing key
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            
            # Add new node at end of chain
            current.next = HashNode(key, value)
            self.size += 1
    
    def get(self, key):
        """Get value associated with key"""
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair"""
        index = self._hash(key)
        current = self.buckets[index]
        
        if current is None:
            raise KeyError(f"Key '{key}' not found")
        
        # If first node has the key
        if current.key == key:
            self.buckets[index] = current.next
            self.size -= 1
            return current.value
        
        # Search in the chain
        while current.next:
            if current.next.key == key:
                deleted_value = current.next.value
                current.next = current.next.next
                self.size -= 1
                return deleted_value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Check if key exists in hash table"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def keys(self):
        """Return list of all keys"""
        keys_list = []
        for head in self.buckets:
            current = head
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list
    
    def values(self):
        """Return list of all values"""
        values_list = []
        for head in self.buckets:
            current = head
            while current:
                values_list.append(current.value)
                current = current.next
        return values_list
    
    def items(self):
        """Return list of all key-value pairs"""
        items_list = []
        for head in self.buckets:
            current = head
            while current:
                items_list.append((current.key, current.value))
                current = current.next
        return items_list
    
    def get_size(self):
        """Return number of key-value pairs"""
        return self.size
    
    def is_empty(self):
        """Check if hash table is empty"""
        return self.size == 0
    
    def get_load_factor(self):
        """Return current load factor"""
        return self.size / self.capacity
    
    def display(self):
        """Display hash table structure for debugging"""
        print(f"Hash Table (Size: {self.size}, Capacity: {self.capacity}, Load Factor: {self.get_load_factor():.2f})")
        for i, head in enumerate(self.buckets):
            if head is not None:
                chain = []
                current = head
                while current:
                    chain.append(f"({current.key}: {current.value})")
                    current = current.next
                print(f"Bucket {i}: {' -> '.join(chain)}")

# Example usage and demonstration
if __name__ == "__main__":
    # Create hash table
    ht = HashTable(5)  # Small capacity to demonstrate resizing
    
    print("=== Hash Table Demonstration ===")
    
    # Insert key-value pairs
    pairs = [
        ("name", "Alice"),
        ("age", 25),
        ("city", "New York"),
        ("job", "Engineer"),
        ("hobby", "Reading"),
        ("color", "Blue"),
        ("food", "Pizza")
    ]
    
    print("\nInserting key-value pairs:")
    for key, value in pairs:
        ht.put(key, value)
        print(f"Inserted ({key}, {value})")
    
    print(f"\nHash table size: {ht.get_size()}")
    print(f"Load factor: {ht.get_load_factor():.2f}")
    
    # Display hash table structure
    print("\nHash table structure:")
    ht.display()
    
    # Get operations
    print("\nGet operations:")
    test_keys = ["name", "age", "invalid_key"]
    for key in test_keys:
        try:
            value = ht.get(key)
            print(f"get('{key}') = {value}")
        except KeyError as e:
            print(f"get('{key}') = {e}")
    
    # Contains operations
    print("\nContains operations:")
    for key in test_keys:
        exists = ht.contains(key)
        print(f"contains('{key}') = {exists}")
    
    # Update existing key
    print("\nUpdating existing key:")
    ht.put("age", 26)
    print(f"Updated age to: {ht.get('age')}")
    
    # Delete operations
    print("\nDelete operations:")
    delete_keys = ["hobby", "invalid_key"]
    for key in delete_keys:
        try:
            deleted_value = ht.delete(key)
            print(f"Deleted '{key}': {deleted_value}")
        except KeyError as e:
            print(f"Delete '{key}': {e}")
    
    # Display all keys, values, and items
    print(f"\nAll keys: {ht.keys()}")
    print(f"All values: {ht.values()}")
    print(f"All items: {ht.items()}")
    
    print(f"\nFinal size: {ht.get_size()}")
    print("Hash table demonstration completed!")