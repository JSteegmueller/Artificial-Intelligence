# Note: Make sure each function can be called by the same name and input arguments as defined in the task.

from collections import deque
from typing import Deque, List


class BinaryTree:
    """
    BinaryTree class
    """

    def __init__(self, value=None, left=None, right=None):
        """
        :param value: value of the given node
        :param left: left child/branch of the binary tree
        :param right: right child/branch of the binary tree
        """
        self.value = value
        self.left = left
        self.right = right


#  Define a binary tree drawn in Q3(a)
tree = BinaryTree(1,
                  BinaryTree(2,
                             BinaryTree(3,
                                        BinaryTree(4,
                                                   BinaryTree(5), BinaryTree(6)),
                                        BinaryTree(7, BinaryTree(8))), None),
                  BinaryTree(9,
                             BinaryTree(10,
                                        BinaryTree(11), BinaryTree(12)),
                             BinaryTree(13,
                                        BinaryTree(14,
                                                   BinaryTree(15),
                                                   BinaryTree(16)),
                                        BinaryTree(17,
                                                   None, BinaryTree(18)))))  # TODO: Q3(a)


def depth_first_search(tree: BinaryTree, val, search_order: List):
    """
    Function to do depth first search in a binary tree
    :param tree: a binary tree
    :param search_order: list that  stores the order (value) in which tree has been searched until now
    :param val: value to search in tree
    :return: True: if val is found, otherwise False
            traversal order. Hint: python lists are sent as reference so you do not need to return explicitly
    """
    current_tree = tree
    deque = Deque()
    while True:
        search_order.append(current_tree.value)
        if current_tree.value == val:
            return True
        if current_tree.right:
            deque.append(current_tree.right)
        if current_tree.left:
            deque.append(current_tree.left)
        if len(deque) < 1:
            return False
        current_tree = deque.pop()


print("*******************************Depth-first search*******************************")
order = []
val = 18
res = depth_first_search(tree, val, order)
if res:
    print(f"Found value {val}")
else:
    print("Not found!")
print("Tree search order was:\n", order)


def depth_limited_search(tree: BinaryTree, val, search_order: List, limit):
    """
    Function to do depth limited search in a binary tree
    :param tree: a binary tree
    :param search_order: list that  stores the order (value) in which tree has been searched until now
    :param val: value to search in tree
    :param limit: level of tree where search must be stopped
    :return: True: if val is found, otherwise False
             traversal order. Hint: python lists are sent as reference so you do not need to return explicitly
    """
    found = False
    if limit == 0: return
    search_order.append(tree.value)
    if tree.value == val:
        return True
    if tree.left:
        found = found or depth_limited_search(tree.left, val, search_order, limit - 1)
    if tree.right:
        found = found or depth_limited_search(tree.right, val, search_order, limit - 1)
    return found

print("*******************************Depth-limited search*******************************")
order = []
val = 13
res = depth_limited_search(tree, val, order, 3)
if res:
    print(f"Found value {val}")
else:
    print("Not found!")
print("Tree search order was:\n", order)


def breadth_first_search(tree: BinaryTree, val, search_order):
    """
    Function to do breadth first search in a binary tree
    :param tree: a binary tree
    :param search_order: list that  stores the order (value) in which tree has been searched until now
    :param val: value to search in tree
    :return: True: if val is found, otherwise False
             traversal order. Hint: python lists are sent as reference so you do not need to return explicitly
    """
    current_tree = tree
    deque = Deque()
    while True:
        search_order.append(current_tree.value)
        if current_tree.value == val:
            return True
        if current_tree.left:
            deque.append(current_tree.left)
        if current_tree.right:
            deque.append(current_tree.right)
        if len(deque) < 1:
            return False
        current_tree = deque.popleft()


print("*******************************Breadth-first search*******************************")
order = []
val = 18
res = breadth_first_search(tree, val, order)
if res:
    print(f"Found value {val}")
else:
    print("Not found!")
print("Tree search order was:\n", order)
