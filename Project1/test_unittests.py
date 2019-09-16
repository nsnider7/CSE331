import unittest
from DLL import DLL, DLLNode, remove_middle


class TestProject1(unittest.TestCase):

    # def test_inserts(self):
    #     lst = DLL()
    #     lst.insert_front(1)
    #     lst.insert_front(2)
    #     lst.insert_front(3)
    #     lst.insert_back(4)
    #     lst.insert_back(5)
    #
    #     self.assertEqual(lst.head.get_value(), 3)
    #     self.assertEqual(lst.tail.get_value(), 5)
    #
    #     forward, backward = [], []
    #     head = lst.head
    #     while head is not None:
    #         forward.append(head.get_value())
    #         head = head.get_next()
    #     tail = lst.tail
    #     while tail is not None:
    #         backward.append(tail.get_value())
    #         tail = tail.get_previous()
    #
    #     self.assertEqual(forward, [3, 2, 1, 4, 5])
    #     self.assertEqual(backward, [5, 4, 1, 2, 3])

    def test_get_size(self):
        lst = DLL()
        self.assertEqual(lst.get_size(), 0)

    def test_is_empty(self):
        lst = DLL()
        self.assertEqual(lst.is_empty(), True)

    def test_insert_front(self):
        lst = DLL()
        lst.insert_front('test')
        self.assertTrue(lst)

    def test_insert_back(self):
        lst = DLL()
        lst.insert_back(1)
        lst.insert_back(2)
        lst.insert_back(3)
        print(lst)
        self.assertEqual(lst, [1, 2, 3])

    # def test_delete_front(self):
    #     lst = DLL()
    #     lst.insert_front(0)
    #     lst.insert_front(1)
    #     lst.insert_front(2)
    #
    #     self.assertEqual(lst.head, DLL(2))


if __name__ == "__main__":
    unittest.main()
