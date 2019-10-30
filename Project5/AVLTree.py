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
        # if tree is empty
        if node is None:
            self.root = Node(value, parent=None)
            self.size += 1
            return
        # if value is not in tree
        elif value == node.value: # if value in tree do nothing
            return
        if value > node.value and node.right is None: # base
            node.right = Node(value, parent=node)
            self.size += 1
            AVLTreeUpdateHeight(node)
            return
        elif value < node.value and node.left is None: # base
            node.left = Node(value, parent=node)
            self.size += 1
            AVLTreeUpdateHeight(node)
            # self.rebalance(self.root)
            return

        if value > node.value:
            self.insert(node.right, value)
            AVLTreeUpdateHeight(node)
            self.rebalance(node)

        elif value < node.value:
            self.insert(node.left, value)
            AVLTreeUpdateHeight(node)
            self.rebalance(node)

    def remove(self, node, value):
        """

        :param node:
        :param value:
        :return:
        """
        if node is None:
            return

        # Parent needed for rebalancing
        parent = node.parent
        if node.value == value:
            self.size -= 1
            # Case 2: Root node (with 1 or 0 children)
            if node == self.root:
                # root has two nodes
                if node.right is not None and node.left is not None:
                    new_node = self.max(node.left)
                    self.root = new_node
                    if new_node != node.left:
                        new_node.left = node.left
                        node.left.parent = new_node
                        new_node.parent.right = None
                        AVLTreeUpdateHeight(node.left)

                    AVLTreeSetChild(new_node, 'right', node.right)
                # root only has left node
                elif node.right is None:
                    self.root = node.left
                else:
                    self.root = node.right
                if self.root:
                    self.root.parent = None
                return self.root
             # Case 1: Internal node with 2 children
            elif (node.left is not None and node.right is not None):
                new_node = self.max(node.left)
                parent_side = parentSide(node)
                if parent_side == 'right':
                    parent.right = new_node
                    new_node.parent = parent
                    node.right.parent = new_node
                    new_node.right = node.right
                    if new_node != node.right:
                        new_node.right = node.right
                    AVLTreeUpdateHeight(new_node)
                elif parent_side == 'left':
                    parent.left = new_node
                    new_node.parent = parent
                    node.right.parent = new_node
                    new_node.right = node.right
                    if new_node != node.left:
                        new_node.left = node.left
                        node.left.parent = new_node
                    AVLTreeUpdateHeight(new_node)
                return self.root

             # Case 3: Internal with left child only
            elif node.left is not None:
                AVLTreeReplaceChild(parent, node, node.left)

             # Case 4: Internal with right child only OR leaf
            else:
                AVLTreeReplaceChild(parent, node, node.right)

        # recursion
        if value > node.value:
            if node.right is None:
                return
            self.remove(node.right, value)
            AVLTreeUpdateHeight(node)
            self.rebalance(node)

        elif value < node.value:
            if node.left is None:
                return
            self.remove(node.left, value)
            AVLTreeUpdateHeight(node)
            self.rebalance(node)

        return self.root

    def search(self, node, value):
        """

        :param value:
        :param node:
        :return:
        """
        if node is None:
            return None

        # base cases
        if node.value == value:
            return node
        elif (node.left is None and node.right is None):
            return node

        # recursion
        if value > node.value:
            return self.search(node.right, value)

        elif value < node.value:
            return self.search(node.left, value)


    def inorder(self, node):
        """

        :param node:
        :return:
        """
        # minNode = self.min(node)
        if node is None:
            return
        yield from self.inorder(node.left)
        yield node
        yield from self.inorder(node.right)


    def preorder(self, node):
        """

        :param node:
        :return:
        """
        if node is None:
            return
        yield node
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

    def postorder(self, node):
        """

        :param node:
        :return:
        """
        if node is None:
            return
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node

    def breadth_first(self, node):
        """

        :param node:
        :return:
        """
        if self.root is not None:
            node_list = []  # known positions not yet yielded
            node_list.append(self.root)  # starting with the root
            while node_list:
                p = node_list.pop(0)  # remove from front of the queue
                yield p  # report this position
                if p.left is not None:
                    node_list.append(p.left)
                if p.right is not None:
                    node_list.append(p.right)

    def depth(self, value):
        """

        :param value:
        :return:
        """
        # if self.size == 0:
        #     return 0
        # else:
        #     curNode = self.search(self.root, value)
        # return self.root.height - curNode.height




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
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.min(node.left)

    def max(self, node):
        """

        :param node:
        :return:
        """
        if node is None:
            return None
        elif node.right is None:
            return node
        else:
            return self.max(node.right)

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


    def left_rotate(self, root):
        """
        Balances an AVL tree and does a left rotation
        :param root: [Node] root of the AVL tree
        :return: the root of the new subtree
        """
        # parent_side = None
        if root is None:
            return None
        rightLeftChild = root.right.left
        parent_side = parentSide(root)
        if parent_side is not None:
            if root.parent.left == root:
                AVLTreeSetChild(root.parent, "left", root.right)
            elif root.parent.right == root:
                AVLTreeSetChild(root.parent, "right", root.right)
        else:
            self.root = root.right
            self.root.parent = None
        # rotate
        AVLTreeSetChild(root.right, "left", root)
        AVLTreeSetChild(root, "right", rightLeftChild)
        AVLTreeUpdateHeight(root.parent)
        #
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
        # determine which side the parent is on
        parent_side = parentSide(root)
        if parent_side is not None:
            if root.parent.left == root:
                AVLTreeSetChild(root.parent, "left", root.left)
            elif root.parent.right == root:
                AVLTreeSetChild(root.parent, "right", root.left)
        else:
            self.root = root.left
            self.root.parent = None
        # rotate the new root to position
        AVLTreeSetChild(root.left, "right", root)
        AVLTreeSetChild(root, "left", leftRightChild)
        AVLTreeUpdateHeight(root.parent)

        AVLTreeUpdateHeight(self.root)
        return self.root  # return new root

    def rebalance(self, node):
        """

        :param node:
        :return:
        """
        AVLTreeUpdateHeight(node)
        if (self.get_balance(node) == -2):
            if self.get_balance(node.right) == 1:
                # Double rotation case.
                self.right_rotate(node.right)
            self.left_rotate(node)
        elif self.get_balance(node) == 2:
            if self.get_balance(node.left) == -1:
                # Double rotation case.
                self.left_rotate(node.left)
            self.right_rotate(node)
        return self.root

