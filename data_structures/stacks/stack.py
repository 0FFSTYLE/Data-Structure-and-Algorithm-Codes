"""
Stack Implementation using List

A stack is a linear data structure that follows the LIFO (Last In, First Out) principle.
Elements are added and removed from the same end called the "top" of the stack.

Time Complexities:
- Push: O(1)
- Pop: O(1)
- Peek/Top: O(1)
- Search: O(n)

Space Complexity: O(n)

Common Applications:
- Function call management (call stack)
- Expression evaluation and syntax parsing
- Undo operations in editors
- Browser history
"""

class Stack:
    def __init__(self, capacity=None):
        """Initialize an empty stack with optional capacity limit"""
        self.items = []
        self.capacity = capacity
    
    def push(self, item):
        """Add an item to the top of the stack"""
        if self.capacity is not None and len(self.items) >= self.capacity:
            raise Exception("Stack overflow: Stack is full")
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise Exception("Stack underflow: Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def is_full(self):
        """Check if the stack is full (only relevant if capacity is set)"""
        if self.capacity is None:
            return False
        return len(self.items) >= self.capacity
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def search(self, item):
        """Search for an item and return its distance from the top (1-based)"""
        try:
            index = self.items[::-1].index(item)
            return index + 1  # 1-based distance from top
        except ValueError:
            return -1
    
    def display(self):
        """Display the stack contents (top to bottom)"""
        return list(reversed(self.items))

def balanced_parentheses(expression):
    """
    Example application: Check if parentheses are balanced
    Returns True if balanced, False otherwise
    """
    stack = Stack()
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()

# Example usage
if __name__ == "__main__":
    # Basic stack operations
    stack = Stack()
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.display())
    print("Stack size:", stack.size())
    
    # Peek at top
    print("Top element:", stack.peek())
    
    # Pop elements
    popped = stack.pop()
    print(f"Popped element: {popped}")
    print("Stack after pop:", stack.display())
    
    # Search for element
    distance = stack.search(10)
    print(f"Element 10 is at distance {distance} from top")
    
    # Test balanced parentheses
    test_expressions = [
        "((()))",      # True
        "()[]{()}",    # True
        "([)]",        # False
        "(((",         # False
        ""             # True (empty string)
    ]
    
    print("\nBalanced Parentheses Tests:")
    for expr in test_expressions:
        result = balanced_parentheses(expr)
        print(f"'{expr}' -> {result}")