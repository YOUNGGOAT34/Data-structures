import time

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, root, key, value):
        if root is None:
            return TreeNode(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        return root
    

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, root.value)
            self.inorder_traversal(root.right)


    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)
def read_upc_csv(file):
    upc_data = {}
    with open(file, 'r') as f:
        for line in f:
            parts = line.strip().split(',', 1)  # Split into 2 parts only
            if len(parts) == 2:
                key, value = parts
                upc_data[int(key)] = value
            else:
                # Handle cases where the line doesn't contain exactly 2 parts
                print(f"Ignoring invalid line: {line}")
    return upc_data




if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insertion
    bst.insert(5, "Apple")
    bst.insert(3, "Banana")
    bst.insert(7, "Orange")
    bst.insert(6, "Mango")
    bst.insert(9, "Grapes")

    # In-order Traversal
    print("In-order Traversal:")
    bst.inorder_traversal(bst.root)

    # Search
    key_to_search = 7
    result = bst.search(key_to_search)
    if result:
        print(f"Key {key_to_search} found! Value: {result.value}")
    else:
        print(f"Key {key_to_search} not found.")

    upc_data = read_upc_csv("UPC.csv")
   

    

    # Step 1: Read UPC data from "UPC.csv"
    upc_data = read_upc_csv("UPC-random.csv")
     # Step 2: Build Binary Search Tree
    bst = BinarySearchTree()
    for key, value in upc_data.items():
        bst.insert(key, value)


    # Test the program for the given search keys
    input_keys = []
    with open("input.dat", 'r') as f:
        for line in f:
            # Split the line by comma and take the first part as the UPC key
            key = int(line.strip().split(',')[0])
            input_keys.append(key) 

    print("Description for search keys:")
    start_time = time.time()
    for key in input_keys:
        description = bst.search(key)
        if description:
            print(f"UPC: {key}, Description: {description.value}")
        else:
            print(f"UPC: {key}, Description not found.")

    end_time = time.time()

    total_time = end_time - start_time
    print(f"Total time taken to complete the search: {total_time} seconds")

    
