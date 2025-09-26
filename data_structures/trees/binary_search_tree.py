"""
Binary Search Tree (BST) Implementation

A binary search tree is a hierarchical data structure where each node has at most 
two children (left and right), and for every node:
- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than the node's value

Time Complexities (Average Case):
- Search: O(log n)
- Insertion: O(log n)
- Deletion: O(log n)

Time Complexities (Worst Case - skewed tree):
- Search: O(n)
- Insertion: O(n)
- Deletion: O(n)

Space Complexity: O(n)
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST"""
        self.root = self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion"""
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If value equals node.value, we don't insert (no duplicates)
        
        return node
    
    def search(self, value):
        """Search for a value in the BST"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method for recursive search"""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Delete a value from the BST"""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method for recursive deletion"""
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to be deleted found
            
            # Case 1: Node has no children (leaf node)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: Node has one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 3: Node has two children
            else:
                # Find the inorder successor (smallest value in right subtree)
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)
        
        return node
    
    def _find_min(self, node):
        """Find the node with minimum value in the subtree"""
        while node.left is not None:
            node = node.left
        return node
    
    def _find_max(self, node):
        """Find the node with maximum value in the subtree"""
        while node.right is not None:
            node = node.right
        return node
    
    # Tree Traversal Methods
    def inorder_traversal(self):
        """Inorder traversal: Left -> Root -> Right (gives sorted order)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Preorder traversal: Root -> Left -> Right"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Postorder traversal: Left -> Right -> Root"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def level_order_traversal(self):
        """Level order traversal (BFS): Visit nodes level by level"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def find_height(self):
        """Find the height of the tree"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def count_nodes(self):
        """Count total number of nodes in the tree"""
        return self._count_recursive(self.root)
    
    def _count_recursive(self, node):
        if node is None:
            return 0
        
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)
    
    def is_valid_bst(self):
        """Check if the tree is a valid BST"""
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for value in values:
        bst.insert(value)
    
    print("BST created with values:", values)
    print("Tree height:", bst.find_height())
    print("Total nodes:", bst.count_nodes())
    print("Is valid BST:", bst.is_valid_bst())
    
    # Traversals
    print("\nTraversals:")
    print("Inorder (sorted):", bst.inorder_traversal())
    print("Preorder:", bst.preorder_traversal())
    print("Postorder:", bst.postorder_traversal())
    print("Level order:", bst.level_order_traversal())
    
    # Search operations
    search_values = [25, 55, 80]
    print(f"\nSearch operations:")
    for val in search_values:
        found = bst.search(val)
        print(f"Search {val}: {'Found' if found else 'Not Found'}")
    
    # Delete operations
    print(f"\nBefore deletion:", bst.inorder_traversal())
    bst.delete(20)  # Delete leaf node
    print(f"After deleting 20:", bst.inorder_traversal())
    
    bst.delete(30)  # Delete node with two children
    print(f"After deleting 30:", bst.inorder_traversal())
    
    bst.delete(50)  # Delete root
    print(f"After deleting 50:", bst.inorder_traversal())