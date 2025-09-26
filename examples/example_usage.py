"""
Data Structures and Algorithms - Example Usage

This file demonstrates practical usage of various data structures and algorithms
implemented in this repository.
"""

import sys
import os

# Add the parent directory to the path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.arrays.array_operations import ArrayOperations
from data_structures.linked_lists.singly_linked_list import SinglyLinkedList
from data_structures.stacks.stack import Stack, balanced_parentheses
from data_structures.queues.queue import Queue, CircularQueue
from data_structures.trees.binary_search_tree import BinarySearchTree
from algorithms.sorting.sorting_algorithms import quick_sort, merge_sort
from algorithms.searching.searching_algorithms import binary_search, linear_search

def demonstrate_data_structures():
    """Demonstrate various data structures"""
    print("=" * 60)
    print("DATA STRUCTURES DEMONSTRATION")
    print("=" * 60)
    
    # Array Example
    print("\n1. ARRAY OPERATIONS")
    print("-" * 30)
    arr = ArrayOperations(10)
    for i, val in enumerate([5, 10, 15, 20, 25]):
        arr.insert(i, val)
    print(f"Array: {arr.display()}")
    print(f"Search 15: Index {arr.search(15)}")
    arr.delete(2)  # Delete 15
    print(f"After deleting index 2: {arr.display()}")
    
    # Linked List Example
    print("\n2. LINKED LIST OPERATIONS")
    print("-" * 30)
    ll = SinglyLinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.insert_at_tail(val)
    print(f"Linked List: {ll.display()}")
    ll.insert_at_position(2, 99)
    print(f"After inserting 99 at position 2: {ll.display()}")
    ll.delete_by_value(99)
    print(f"After deleting 99: {ll.display()}")
    
    # Stack Example
    print("\n3. STACK OPERATIONS")
    print("-" * 30)
    stack = Stack()
    for val in [10, 20, 30, 40]:
        stack.push(val)
    print(f"Stack: {stack.display()}")
    print(f"Top element: {stack.peek()}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after pop: {stack.display()}")
    
    # Queue Example  
    print("\n4. QUEUE OPERATIONS")
    print("-" * 30)
    queue = Queue()
    for val in ['A', 'B', 'C', 'D']:
        queue.enqueue(val)
    print(f"Queue: {queue.display()}")
    print(f"Front: {queue.front()}, Rear: {queue.rear()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue.display()}")
    
    # Binary Search Tree Example
    print("\n5. BINARY SEARCH TREE")
    print("-" * 30)
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    print(f"BST Inorder (sorted): {bst.inorder_traversal()}")
    print(f"BST Level order: {bst.level_order_traversal()}")
    print(f"Tree height: {bst.find_height()}")
    print(f"Search 40: {bst.search(40)}")

def solve_practical_problems():
    """Solve practical problems using data structures and algorithms"""
    print("\n" + "=" * 60)
    print("PRACTICAL PROBLEM SOLVING")
    print("=" * 60)
    
    # Problem 1: Balanced Parentheses
    print("\n1. BALANCED PARENTHESES CHECKER")
    print("-" * 40)
    expressions = ["((()))", "()[]{}", "([)]", "((("]
    for expr in expressions:
        result = balanced_parentheses(expr)
        print(f"'{expr}' -> {'Balanced' if result else 'Not Balanced'}")
    
    # Problem 2: Find duplicates using data structures
    print("\n2. FIND DUPLICATES IN ARRAY")
    print("-" * 40)
    def find_duplicates_with_set(arr):
        seen = set()
        duplicates = set()
        for item in arr:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        return list(duplicates)
    
    test_array = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
    print(f"Array: {test_array}")
    print(f"Duplicates: {find_duplicates_with_set(test_array)}")
    
    # Problem 3: Sorting comparison
    print("\n3. SORTING PERFORMANCE COMPARISON")
    print("-" * 40)
    import time
    import random
    
    # Generate random data
    data = [random.randint(1, 1000) for _ in range(100)]
    print(f"Sorting {len(data)} random numbers...")
    
    algorithms = [
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort)
    ]
    
    for name, func in algorithms:
        start_time = time.time()
        sorted_data = func(data.copy())
        end_time = time.time()
        print(f"{name}: {(end_time - start_time) * 1000:.2f} ms")
    
    # Problem 4: Search comparison
    print("\n4. SEARCH PERFORMANCE COMPARISON")
    print("-" * 40)
    sorted_data = sorted(data)
    target = sorted_data[len(sorted_data) // 2]  # Middle element
    
    search_algorithms = [
        ("Linear Search", linear_search),
        ("Binary Search", binary_search)
    ]
    
    print(f"Searching for {target} in sorted array of {len(sorted_data)} elements:")
    for name, func in search_algorithms:
        start_time = time.time()
        if name == "Linear Search":
            result = func(sorted_data, target)
        else:
            result = func(sorted_data, target)
        end_time = time.time()
        print(f"{name}: Found at index {result} in {(end_time - start_time) * 1000000:.2f} μs")

def demonstrate_algorithm_complexity():
    """Demonstrate time complexity differences"""
    print("\n" + "=" * 60)
    print("ALGORITHM COMPLEXITY DEMONSTRATION")
    print("=" * 60)
    
    import time
    import random
    
    sizes = [100, 500, 1000]
    
    print("\nSorting Algorithm Performance (Time in ms):")
    print("Size\tQuick Sort\tMerge Sort")
    print("-" * 40)
    
    for size in sizes:
        data = [random.randint(1, 1000) for _ in range(size)]
        
        # Quick Sort
        start = time.time()
        quick_sort(data.copy())
        quick_time = (time.time() - start) * 1000
        
        # Merge Sort  
        start = time.time()
        merge_sort(data.copy())
        merge_time = (time.time() - start) * 1000
        
        print(f"{size}\t{quick_time:.2f}\t\t{merge_time:.2f}")

if __name__ == "__main__":
    demonstrate_data_structures()
    solve_practical_problems()
    demonstrate_algorithm_complexity()
    
    print("\n" + "=" * 60)
    print("EXAMPLES COMPLETED SUCCESSFULLY!")
    print("=" * 60)