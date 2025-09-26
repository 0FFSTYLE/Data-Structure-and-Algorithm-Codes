# Data Structures and Algorithms Tutorial

A comprehensive collection of data structure and algorithm implementations with detailed explanations, time/space complexity analysis, and practical examples.

## 📚 Table of Contents

- [Overview](#overview)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [Getting Started](#getting-started)
- [Examples](#examples)
- [Contributing](#contributing)

## 🎯 Overview

This repository serves as a complete tutorial and reference for fundamental data structures and algorithms. Each implementation includes:

- **Detailed documentation** with complexity analysis
- **Working code examples** in Python
- **Practical applications** and use cases
- **Step-by-step explanations** of operations

## 📊 Data Structures

### Linear Data Structures

#### Arrays
- **File**: [`data_structures/arrays/array_operations.py`](data_structures/arrays/array_operations.py)
- **Operations**: Insert, Delete, Search, Access
- **Time Complexity**: Access O(1), Search O(n), Insert/Delete O(n)
- **Use Cases**: When you need fast random access by index

#### Linked Lists
- **File**: [`data_structures/linked_lists/singly_linked_list.py`](data_structures/linked_lists/singly_linked_list.py)
- **Operations**: Insert at head/tail/position, Delete, Search
- **Time Complexity**: Access O(n), Insert/Delete O(1) at head
- **Use Cases**: Dynamic size, frequent insertions/deletions at beginning

#### Stacks
- **File**: [`data_structures/stacks/stack.py`](data_structures/stacks/stack.py)
- **Operations**: Push, Pop, Peek, Search
- **Time Complexity**: All operations O(1) except search O(n)
- **Use Cases**: Function calls, expression evaluation, undo operations
- **Example Application**: Balanced parentheses checker included

#### Queues
- **File**: [`data_structures/queues/queue.py`](data_structures/queues/queue.py)
- **Types**: Regular Queue, Circular Queue
- **Operations**: Enqueue, Dequeue, Front, Rear
- **Time Complexity**: All operations O(1)
- **Use Cases**: BFS, process scheduling, handling requests

### Non-Linear Data Structures

#### Binary Search Trees
- **File**: [`data_structures/trees/binary_search_tree.py`](data_structures/trees/binary_search_tree.py)
- **Operations**: Insert, Delete, Search, Traversals
- **Time Complexity**: Average O(log n), Worst O(n)
- **Traversals**: Inorder, Preorder, Postorder, Level-order
- **Use Cases**: Sorted data, range queries, hierarchical data

## 🚀 Algorithms

### Sorting Algorithms

**File**: [`algorithms/sorting/sorting_algorithms.py`](algorithms/sorting/sorting_algorithms.py)

| Algorithm | Time Complexity | Space | Stable | Description |
|-----------|----------------|-------|---------|-------------|
| **Bubble Sort** | O(n²) | O(1) | Yes | Simple comparison-based sort |
| **Selection Sort** | O(n²) | O(1) | No | Finds minimum and places at beginning |
| **Insertion Sort** | O(n²) | O(1) | Yes | Builds sorted array incrementally |
| **Merge Sort** | O(n log n) | O(n) | Yes | Divide and conquer approach |
| **Quick Sort** | O(n log n) avg | O(log n) | No | Pivot-based partitioning |
| **Heap Sort** | O(n log n) | O(1) | No | Uses binary heap structure |

### Searching Algorithms

**File**: [`algorithms/searching/searching_algorithms.py`](algorithms/searching/searching_algorithms.py)

| Algorithm | Time Complexity | Space | Requirements | Description |
|-----------|----------------|-------|--------------|-------------|
| **Linear Search** | O(n) | O(1) | None | Sequential search |
| **Binary Search** | O(log n) | O(1) | Sorted array | Divide and conquer |
| **Jump Search** | O(√n) | O(1) | Sorted array | Block-based search |
| **Interpolation Search** | O(log log n) | O(1) | Uniformly distributed | Improved binary search |
| **Exponential Search** | O(log n) | O(1) | Sorted array | Find range then binary search |
| **Ternary Search** | O(log₃ n) | O(1) | Sorted array | Divide into three parts |
| **Fibonacci Search** | O(log n) | O(1) | Sorted array | Uses Fibonacci numbers |

## 🏃‍♂️ Getting Started

### Prerequisites
- Python 3.6 or higher

### Running the Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/0FFSTYLE/Data-Structure-and-Algorithm-Codes.git
   cd Data-Structure-and-Algorithm-Codes
   ```

2. **Run individual data structures**:
   ```bash
   python data_structures/arrays/array_operations.py
   python data_structures/linked_lists/singly_linked_list.py
   python data_structures/stacks/stack.py
   python data_structures/queues/queue.py
   python data_structures/trees/binary_search_tree.py
   ```

3. **Run sorting algorithms**:
   ```bash
   python algorithms/sorting/sorting_algorithms.py
   ```

4. **Run searching algorithms**:
   ```bash
   python algorithms/searching/searching_algorithms.py
   ```

5. **Run comprehensive examples**:
   ```bash
   python examples/example_usage.py
   ```

## 💡 Examples

The [`examples/example_usage.py`](examples/example_usage.py) file demonstrates:

- **Practical usage** of all data structures
- **Problem-solving** with real-world examples
- **Performance comparisons** between algorithms
- **Best practices** for choosing appropriate data structures

Example output includes:
- Data structure operations and results
- Balanced parentheses validation
- Duplicate finding algorithms
- Sorting and searching performance metrics

## 📈 Complexity Quick Reference

### Data Structures Operations

| Data Structure | Access | Search | Insertion | Deletion | Space |
|---------------|--------|---------|-----------|-----------|-------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **BST** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

*\*At head position*

### Algorithm Performance

| Problem | Best Algorithm | Time Complexity | When to Use |
|---------|---------------|----------------|-------------|
| **Sorting small arrays** | Insertion Sort | O(n²) | n < 50 |
| **Sorting large arrays** | Quick/Merge Sort | O(n log n) | General purpose |
| **Searching unsorted** | Linear Search | O(n) | No other option |
| **Searching sorted** | Binary Search | O(log n) | Always prefer this |
| **Finding duplicates** | Hash Set | O(n) | When extra space available |

## 🔧 Key Features

- **Educational Focus**: Each implementation prioritizes clarity and understanding
- **Comprehensive Coverage**: From basic arrays to complex tree structures
- **Practical Examples**: Real-world applications and problem-solving
- **Performance Analysis**: Detailed time and space complexity discussions
- **Production Ready**: Clean, well-documented, and tested code

## 🎓 Learning Path

1. **Start with Linear Structures**: Arrays → Linked Lists → Stacks → Queues
2. **Move to Non-Linear**: Binary Search Trees → Hash Tables
3. **Learn Basic Algorithms**: Linear Search → Binary Search → Simple Sorting
4. **Advanced Algorithms**: Efficient Sorting → Advanced Searching
5. **Practice**: Use the examples and create your own implementations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Areas for contribution:
- Additional data structures (Hash Tables, Heaps, Graphs)
- More algorithms (Dynamic Programming, Graph algorithms)
- Language implementations (Java, C++, JavaScript)
- Performance optimizations
- Additional examples and use cases

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🌟 Acknowledgments

- Built for educational purposes
- Suitable for computer science students, coding interviews, and professional development
- Contributions and feedback welcome from the community

---

**Happy Learning! 🚀**

*Remember: Understanding the concept is more important than memorizing the code. Focus on when and why to use each data structure and algorithm.*
