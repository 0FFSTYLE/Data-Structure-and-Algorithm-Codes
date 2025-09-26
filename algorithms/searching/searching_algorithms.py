"""
Common Searching Algorithms Implementation

This module contains implementations of various searching algorithms with
their time and space complexity analysis.
"""

def linear_search(arr, target):
    """
    Linear Search - Sequential search through all elements
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    Works on: Sorted and unsorted arrays
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Binary Search - Divide and conquer search (requires sorted array)
    
    Time Complexity: O(log n)
    Space Complexity: O(1) iterative, O(log n) recursive
    Works on: Sorted arrays only
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Binary Search - Recursive implementation
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def jump_search(arr, target):
    """
    Jump Search - Block-based search algorithm
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    Works on: Sorted arrays only
    """
    import math
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Find the block where element may be present
    while arr[min(step, n) - 1] < target and step < n:
        prev = step
        step += int(math.sqrt(n))
    
    # Linear search in the identified block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1

def interpolation_search(arr, target):
    """
    Interpolation Search - Improved binary search for uniformly distributed data
    
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    Works on: Sorted arrays with uniformly distributed values
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        # If array has only one element
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Calculate probe position
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1

def exponential_search(arr, target):
    """
    Exponential Search - Find range then apply binary search
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Works on: Sorted arrays only
    """
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find range for binary search
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Apply binary search on the found range
    left = i // 2
    right = min(i, len(arr) - 1)
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def ternary_search(arr, target):
    """
    Ternary Search - Divide array into three parts
    
    Time Complexity: O(log₃ n)
    Space Complexity: O(1)
    Works on: Sorted arrays only
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

def fibonacci_search(arr, target):
    """
    Fibonacci Search - Uses Fibonacci numbers to divide array
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    Works on: Sorted arrays only
    """
    n = len(arr)
    
    # Initialize fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number
    
    # Find smallest Fibonacci number >= n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1
    
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1

# Testing and comparison function
def compare_searching_algorithms(arr, target):
    """Compare all searching algorithms with the same input"""
    import time
    
    # Ensure array is sorted for algorithms that require it
    sorted_arr = sorted(arr)
    
    algorithms = [
        ("Linear Search", linear_search, arr),
        ("Binary Search", binary_search, sorted_arr),
        ("Binary Search (Recursive)", binary_search_recursive, sorted_arr),
        ("Jump Search", jump_search, sorted_arr),
        ("Interpolation Search", interpolation_search, sorted_arr),
        ("Exponential Search", exponential_search, sorted_arr),
        ("Ternary Search", ternary_search, sorted_arr),
        ("Fibonacci Search", fibonacci_search, sorted_arr)
    ]
    
    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Target: {target}")
    print(f"Array size: {len(arr)}")
    print("-" * 60)
    
    for name, func, test_arr in algorithms:
        start_time = time.time()
        result = func(test_arr, target)
        end_time = time.time()
        
        status = "Found" if result != -1 else "Not Found"
        print(f"{name:25}: Index {result:2d} ({status}) - Time: {(end_time - start_time) * 1000000:.2f} μs")

# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90, 5, 77, 30], 22),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7),
        ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 15),  # Not found
        (list(range(1, 101)), 50),  # Large sorted array
    ]
    
    for i, (arr, target) in enumerate(test_cases, 1):
        print(f"=== Test Case {i} ===")
        compare_searching_algorithms(arr, target)
        print("=" * 70)
        print()