def inorder(node):
        """

        :param node:
        :return:
        """
        if node is None:
            return
        yield from inorder(node.left)
        yield node
        yield from inorder(node.right)

def add_under(root, total):
    if root is None:
        return 0
    return root.value + add_under(root.left, total) + add_under(root.right, total)

def node_max(node):
    if node is None:
        return None
    elif node.right is None:
        return node
    else:
        return node_max(node.right)

def BST_correction(node):
    # if root node
    if node is None:
        return
    tempLeft = node.left
    node.left = node.right
    node.right = tempLeft

    BST_correction(node.right)
    BST_correction(node.left)







def sum_update(root, total):
    """

    :param root:
    :param total:
    :return:
    """
    if root is None:
        return None
    inorder_list = []
    gen1 = inorder(root)
    iterator = next(gen1, None)
    # get an inorder list
    while iterator:
        inorder_list.append(iterator.value)
        iterator = next(gen1, None)
    sum = add_under(root, total)
    count = 0
    gen1 = inorder(root)
    iterator = next(gen1, None)
    maxNode = node_max(root)
    while sum != maxNode.value:
        iterator.value = sum
        sum -= inorder_list[count]
        count+=1
        iterator = next(gen1, None)


    BST_correction(root)

    return root



    # total = total + root.value

        # return root
    # if root is None:
    #     return
    # avl = AVLTree()
    # avl.root = root
    # node_gen1 = avl.inorder(avl.root)
    # node_gen2 = avl.inorder(avl.root)
    # size_gen = avl.inorder(avl.root)
    # size_iterator = next(size_gen, None)
    # while size_iterator:
    #     size_iterator = next(size_gen, None)
    #     avl.size += 1
    # count = 0
    # if total == 0:
    #     updateNode = next(node_gen1, None)
    #     curNode = updateNode.value
    #     toAddNode = next(node_gen2, None)
    #
    # else:
    #     while (total + 1) != count:
    #         updateNode = next(node_gen1, None)
    #         curNode = updateNode.value
    #         count += 1
    #         toAddNode = next(node_gen2, None)
    # avl.remove(avl.root, curNode)
    # while toAddNode:
    #     if toAddNode.value > curNode:
    #         updateNode.value += toAddNode.value
    #     toAddNode = next(node_gen2, None)
    # avl.insert(avl.root, updateNode.value)
    # total += 1
    # if total == avl.size:
    #     # new_avl = AVLTree()
    #     # new_avl.root = root
    #     return avl.root
    # sum_update(root, total)


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

def AVLTreeReplaceChild(parent, currentChild, newChild):
    if parent.left == currentChild:
        return AVLTreeSetChild(parent, "left", newChild)
    elif parent.right == currentChild:
        return AVLTreeSetChild(parent, "right", newChild)
    return False
