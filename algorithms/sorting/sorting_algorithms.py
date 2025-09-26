"""
Common Sorting Algorithms Implementation

This module contains implementations of various sorting algorithms with
their time and space complexity analysis.
"""

def bubble_sort(arr):
    """
    Bubble Sort - Simple comparison-based sorting algorithm
    
    Time Complexity: O(n²) in worst and average case, O(n) in best case
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original array
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

def selection_sort(arr):
    """
    Selection Sort - Finds minimum element and places it at the beginning
    
    Time Complexity: O(n²) in all cases
    Space Complexity: O(1)
    Stable: No
    In-place: Yes
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def insertion_sort(arr):
    """
    Insertion Sort - Builds sorted array one element at a time
    
    Time Complexity: O(n²) in worst and average case, O(n) in best case
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

def merge_sort(arr):
    """
    Merge Sort - Divide and conquer algorithm
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def quick_sort(arr):
    """
    Quick Sort - Divide and conquer with pivot partitioning
    
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) average, O(n) worst case
    Stable: No
    In-place: Yes (this implementation creates new arrays for simplicity)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    """
    Heap Sort - Uses binary heap data structure
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(1)
    Stable: No
    In-place: Yes
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)  # Call heapify on reduced heap
    
    return arr

def heapify(arr, n, i):
    """Helper function for heap sort - maintains max heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Testing and comparison function
def compare_sorting_algorithms(arr):
    """Compare all sorting algorithms with the same input"""
    import time
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    print(f"Original array: {arr}")
    print(f"Array size: {len(arr)}")
    print("-" * 50)
    
    for name, func in algorithms:
        start_time = time.time()
        sorted_arr = func(arr)
        end_time = time.time()
        
        print(f"{name:15}: {sorted_arr}")
        print(f"Time taken: {(end_time - start_time) * 1000:.4f} ms")
        print()

# Example usage
if __name__ == "__main__":
    # Test with different types of arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],           # Random array
        [5, 2, 4, 6, 1, 3],                     # Small array
        [1, 2, 3, 4, 5],                        # Already sorted
        [5, 4, 3, 2, 1],                        # Reverse sorted
        [3, 3, 3, 3, 3]                         # All same elements
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"=== Test Case {i} ===")
        compare_sorting_algorithms(arr)
        print("=" * 60)
        print()