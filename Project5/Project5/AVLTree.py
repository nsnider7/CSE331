import random as r

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.height == other.height

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result
            
    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """

        :param node:
        :param value:
        :return:
        """
        pass


    def remove(self, node, value):
        """

        :param node:
        :param value:
        :return:
        """
        pass


    def search(self, node, value):
        """

        :param value:
        :param node:
        :return:
        """
        pass


    def inorder(self, node):
        """

        :param node:
        :return:
        """
        pass


    def preorder(self, node):
        """

        :param node:
        :return:
        """
        pass


    def postorder(self, node):
        """

        :param node:
        :return:
        """
        pass


    def breadth_first(self, node):
        """

        :param node:
        :return:
        """
        pass

    def depth(self, value):
        """

        :param value:
        :return:
        """
        pass


    def height(self, node):
        """

        :param node:
        :return:
        """
        pass


    def min(self, node):
        """

        :param node:
        :return:
        """
        pass


    def max(self, node):
        """

        :param node:
        :return:
        """
        pass


    def get_size(self):
        """

        :return:
        """
        pass


    def get_balance(self, node):
        """

        :param node:
        :return:
        """
        pass


    def left_rotate(self, root):
        """

        :param root:
        :return:
        """
        pass


    def right_rotate(self, root):
        """

        :param root:
        :return:
        """
        pass


    def rebalance(self, node):
        """

        :param node:
        :return:
        """
        pass


def sum_update(root, total):
    """

    :param root:
    :param total:
    :return:
    """
    pass

