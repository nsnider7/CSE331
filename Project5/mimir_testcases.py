import unittest
from AVLTree import AVLTree, sum_update, Node, add_under


class TestProject1(unittest.TestCase):

    def test_left_and_right_rotate(self):
        # 1 normal right right rotation
        avl = AVLTree()
        avl.root = Node(3)
        avl.root.left = Node(2, parent=avl.root)
        avl.root.left.left = Node(1, parent=avl.root.left)
        avl.size = 3
        avl.right_rotate(avl.root)
        assert avl.root.value == 2
        assert avl.root.height == 1
        assert avl.root.left.value == 1
        assert avl.root.left.height == 0
        assert avl.root.right.value == 3
        assert avl.root.right.left == None
        assert avl.root.right.right == None
        assert avl.root.right.height == 0
        # # right right rotation with a parent
        # avl = AVLTree()
        # avl.root = Node(4)
        # avl.root.left = Node(3, parent=avl.root)
        # avl.root.left.left = Node(2, parent=avl.root.left)
        # avl.root.left.left.left = Node(1, parent=avl.root.left.left)
        # avl.size = 4
        # avl.right_rotate(avl.root.left)
        # assert avl.root.value == 4
        # assert avl.root.height == 2
        # assert avl.root.left.value == 2
        # assert avl.root.left.height == 1
        # assert avl.root.left.right.value == 3
        # assert avl.root.left.right.left == None
        # assert avl.root.left.right.right == None
        # assert avl.root.left.left.value == 1
        # assert avl.root.left.right.height == 0
        # assert avl.root.left.left.height == 0
        # assert avl.size == 4
        # # normal right left rotation
        # avl = AVLTree()
        # avl.root = Node(3)
        # avl.root.left = Node(1, parent=avl.root)
        # avl.root.left.right = Node(2, parent=avl.root.left)
        # avl.size = 3
        # avl.right_rotate(avl.root)
        # assert avl.root.value == 2
        # assert avl.root.height == 1
        # assert avl.root.left.value == 1
        # assert avl.root.left.right == None
        # assert avl.root.left.left == None
        # assert avl.root.right.value == 3
        # assert avl.root.right.right == None
        # assert avl.root.right.left == None
        # assert avl.root.left.height == 0
        # assert avl.root.right.height == 0
        # # right left rotation with a parent
        # avl = AVLTree()
        # avl.root = Node(4)
        # avl.root.left = Node(3, parent=avl.root)
        # avl.root.left.left = Node(1, parent=avl.root.left)
        # avl.root.left.left.right = Node(2, parent=avl.root.left.left)
        # avl.right_rotate(avl.root.left)
        # assert avl.root.value == 4
        # assert avl.root.height == 2
        # assert avl.root.left.value == 2
        # assert avl.root.left.height == 1
        # assert avl.root.left.left.value == 1
        # assert avl.root.left.left.right == None
        # assert avl.root.left.left.left == None
        # assert avl.root.left.right.value == 3
        # assert avl.root.left.right.right == None
        # assert avl.root.left.right.left == None
        # assert avl.root.left.left.height == 0
        # assert avl.root.left.right.height == 0
        # # assert avl.size == 4
        # assert avl.root.height == 2
        # # 1 left
        # avl = AVLTree()
        # avl.root = Node(4)
        # avl.root.left = Node(2, parent=avl.root)
        # avl.root.left.right = Node(3, parent=avl.root.left)
        # avl.root.left.left = Node(1, parent=avl.root.left)
        # avl.size = 4
        # avl.right_rotate(avl.root)
        # assert avl.root.value == 2
        # assert avl.root.left.value == 1
        # assert avl.root.right.value == 4
        # assert avl.root.right.left.value == 3
        # assert avl.size == 4
        # assert avl.root.height == 2
        # # 1 left WITH PARENT NODE
        # avl = AVLTree()
        # avl.root = Node(5, parent=None)
        # avl.root.left = Node(4, parent=avl.root)
        # avl.root.left.left = Node(2, parent=avl.root.left)
        # avl.root.left.left.right = Node(3, parent=avl.root.left.left)
        # avl.root.left.left.left = Node(1, parent=avl.root.left.left)
        # avl.size = 5
        # avl.right_rotate(avl.root.left)
        # assert avl.root.value == 5
        # assert avl.root.left.value == 2
        # assert avl.root.left.right.value == 4
        # assert avl.root.left.parent.value == 5
        # assert avl.root.left.left.value == 1
        # assert avl.root.left.right.left.value == 3
        # # assert avl.size == 5
        # # 1 right
        # avl = AVLTree()
        # avl.root = Node(1)
        # avl.root.right = Node(3, parent=avl.root)
        # avl.root.right.right = Node(4, parent=avl.root.right)
        # avl.root.right.left = Node(2, parent=avl.root.right)
        # avl.size = 4
        # avl.left_rotate(avl.root)
        # assert avl.root.value == 3
        # assert avl.root.left.value == 1
        # assert avl.root.right.value == 4
        # assert avl.root.left.right.value == 2
        # assert avl.size == 4
        # # 2 right
        # avl = AVLTree()
        # avl.root = Node(3)
        # avl.root.left = Node(2, parent=avl.root)
        # avl.root.left.left = Node(1, parent=avl.root.left)
        # avl.right_rotate(avl.root)
        # avl.size = 3
        # assert avl.root.value == 2
        # assert avl.root.left.value == 1
        # assert avl.root.right.value == 3
        # assert avl.size == 3
        # # # 2 left
        # avl = AVLTree()
        # avl.root = Node(1)
        # avl.root.right = Node(2, parent=avl.root)
        # avl.root.right.right = Node(3, parent=avl.root.right)
        # avl.left_rotate(avl.root)
        # avl.size = 3
        # assert avl.root.value == 2
        # assert avl.root.left.value == 1
        # assert avl.root.right.value == 3
        # assert avl.size == 3
        # # 3 right (left-right)
        # avl = AVLTree()
        # avl.root = Node(10)
        # avl.root.left = Node(5, parent=avl.root)
        # avl.root.left.right = Node(7, parent=avl.root.left)
        # avl.right_rotate(avl.root)
        # avl.size = 3
        # assert avl.root.value == 7
        # assert avl.root.parent == None
        # assert avl.root.height == 1
        # assert avl.root.left.value == 5
        # assert avl.root.left.left == None
        # assert avl.root.left.right == None
        # assert avl.root.left.height == 0
        # assert avl.root.left.parent.value == 7
        # assert avl.root.right.value == 10
        # assert avl.root.right.left == None
        # assert avl.root.right.right == None
        # assert avl.root.right.height == 0
        # assert avl.root.right.parent.value == 7
        # assert avl.size == 3
        # # 3 right (left-right) WITH PARENT NODE
        # avl = AVLTree()
        # avl.root = Node(4)
        # avl.root.left = Node(3, parent=avl.root)
        # avl.root.left.left = Node(1, parent=avl.root.left)
        # avl.root.left.left.right = Node(2, parent=avl.root.left.left)
        # avl.right_rotate(avl.root.left)
        # avl.size = 4
        # assert avl.root.value == 4
        # assert avl.root.left.left.value == 1
        # assert avl.root.left.right.value == 3
        # assert avl.size == 4
        # # # 3 left (right-left)
        # avl = AVLTree()
        # avl.root = Node(1)
        # avl.root.right = Node(3, parent=avl.root)
        # avl.root.right.left = Node(2, parent=avl.root.right)
        # avl.left_rotate(avl.root)
        # avl.size = 3
        # assert avl.root.value == 2
        # assert avl.root.left.value == 1
        # assert avl.root.right.value == 3
        # assert avl.root.right.left == None
        # assert avl.size == 3
        # # # 3 left (right-left) WITH PARENT NODE
        # avl = AVLTree()
        # avl.root = Node(0, parent=None)
        # avl.root.right = Node(1, parent=avl.root)
        # avl.root.right.right = Node(3, parent=avl.root.right)
        # avl.root.right.right.left = Node(2, parent=avl.root.right.right)
        # avl.left_rotate(avl.root.right)
        # avl.size = 4
        # assert avl.root.value == 0
        # assert avl.root.right.value == 2
        # assert avl.root.right.left.value == 1
        # assert avl.root.right.right.value == 3
        # assert avl.size == 4
        # # 4 right (left-left -> right-right)
        # avl = AVLTree()
        # avl.root = Node(4)
        # avl.root.left = Node(2, parent=avl.root)
        # avl.root.left.right = Node(3, parent=avl.root.left)
        # avl.root.left.left = Node(1, parent=avl.root.left)
        # avl.root.left.left.left = Node(0, parent=avl.root.left.left)
        # avl.root.right = Node(5, parent=avl.root)
        # avl.size = 6
        # avl.right_rotate(avl.root)
        # assert avl.root.value == 2
        # assert avl.root.left.value == 1
        # assert avl.root.left.left.value == 0
        # assert avl.root.right.value == 4
        # assert avl.root.right.left.value == 3
        # assert avl.root.right.right.value == 5
        # assert avl.size == 6
        # # # 4 right (left-left -> right-right) WITH PARENT NODE
        # avl = AVLTree()
        # avl.root = Node(6)
        # avl.root.left = Node(4, parent=avl.root)
        # avl.root.left.right = Node(5, parent=avl.root.left)
        # avl.root.left.left = Node(2, parent=avl.root.left)
        # avl.root.left.left.right = Node(3, parent=avl.root.left.left)
        # avl.root.left.left.left = Node(1, parent=avl.root.left.left)
        # avl.root.left.left.left.left = Node(0, parent=avl.root.left.left)
        # avl.size = 7
        # avl.right_rotate(avl.root.left)
        # assert avl.root.value == 6
        # assert avl.root.left.value == 2
        # assert avl.root.left.left.value == 1
        # assert avl.root.left.left.left.value == 0
        # assert avl.root.left.right.value == 4
        # assert avl.root.left.right.left.value == 3
        # assert avl.root.left.right.right.value == 5
        # assert avl.size == 7
        # # # 4 left (right-right -> left-left)
        # avl = AVLTree()
        # avl.root = Node(1)
        # avl.root.right = Node(3, parent=avl.root)
        # avl.root.right.right = Node(4, parent=avl.root.right)
        # avl.root.right.left = Node(2, parent=avl.root.right)
        # avl.root.right.right.right = Node(5, parent=avl.root.right.right)
        # avl.root.left = Node(0, parent=avl.root)
        # avl.size = 6
        # avl.left_rotate(avl.root)
        # assert avl.root.value == 3
        # assert avl.root.right.value == 4
        # assert avl.root.right.right.value == 5
        # assert avl.root.left.value == 1
        # assert avl.root.left.right.value == 2
        # assert avl.root.left.left.value == 0
        # assert avl.size == 6
        # # # 4 left (right-right -> left-left) WTIH PARENT
        # avl = AVLTree()
        # avl.root = Node(6, parent=None)
        # avl.root.left = Node(1, parent=avl.root)
        # avl.root.left.right = Node(3, parent=avl.root.left)
        # avl.root.left.right.right = Node(4, parent=avl.root.left.right)
        # avl.root.left.right.left = Node(2, parent=avl.root.left.right)
        # avl.root.left.right.right.right = Node(5, parent=avl.root.left.right.right)
        # avl.root.left.left = Node(0, parent=avl.root.left)
        # avl.size = 7
        # avl.left_rotate(avl.root.left)
        # assert avl.root.value == 6
        # assert avl.root.left.value == 3
        # assert avl.root.left.right.value == 4
        # assert avl.root.left.right.right.value == 5
        # assert avl.root.left.left.value == 1
        # assert avl.root.left.left.right.value == 2
        # assert avl.root.left.left.left.value == 0
        # assert avl.size == 7
        # # 4 pt 2 right (left-left variation -> right-right)
        # avl = AVLTree()
        # avl.root = Node(17)
        # avl.root.left = Node(9, parent=avl.root)
        # avl.root.left.right = Node(15, parent=avl.root.left)
        # avl.root.left.left = Node(6, parent=avl.root.left)
        # avl.root.left.left.right = Node(7, parent=avl.root.left.left)
        # avl.root.right = Node(26, parent=avl.root)
        # avl.size = 6
        # avl.right_rotate(avl.root)
        # assert avl.root.height == 2
        # assert avl.root.value == 9
        # assert avl.root.left.value == 6
        # assert avl.root.left.right.value == 7
        # assert avl.root.right.value == 17
        # assert avl.root.right.left.value == 15
        # assert avl.root.right.right.value == 26
        # assert avl.size == 6
        # # # 6 left to right
        # avl = AVLTree()
        # avl.root = Node(21)
        # avl.root.left = Node(6, parent=avl.root)
        # avl.root.left.right = Node(18, parent=avl.root.left)
        # avl.root.left.right.left = Node(14, parent=avl.root.left.right)
        # avl.root.left.left = Node(3, parent=avl.root.left)
        # avl.root.right = Node(26, parent=avl.root)
        # avl.size = 6
        # avl.right_rotate(avl.root)
        # assert avl.root.height == 2
        # assert avl.root.value == 18
        # assert avl.root.left.value == 6
        # assert avl.root.left.right.value == 14
        # assert avl.root.left.left.value == 3
        # assert avl.root.right.value == 21
        # assert avl.root.right.left == None
        # assert avl.root.right.right.value == 26
        # assert avl.size == 6
        # # 6 left to right WTIH PARENT NODE
        # avl = AVLTree()
        # avl.root = Node(28)
        # avl.root.left = Node(21, parent=avl.root)
        # avl.root.left.left = Node(6, parent=avl.root.left)
        # avl.root.left.left.right = Node(18, parent=avl.root.left.left)
        # avl.root.left.left.right.left = Node(14, parent=avl.root.left.left.right)
        # avl.root.left.left.left = Node(3, parent=avl.root.left.left)
        # avl.root.left.right = Node(26, parent=avl.root.left)
        # avl.size = 7
        # avl.right_rotate(avl.root.left)
        # assert avl.root.height == 3
        # assert avl.root.value == 28
        # assert avl.root.left.left.value == 6
        # assert avl.root.left.left.right.value == 14
        # assert avl.root.left.left.left.value == 3
        # assert avl.root.left.right.value == 21
        # assert avl.root.left.right.left == None
        # assert avl.root.left.right.right.value == 26
        # assert avl.size == 7
        # # 6 right to left
        # avl = AVLTree()
        # avl.root = Node(6)
        # avl.root.right = Node(21, parent=avl.root)
        # avl.root.right.left = Node(14, parent=avl.root.right)
        # avl.root.right.left.right = Node(18, parent=avl.root.right.left)
        # avl.root.right.right = Node(26, parent=avl.root.right)
        # avl.root.left = Node(3, parent=avl.root)
        # avl.size = 6
        # avl.left_rotate(avl.root)
        # assert avl.root.height == 2
        # assert avl.root.value == 14
        # assert avl.root.left.value == 6
        # assert avl.root.left.left.value == 3
        # assert avl.root.right.value == 21
        # assert avl.root.right.left.value == 18
        # assert avl.root.right.right.value == 26
        # assert avl.size == 6
        # # 5
        # avl = AVLTree()
        # avl.root = Node(21)
        # avl.root.left = Node(6, parent=avl.root)
        # avl.root.left.right = Node(18, parent=avl.root.left)
        # avl.root.left.right.height = 2
        # avl.root.left.right.left = Node(10, parent=avl.root.left.right)
        # avl.root.left.right.left.height = 1
        # avl.root.left.right.left.right = Node(14, parent=avl.root.left.right.left)
        # avl.root.left.right.right = Node(19, parent=avl.root.left.right)
        # avl.root.left.left = Node(3, parent=avl.root.left)
        # avl.root.left.left.height = 1
        # avl.root.left.left.right = Node(5, parent=avl.root.left.left)
        # avl.root.left.left.left = Node(1, parent=avl.root.left.left)
        # avl.root.right = Node(26, parent=avl.root)
        # avl.root.right.left = Node(24, parent=avl.root.right)
        # avl.root.right.right = Node(29, parent=avl.root.right)
        # avl.size = 12
        # avl.right_rotate(avl.root)
        # assert avl.root.height == 3
        # assert avl.root.value == 18
        # assert avl.root.parent == None
        # assert avl.root.left.value == 6
        # assert avl.root.left.right.value == 10
        # assert avl.root.left.right.right.value == 14
        # assert avl.root.left.left.value == 3
        # assert avl.root.left.left.right.value == 5
        # assert avl.root.left.left.left.value == 1
        # assert avl.root.right.value == 21
        # assert avl.root.right.left.value == 19
        # assert avl.root.right.right.value == 26
        # assert avl.root.right.right.left.value == 24
        # assert avl.root.right.right.right.value == 29
        # assert avl.size == 12


    def test_insert(self):
        #mimir last test
        avl3 = AVLTree()
        avl3.insert(avl3.root, 1)
        avl3.insert(avl3.root, 5)
        avl3.insert(avl3.root, 2)
        avl3.insert(avl3.root, 9)
        avl3.insert(avl3.root, 10)
        avl3.insert(avl3.root, 20)
        avl3.insert(avl3.root, 7)
        assert avl3.root.value == 9
        assert avl3.root.left.value == 2
        assert avl3.root.left.left.value == 1
        assert avl3.root.left.right.value == 5
        assert avl3.root.left.right.right.value == 7
        assert avl3.root.right.value == 10
        assert avl3.root.right.right.value == 20

        # no rebalance, standard insert
        avl = AVLTree()
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 1)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 7)
        assert avl.root.value == 5
        assert avl.root.height == 2
        assert avl.root.left.value == 1
        assert avl.root.left.parent.value == 5
        assert avl.root.left.height == 1
        assert avl.root.left.right.value == 3
        assert avl.root.left.right.parent.value == 1
        assert avl.root.right.value == 10
        assert avl.root.left.right.height == 0
        assert avl.root.right.left.value == 7
        assert avl.size == 5
        # forms a left left under the root
        # uses a right right rotation
        avl5 = AVLTree()
        avl5.insert(avl5.root, 2)
        avl5.insert(avl5.root, 3)
        avl5.insert(avl5.root, 4)
        avl5.insert(avl5.root, 1)
        avl5.insert(avl5.root, 0)
        assert avl5.root.value == 3
        assert avl5.root.height == 2
        assert avl5.root.left.value == 1
        assert avl5.root.left.parent.value == 3
        assert avl5.root.left.height == 1
        assert avl5.root.left.left.value == 0
        assert avl5.root.left.left.parent.value == 1
        assert avl5.root.left.right.value == 2
        assert avl5.root.left.right.parent.value == 1
        assert avl5.root.left.left.height == 0
        assert avl5.root.left.right.height == 0
        assert avl5.root.right.value == 4
        assert avl5.root.right.parent.value == 3
        assert avl5.root.right.height == 0
        assert avl5.size == 5
        # forms a right right under the right of the root
        # uses a left left rotation
        avl2 = AVLTree()
        avl2.insert(avl2.root, 3)
        avl2.insert(avl2.root, 2)
        avl2.insert(avl2.root, 1)
        avl2.insert(avl2.root, 4)
        avl2.insert(avl2.root, 5)
        assert avl2.root.value == 2
        assert avl2.root.height == 2
        assert avl2.root.left.value == 1
        assert avl2.root.left.height == 0
        assert avl2.root.right.value == 4
        assert avl2.root.right.parent.value == 2
        assert avl2.root.right.height == 1
        assert avl2.root.right.left.value == 3
        assert avl2.root.right.left.parent.value == 4
        assert avl2.root.right.right.value == 5
        assert avl2.root.right.right.parent.value == 4
        assert avl2.root.right.left.height == 0
        assert avl2.root.right.right.height == 0
        assert avl2.size == 5
        # when 2 is inserted there is a right left that uses a left right rotation
        # when 10 is inserted creates a right right under root, uses left left rotation
        # 20 is inserted uses a whole tree left left rotation to fix (case 4)
        avl3 = AVLTree()
        avl3.insert(avl3.root, 1)
        avl3.insert(avl3.root, 5)
        avl3.insert(avl3.root, 2)
        avl3.insert(avl3.root, 9)
        avl3.insert(avl3.root, 10)
        avl3.insert(avl3.root, 20)
        avl3.insert(avl3.root, 7)

        assert avl3.root.value == 9
        assert avl3.root.parent == None
        assert avl3.root.height == 3
        assert avl3.root.left.value == 2
        assert avl3.root.left.parent.value == 9
        assert avl3.root.left.height == 2
        assert avl3.root.left.left.value == 1
        assert avl3.root.left.left.parent.value == 2
        assert avl3.root.left.left.height == 0
        assert avl3.root.left.right.value == 5
        assert avl3.root.left.right.parent.value == 2
        assert avl3.root.left.right.height == 1
        assert avl3.root.left.right.right.value == 7
        assert avl3.root.right.value == 10
        assert avl3.root.right.parent.value == 9
        assert avl3.root.right.height == 1
        assert avl3.root.right.right.value == 20
        assert avl3.root.right.right.parent.value == 10
        assert avl3.root.right.right.height == 0
        assert avl3.size == 7
        # no rebalance, full level 2 tree
        avl4 = AVLTree()
        avl4.insert(avl4.root, 10)
        avl4.insert(avl4.root, 5)
        avl4.insert(avl4.root, 15)
        avl4.insert(avl4.root, 3)
        avl4.insert(avl4.root, 8)
        avl4.insert(avl4.root, 12)
        avl4.insert(avl4.root, 18)
        assert avl4.root.value == 10
        assert avl4.root.height == 2
        assert avl4.root.left.value == 5
        assert avl4.root.left.height == 1
        assert avl4.root.left.left.value == 3
        assert avl4.root.left.left.height == 0
        assert avl4.root.left.right.value == 8
        assert avl4.root.left.right.parent.value == 5
        assert avl4.root.right.value == 15
        assert avl4.root.right.parent.value == 10
        assert avl4.root.right.right.value == 18
        assert avl4.root.right.left.value == 12
        assert avl4.size == 7
        # min and max here too
        assert avl4.min(avl4.root).value == 3
        assert avl4.max(avl4.root).value == 18
        # inserting 1 creates a left left, uses a right right to fix
        avl6 = AVLTree()
        avl6.insert(avl6.root, 4)
        avl6.insert(avl6.root, 2)
        avl6.insert(avl6.root, 1)
        avl6.insert(avl6.root, 3)
        assert avl6.root.value == 2
        assert avl6.root.height == 2
        assert avl6.root.parent == None
        assert avl6.root.left.value == 1
        assert avl6.root.left.height == 0
        assert avl6.root.left.parent.value == 2
        assert avl6.root.right.value == 4
        assert avl6.root.right.height == 1
        assert avl6.root.right.parent.value == 2
        assert avl6.root.right.left.value == 3
        assert avl6.root.right.left.height == 0
        assert avl6.root.right.left.parent.value == 4
        assert avl6.size == 4
        # when 5 inserted uses a left left rotation to fix
        avl7 = AVLTree()
        avl7.insert(avl7.root, 1)
        avl7.insert(avl7.root, 0)
        avl7.insert(avl7.root, 3)
        avl7.insert(avl7.root, 2)
        avl7.insert(avl7.root, 4)
        avl7.insert(avl7.root, 5)
        assert avl7.root.value == 3
        assert avl7.root.height == 2
        assert avl7.root.parent == None
        assert avl7.root.left.value == 1
        assert avl7.root.left.height == 1
        assert avl7.root.left.parent.value == 3
        assert avl7.root.right.value == 4
        assert avl7.root.right.height == 1
        assert avl7.root.right.parent.value == 3
        assert avl7.root.right.right.value == 5
        assert avl7.root.right.right.height == 0
        assert avl7.root.right.right.parent.value == 4
        assert avl7.root.left.left.height == 0
        assert avl7.root.left.left.value == 0
        assert avl7.root.left.left.parent.value == 1
        assert avl7.root.left.right.height == 0
        assert avl7.root.left.right.value == 2
        assert avl7.root.left.right.parent.value == 1
        assert avl7.size == 6
        # right right to fix on insert 7
        avl8 = AVLTree()
        avl8.insert(avl8.root, 17)
        avl8.insert(avl8.root, 26)
        avl8.insert(avl8.root, 9)
        avl8.insert(avl8.root, 6)
        avl8.insert(avl8.root, 15)
        avl8.insert(avl8.root, 7)
        assert avl8.root.value == 9
        assert avl8.root.height == 2
        assert avl8.root.parent == None
        assert avl8.root.left.value == 6
        assert avl8.root.left.height == 1
        assert avl8.root.left.parent.value == 9
        assert avl8.root.left.right.value == 7
        assert avl8.root.left.right.height == 0
        assert avl8.root.left.right.parent.value == 6
        assert avl8.root.right.value == 17
        assert avl8.root.right.height == 1
        assert avl8.root.right.parent.value == 9
        assert avl8.root.right.right.value == 26
        assert avl8.root.right.right.height == 0
        assert avl8.root.right.right.parent.value == 17
        assert avl8.root.right.left.height == 0
        assert avl8.root.right.left.value == 15
        assert avl8.root.right.left.parent.value == 17
        assert avl8.size == 6
        # 14 causes a left right, right left is used to fix
        avl9 = AVLTree()
        avl9.insert(avl9.root, 21)
        avl9.insert(avl9.root, 26)
        avl9.insert(avl9.root, 6)
        avl9.insert(avl9.root, 3)
        avl9.insert(avl9.root, 18)
        avl9.insert(avl9.root, 24)
        avl9.insert(avl9.root, 29)
        avl9.insert(avl9.root, 1)
        avl9.insert(avl9.root, 5)
        avl9.insert(avl9.root, 10)
        avl9.insert(avl9.root, 19)
        avl9.insert(avl9.root, 14)
        assert avl9.root.value == 18
        assert avl9.root.height == 3
        assert avl9.root.parent == None
        assert avl9.root.left.value == 6
        assert avl9.root.left.height == 2
        assert avl9.root.left.parent.value == 18
        assert avl9.root.left.right.value == 10
        assert avl9.root.left.right.height == 1
        assert avl9.root.left.right.parent.value == 6
        assert avl9.root.left.right.right.value == 14
        assert avl9.root.left.right.right.height == 0
        assert avl9.root.left.right.right.parent.value == 10
        assert avl9.root.left.left.value == 3
        assert avl9.root.left.left.height == 1
        assert avl9.root.left.left.parent.value == 6
        assert avl9.root.left.left.right.value == 5
        assert avl9.root.left.left.right.height == 0
        assert avl9.root.left.left.right.parent.value == 3
        assert avl9.root.left.left.left.value == 1
        assert avl9.root.left.left.left.height == 0
        assert avl9.root.left.left.left.parent.value == 3
        assert avl9.root.right.value == 21
        assert avl9.root.right.height == 2
        assert avl9.root.right.parent.value == 18
        assert avl9.root.right.right.value == 26
        assert avl9.root.right.right.height == 1
        assert avl9.root.right.right.parent.value == 21
        assert avl9.root.right.left.height == 0
        assert avl9.root.right.left.value == 19
        assert avl9.root.right.left.parent.value == 21
        assert avl9.root.right.right.left.value == 24
        assert avl9.root.right.right.left.height == 0
        assert avl9.root.right.right.left.parent.value == 26
        assert avl9.root.right.right.right.value == 29
        assert avl9.root.right.right.right.height == 0
        assert avl9.root.right.right.right.parent.value == 26
        assert avl9.size == 12
        #left right so used a right left rotation to fix
        avl10 = AVLTree()
        avl10.insert(avl10.root, 21)
        avl10.insert(avl10.root, 26)
        avl10.insert(avl10.root, 6)
        avl10.insert(avl10.root, 3)
        avl10.insert(avl10.root, 18)
        avl10.insert(avl10.root, 17)
        avl10.insert(avl10.root, 19)
        assert avl10.root.value == 18
        assert avl10.root.height == 2
        assert avl10.root.parent == None
        assert avl10.root.left.value == 6
        assert avl10.root.left.height == 1
        assert avl10.root.left.parent.value == 18
        assert avl10.root.left.right.value == 17
        assert avl10.root.left.right.height == 0
        assert avl10.root.left.right.parent.value == 6
        assert avl10.root.right.right.value == 26
        assert avl10.root.right.right.height == 0
        assert avl10.root.right.right.parent.value == 21
        assert avl10.root.right.value == 21
        assert avl10.root.right.left.value == 19
        assert avl10.root.right.height == 1
        assert avl10.root.right.parent.value == 18
        assert avl10.root.left.left.value == 3
        assert avl10.root.left.left.height == 0
        assert avl10.root.left.left.parent.value == 6
        assert avl10.size == 7
        #right left so used a left right rotation to fix
        avl11 = AVLTree()
        avl11.insert(avl11.root, 1)
        avl11.insert(avl11.root, 0)
        avl11.insert(avl11.root, 5)
        avl11.insert(avl11.root, 3)
        avl11.insert(avl11.root, 6)
        avl11.insert(avl11.root, 4)
        assert avl11.root.value == 3
        assert avl11.root.height == 2
        assert avl11.root.parent == None
        assert avl11.root.left.value == 1
        assert avl11.root.left.height == 1
        assert avl11.root.left.parent.value == 3
        assert avl11.root.left.left.value == 0
        assert avl11.root.left.left.height == 0
        assert avl11.root.left.left.parent.value == 1
        assert avl11.root.right.right.value == 6
        assert avl11.root.right.right.height == 0
        assert avl11.root.right.right.parent.value == 5
        assert avl11.root.right.value == 5
        assert avl11.root.right.parent.value == 3
        assert avl11.root.right.height == 1
        assert avl11.root.right.parent.value == 3
        assert avl11.root.right.left.value == 4
        assert avl11.root.right.left.height == 0
        assert avl11.root.right.left.parent.value == 5
        assert avl11.min(avl11.root).value == 0
        assert avl11.max(avl11.root).value == 6
        assert avl11.size == 6

        # 3 right right left rotation
        avl = AVLTree()
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 7)
        assert avl.root.value == 7
        assert avl.root.parent == None
        assert avl.root.height == 1
        assert avl.root.left.value == 5
        assert avl.root.left.left == None
        assert avl.root.left.right == None
        assert avl.root.left.height == 0
        assert avl.root.left.parent.value == 7
        assert avl.root.right.value == 10
        assert avl.root.right.left == None
        assert avl.root.right.right == None
        assert avl.root.right.height == 0
        assert avl.root.right.parent.value == 7
        assert avl.size == 3

        # 3 noormal left right rotation
        avl = AVLTree()
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 4)
        assert avl.root.value == 4
        assert avl.root.parent == None
        assert avl.root.height == 1
        assert avl.root.left.value == 3
        assert avl.root.left.left == None
        assert avl.root.left.right == None
        assert avl.root.left.height == 0
        assert avl.root.left.parent.value == 4
        assert avl.root.right.value == 5
        assert avl.root.right.left == None
        assert avl.root.right.right == None
        assert avl.root.right.height == 0
        assert avl.root.right.parent.value == 4
        assert avl.size == 3
        # 3 left right rotation with root
        avl = AVLTree()
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 6)
        assert avl.root.value == 4
        assert avl.root.parent == None
        assert avl.root.height == 2
        assert avl.height(avl.root) == 2
        assert avl.root.left.value == 3
        assert avl.root.left.left == None
        assert avl.root.left.right == None
        assert avl.root.left.height == 0
        assert avl.height(avl.root.left) == 0
        assert avl.root.left.parent.value == 4
        assert avl.root.right.value == 6
        assert avl.root.right.height == 1
        assert avl.root.right.parent.value == 4
        assert avl.root.right.left.value == 5
        assert avl.root.right.left.left == None
        assert avl.root.right.left.right == None
        assert avl.root.right.left.height == 0
        assert avl.root.right.left.parent.value == 6
        assert avl.root.right.right.value == 7
        assert avl.root.right.right.right == None
        assert avl.root.right.right.left == None
        assert avl.root.right.right.height == 0
        assert avl.root.right.right.parent.value == 6
        assert avl.size == 5

        # 3 (right left)
        # checks normal left left rotation and left left with root
        avl = AVLTree()
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 6)
        avl.insert(avl.root, 7)
        assert avl.root.value == 4
        assert avl.root.parent == None
        assert avl.root.height == 2
        assert avl.root.left.value == 3
        assert avl.root.left.parent.value == 4
        assert avl.root.left.height == 0
        assert avl.root.right.value == 6
        assert avl.root.right.parent.value == 4
        assert avl.root.right.height == 1
        assert avl.root.right.right.value == 7
        assert avl.root.right.right.parent.value == 6
        assert avl.root.right.right.height == 0
        assert avl.root.right.left.value == 5
        assert avl.root.right.left.parent.value == 6
        assert avl.root.right.left.height == 0
        # checks normal right right rotation and right right with root
        avl = AVLTree()
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 2)
        avl.insert(avl.root, 1)
        assert avl.root.value == 4
        assert avl.root.parent == None
        assert avl.root.height == 2
        assert avl.root.left.value == 2
        assert avl.root.left.parent.value == 4
        assert avl.root.left.height == 1
        assert avl.root.left.left.value == 1
        assert avl.root.left.left.parent.value == 2
        assert avl.root.left.left.height == 0
        assert avl.root.left.right.value == 3
        assert avl.root.left.right.parent.value == 2
        assert avl.root.left.right.height == 0
        assert avl.root.right.value == 5
        assert avl.root.right.parent.value == 4
        assert avl.root.right.height == 0

        avl = AVLTree()
        avl.insert(avl.root, 2)
        avl.insert(avl.root, 2)
        avl.insert(avl.root, 2)
        assert avl.root.value == 2
        assert avl.root.parent == None
        assert avl.root.height == 0
        assert avl.root.left == None
        assert avl.root.right == None
        assert avl.size == 1
        assert avl.height(avl.root) == 0




    def test_search(self):
        avl = AVLTree()

        avl.insert(avl.root, 30)
        avl.insert(avl.root, 20)
        avl.insert(avl.root, 40)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 25)
        avl.insert(avl.root, 35)
        avl.insert(avl.root, 50)

        assert avl.search(avl.root, 10) == avl.root.left.left
        assert avl.search(avl.root, 50) == avl.root.right.right
        assert avl.search(avl.root, 20) == avl.root.left
        assert avl.search(avl.root, 22) == avl.root.left.right

        avl1 = AVLTree()
        assert avl.search(avl1.root, 10) == None
    #
    def test_remove(self):
        avl = AVLTree()
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 15)
        avl.insert(avl.root, 1)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 13)
        avl.insert(avl.root, 19)
        # normal remove of right leaf node
        avl.remove(avl.root, 7)
        assert avl.root.left.right == None
        assert avl.size == 6
        # normal remove of left leaf node
        avl.remove(avl.root, 1)
        assert avl.root.left.left == None
        assert avl.root.left.height == 0
        assert avl.size == 5
        # remove that causes imbalance
        avl.remove(avl.root, 5)
        assert avl.root.value == 15
        assert avl.root.left.value == 10
        assert avl.root.right.value == 19
        assert avl.root.left.right.value == 13
        assert avl.size == 4

        #removing a node with two children
        avl11 = AVLTree()
        avl11.insert(avl11.root, 1)
        avl11.insert(avl11.root, 0)
        avl11.insert(avl11.root, 5)
        avl11.insert(avl11.root, 3)
        avl11.insert(avl11.root, 6)
        avl11.insert(avl11.root, 4)
        avl11.remove(avl11.root, 5)
        assert avl11.size == 5
        assert avl11.root.value == 3
        assert avl11.root.height == 2
        assert avl11.root.parent == None
        assert avl11.root.left.value == 1
        assert avl11.root.left.height == 1
        assert avl11.root.left.parent.value == 3
        assert avl11.root.right.value == 4
        assert avl11.root.right.height == 1
        assert avl11.root.right.parent.value == 3
        assert avl11.root.right.right.value == 6
        assert avl11.root.right.right.height == 0
        assert avl11.root.right.right.parent.value == 4

        #removing a node with two children and more coming after it
        avl11 = AVLTree()
        avl11.insert(avl11.root, 8)
        avl11.insert(avl11.root, 5)
        avl11.insert(avl11.root, 12)
        avl11.insert(avl11.root, 3)
        avl11.insert(avl11.root, 6)
        avl11.insert(avl11.root, 10)
        avl11.insert(avl11.root, 13)
        avl11.insert(avl11.root, 2)
        avl11.insert(avl11.root, 4)
        avl11.insert(avl11.root, 9)
        avl11.insert(avl11.root, 11)
        # avl11.remove(avl11.root, 11)
        avl11.remove(avl11.root, 5)
        assert avl11.root.value == 8
        assert avl11.root.height == 3
        assert avl11.root.parent == None
        assert avl11.root.left.value == 4
        assert avl11.root.left.height == 2
        assert avl11.root.left.parent.value == 8
        assert avl11.root.left.right.value == 6
        assert avl11.root.left.right.height == 0
        assert avl11.root.left.right.parent.value == 4
        assert avl11.root.left.left.value == 3
        assert avl11.root.left.left.height == 1
        assert avl11.root.left.left.parent.value == 4
        assert avl11.root.left.left.left.value == 2
        assert avl11.root.left.left.left.height == 0
        assert avl11.root.left.left.left.parent.value == 3
        assert avl11.root.right.value == 12
        assert avl11.root.right.height == 2
        assert avl11.root.right.parent.value == 8
        assert avl11.root.right.right.value == 13
        assert avl11.root.right.right.height == 0
        assert avl11.root.right.right.parent.value == 12
        assert avl11.root.right.left.value == 10
        assert avl11.root.right.left.height == 1
        assert avl11.root.right.left.parent.value == 12
        assert avl11.root.right.left.left.value == 9
        assert avl11.root.right.left.left.height == 0
        assert avl11.root.right.left.left.parent.value == 10
        assert avl11.root.right.left.right.value == 11
        assert avl11.root.right.left.right.height == 0
        assert avl11.root.right.left.right.parent.value == 10
        assert avl11.size == 10
        # removing root node with 2 children
        avl = AVLTree()
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 2)
        avl.insert(avl.root, 4)
        avl.remove(avl.root, 3)
        assert avl.root.value == 2
        assert avl.root.height == 1
        assert avl.root.parent == None
        assert avl.root.left == None
        assert avl.root.right.value == 4
        assert avl.root.right.height == 0
        assert avl.root.right.parent.value == 2
        # removing root node with 2 children, children have children
        avl = AVLTree()
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 6)
        avl.insert(avl.root, 4)
        avl.remove(avl.root, 5)
        assert avl.root.value == 4
        assert avl.root.height == 1
        assert avl.root.parent == None
        assert avl.root.left.value == 3
        assert avl.root.left.height == 0
        assert avl.root.left.parent.value == 4
        assert avl.root.right.value == 6
        assert avl.root.right.height == 0
        assert avl.root.right.parent.value == 4
        # removing internal with left node only
        avl = AVLTree()
        avl.insert(avl.root, 6)
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 9)
        avl.insert(avl.root, 2)
        avl.remove(avl.root, 4)
        assert avl.root.value == 6
        assert avl.root.left.value == 2
        assert avl.root.right.value == 8
        assert avl.root.right.right.value == 9
        assert avl.root.right.left.value == 7
        # removing internal with right node only
        avl = AVLTree()
        avl.insert(avl.root, 6)
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 9)
        avl.insert(avl.root, 5)
        test = avl.remove(avl.root, 4)
        assert test.value == 6
        assert avl.root.value == 6
        assert avl.root.height == 2
        assert avl.root.left.value == 5
        assert avl.root.left.height == 0
        assert avl.root.left.parent.value == 6
        assert avl.root.right.value == 8
        assert avl.root.right.right.value == 9
        assert avl.root.right.left.value == 7
        assert avl.size == 5
        avl = AVLTree()
        avl.insert(avl.root, 4)
        avl.insert(avl.root, 6)
        test = avl.remove(avl.root, 4)
        assert test.value == 6
        assert avl.root.value == 6
        assert avl.root.height == 0
        assert avl.root.parent == None
        assert avl.root.left == None
        assert avl.root.right == None




    def test_traversals(self):
        avl = AVLTree()

        avl.insert(avl.root, 14)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 21)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 17)
        avl.insert(avl.root, 25)
    #
        gen1 = avl.preorder(avl.root)
        gen2 = avl.postorder(avl.root)
        gen3 = avl.inorder(avl.root)
        gen4 = avl.breadth_first(avl.root)
    #
        pre = [14, 7, 3, 10, 21, 17, 25]
        post = [3, 10, 7, 17, 25, 21, 14]
        inorder = sorted(post)
        bfs = [14, 7, 21, 3, 10, 17, 25]
    #
        for i in range(7):
            assert next(gen1, None).value == pre[i]
            assert next(gen2, None).value == post[i]
            assert next(gen3, None).value == inorder[i]
            assert next(gen4, None).value == bfs[i]

    def test_depth_height(self):
        avl = AVLTree()
        avl.insert(avl.root, 21)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 32)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 16)
        avl.insert(avl.root, 27)
        avl.insert(avl.root, 39)
        assert avl.depth(5) == 2
        assert avl.depth(10) == 1
        assert avl.height(avl.root) == 2
        assert avl.height(avl.root.left) == 1

        avl = AVLTree()
        avl.insert(avl.root, 23)
        avl.insert(avl.root, 12)
        avl.insert(avl.root, 34)
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 15)
        avl.insert(avl.root, 30)
        avl.insert(avl.root, 35)
        avl.insert(avl.root, 37)
        avl.insert(avl.root, 1)
        avl.insert(avl.root, 11)
        avl.insert(avl.root, 14)
        avl.insert(avl.root, 17)
        avl.insert(avl.root, 25)
        avl.insert(avl.root, 32)

        assert avl.height(avl.root) == 3
        assert avl.height(avl.root.left) == 2
        assert avl.height(avl.root.right) == 2
        assert avl.height(avl.root.left.left) == 1
        assert avl.height(avl.root.left.left.left) == 0
        assert avl.height(avl.root.right.right) == 1
        assert avl.height(avl.root.right.left) == 1
        assert avl.height(avl.root.left.right.right) == 0


    def test_min_and_max(self):
        avl = AVLTree()

        avl.insert(avl.root, 10)
        avl.insert(avl.root, 5)
        avl.insert(avl.root, 15)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 12)
        avl.insert(avl.root, 18)

        assert avl.min(avl.root).value == 3
        assert avl.max(avl.root).value == 18
    #
    def test_sum_update(self):
        avl = AVLTree()

        """
        Structure of initial tree:
              10
             /  \
            8   12
           / \  / \
          7  9 11  13
        """
        """
        Structure of final tree:

              46
             /  \
            25   63
           / \   / \
          13 36 55  70
        """
        total = 0
        avl.insert(avl.root, 10)
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 12)
        avl.insert(avl.root, 7)
        avl.insert(avl.root, 9)
        avl.insert(avl.root, 11)
        avl.insert(avl.root, 13)
        avl.insert(avl.root, 45)
        avl.insert(avl.root,36)
        avl.insert(avl.root, 2)
        avl.insert(avl.root, 21)
        avl.insert(avl.root, 65)
        avl.insert(avl.root, 20)
        avl.insert(avl.root, 14)
        avl.insert(avl.root, 3)
        avl.insert(avl.root, 18)
        avl.insert(avl.root, 30)
        avl.insert(avl.root, 29)
        avl.insert(avl.root, 54)


        sum_update(avl.root, 0)
        """
        Structure of final tree:

              46
             /  \
            25   63
           / \   / \
          13 36 55  70
        """
        x = avl.inorder(avl.root)
        sol = [13, 25, 36, 46, 55, 63, 70]

        for i in range(7):
            assert next(x, None).value == sol[i]

        avl = AVLTree()
        avl.insert(avl.root, 8)
        avl.insert(avl.root, 4)
        sum_update(avl.root, 0)
        assert avl.root.value == 8
        assert avl.root.right.value == 12
        assert avl.root.left == None


        # x = avl.inorder(avl.root)
        #
        # sol = [11,21,30,38,42,45]
        #
        # for i in range(0,7):
        #     print(next(x, None).value)
            # assert next(x, None).value == sol[i]

    # def your_test_here(self):
    #
    #     avl = AVLTree()
    #     assert avl.root is None

if __name__ == "__main__":
    unittest.main()
