from stact import Queue
from stact import Stack
from Binary_print_trr import BinaryTreePrinter



class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            node = Queue()
            node.enqueue(self.root)

            while True:
                chaking_node = node.dequee()
                if chaking_node.left is None:
                    chaking_node.left = TreeNode(val)
                    return
                elif chaking_node.right is None:
                    chaking_node.right = TreeNode(val)
                    return
                else:
                    node.enqueue(chaking_node.left)
                    node.enqueue(chaking_node.right)
        
    def __str__(self):
        tree_pinter = BinaryTreePrinter()
        return tree_pinter.get_tree_string(self.root)

    
my_tree = BinaryTree()
for c in ['a','b','c','d','f']:
    my_tree.insert(c)
    print(my_tree)
