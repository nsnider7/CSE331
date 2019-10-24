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
        # if value already in the tree
        # if value is not in tree
        if value > node.value:
            node.right = Node(value, parent=node)
        elif value < node.value:
            node.left = Node(value)

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
        return node.height

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
        return self.size

    def get_balance(self, node):
        """

        :param node:
        :return:
        """
        leftHeight = -1
        if node.left is not None:
            leftHeight = node.left.height
        rightHeight = -1
        if node.right is not None:
            rightHeight = node.right.height
        return leftHeight - rightHeight

    def set_parent(self, parent_side, temp_parent):
        if parent_side is None:
            self.parent = None
        elif parent_side == 'left':
            self.root.parent = temp_parent
            self.root.parent.left = self.root
        elif parent_side == 'right':
            self.root.parent = temp_parent
            self.root.parent.right = self.root

    def left_rotate(self, root):
        """
        Balances an AVL tree and does a left rotation
        :param root: [Node] root of the AVL tree
        :return: the root of the new subtree
        """
        if root is None:
            return None
        rightLeftChild = root.right.left
        # case 1 right-right means rotate left-left
        if root.right.right is not None:  # node is root
            parent_side = parentSide(root)
            # create a temp parent to assign new root to
            temp_parent = root.parent
            # rotate the new root to position
            self.root = root.right
            # call set_parent to set the parent of the new node
            self.set_parent(parent_side, temp_parent)
            # rotate
            AVLTreeSetChild(root.right, "left", root)
            AVLTreeSetChild(root, "right", rightLeftChild)

        # case 2 right-left means left-right rotation
        elif root.right.right is None and root.right.left is not None:  # node is root
            parent_side = parentSide(root)
            # create a temp parent to assign new root to
            temp_parent = root.parent
            # rotate the new root to position
            self.root = root.right.left
            # call set_parent to set the parent of the new node
            self.set_parent(parent_side, temp_parent)
            # rotate
            AVLTreeSetChild(root.right.left, "left", root)
            AVLTreeSetChild(root.right.left, "right", root.right)
        AVLTreeUpdateHeight(self.root)
        return self.root

    def right_rotate(self, root):
        """

        :param root:
        :return:
        """
        if root is None:
            return None
        leftRightChild = root.left.right
        # case 1 left-left needs to be right right rotated
        if root.left.left is not None:
            # determine which side the parent is on
            parent_side = parentSide(root)
            # create a temp parent to assign new root to
            temp_parent = root.parent
            # rotate the new root to position
            self.root = root.left
            self.set_parent(parent_side, temp_parent)
            AVLTreeSetChild(root.left, "right", root)
            AVLTreeSetChild(root, "left", leftRightChild)

        # case 2-if tree is a left-right then do a right left rotation
        elif root.left.left is None and root.left.right is not None:  # if node is root
            parent_side = None
            # determine which side the parent is on
            parent_side = parentSide(root)
            # create a temp parent to assign new root to
            temp_parent = root.parent
            # rotate the new root to position
            self.root = root.left.right
            self.set_parent(parent_side, temp_parent)
            # set new roots values in rotation
            AVLTreeSetChild(root.left.right, "right", root)
            AVLTreeSetChild(root.left.right, "left", root.left)
        AVLTreeUpdateHeight(self.root)
        return self.root  # return new root

    def rebalance(self, node):
        """

        :param node:
        :return:
        """
        AVLTreeUpdateHeight(node)
        if (self.AVLTreeGetBalance(node) == -2):
            if self.AVLTreeGetBalance(node.right) == 1:
                # Double rotation case.
                self.AVLTreeRotateRight(self, node.right)
            return self.AVLTreeRotateLeft(self, node)
        elif self.AVLTreeGetBalance(node) == 2:
            if self.AVLTreeGetBalance(node.left) == -1:
                # Double rotation case.
                self.AVLTreeRotateLeft(self, node.left)
            return self.AVLTreeRotateRight(self, node)
        return node


def sum_update(root, total):
    """

    :param root:
    :param total:
    :return:
    """
    pass


def AVLTreeSetChild(parent, whichChild, child):
    if whichChild != "left" and whichChild != "right":
        return False

    if whichChild == "left":
        parent.left = child
    else:
        parent.right = child
    if child is not None:
        child.parent = parent

    AVLTreeUpdateHeight(parent)
    return True

# determines which side the parent is on the
def parentSide(root):
    '''
    determines which side the parent is on the current node
    :param root: [Node] to check what side parent is one
    :return: [str] returns which side or None is no parent
    '''
    if root.parent is not None:
        if root.parent.left == root:
            return 'left'
        elif root.parent.right == root:
            return 'right'
    else:
        return None

def AVLTreeUpdateHeight(node):
    leftHeight = -1
    if node.left is not None:
        leftHeight = node.left.height
    rightHeight = -1
    if node.right is not None:
        rightHeight = node.right.height
    node.height = max(leftHeight, rightHeight) + 1
