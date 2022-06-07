from .code_367 import *
from .code_367 import is_tree_balanced

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(8) 
root1 = Node(1) 
root1.left = Node(2) 
root1.right = Node(3) 
root1.left.left = Node(4) 
root1.left.right = Node(5) 
root1.right.left = Node(6) 
root1.left.left.left = Node(7)
root2 = Node(1) 
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5)
root2.left.left.left = Node(7)
def test():
    assert is_tree_balanced(root1) == True