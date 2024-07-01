class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def get_balance(n):
    return height(n.left) - height(n.right) if n else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

    return y

def insert(node, key):
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if not root.left or not root.right:
            temp = root.left if root.left else root.right
            if not temp:
                temp = root
                root = None
            else:
                root = temp
        else:
            temp = min_value_node(root.right)
            root.key = temp.key
            root.right = delete_node(root.right, temp.key)

    if not root:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def search(root, key):
    while root and root.key != key:
        root = root.right if root.key < key else root.left
    return root

def pre_order(root):
    if root:
        print(root.key, end=' ')
        pre_order(root.left)
        pre_order(root.right)

if __name__ == "__main__":
    root = None
    root = insert(root, 10)
    root = insert(root, 20)
    root = insert(root, 30)
    root = insert(root, 40)
    root = insert(root, 50)
    root = insert(root, 25)

    print("Preorder traversal of the AVL tree:")
    pre_order(root)
    
    root = delete_node(root, 10)
    print("\nPreorder traversal after deleting 10:")
    pre_order(root)
    
    found_node = search(root, 30)
    if found_node:
        print("\nNode with key 30 found.")
    else:
        print("\nNode with key 30 not found.")





#output 

#Preorder traversal of the AVL tree:
#30 20 10 25 40 50 
#Preorder traversal after deleting 10:
#30 20 25 40 50