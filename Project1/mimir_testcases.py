import unittest
from DLL import DLL, DLLNode, remove_middle


class TestProject1(unittest.TestCase):

    def test_inserts(self):
        lst = DLL()
        lst.insert_front(1)
        lst.insert_front(2)
        lst.insert_front(3)
        lst.insert_back(4)
        lst.insert_back(5)

        self.assertEqual(lst.head.get_value(), 3)
        self.assertEqual(lst.tail.get_value(), 5)

        forward, backward = [], []
        head = lst.head
        while head is not None:
            forward.append(head.get_value())
            head = head.get_next()
        tail = lst.tail
        while tail is not None:
            backward.append(tail.get_value())
            tail = tail.get_previous()

        self.assertEqual(forward, [3, 2, 1, 4, 5])
        self.assertEqual(backward, [5, 4, 1, 2, 3])

    def test_accessors(self):
        lst = DLL()

        self.assertTrue(lst.is_empty())
        self.assertEqual(lst.get_size(), 0)

        for _ in range(5):
            lst.insert_front(1)

        self.assertTrue(not lst.is_empty())
        self.assertEqual(lst.get_size(), 5)

        for _ in range(3):
            lst.delete_front()

        self.assertTrue(not lst.is_empty())
        self.assertEqual(lst.get_size(), 2)

    def test_deletes(self):
        def condense(linkedlist):
            res = list()
            node = linkedlist.head
            while node is not None:
                res.append(node.get_value())
                node = node.get_next()
            return res

        lst = DLL()
        inserts = [1, 4, 0, 10, 3, 7, 9]

        for x in inserts:
            lst.insert_back(x)

        lst.delete_front()
        inserts.pop(0)

        self.assertEqual(inserts, condense(lst))
        print(lst)
        lst.delete_back()
        inserts.pop()

        self.assertEqual(inserts, condense(lst))

    def test_delete_value_all(self):
        def condense(linkedlist):
            res = list()
            node = linkedlist.head
            while node is not None:
                res.append(node.get_value())
                node = node.get_next()
            return res
        # Delete val
        # head delete test
        lst = DLL()
        insert = [1, 2, 3, 4, 5, 6, 1, 1, 2, 4, 1, 9]
        for i in insert:
            lst.insert_back(i)
        lst.delete_value(1)
        self.assertEqual(condense(lst), insert[1:])

        ## head delete test
        lst = DLL()
        insert = [1, 2, 3, 9]
        for i in insert:
            lst.insert_back(i)
        lst.delete_value(9)
        self.assertEqual(condense(lst), insert[:3])

        ## regular in list delete test
        my_lst = DLL()
        my_insert = [1, 2, 3, 4, 5]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_value(3)
        self.assertEqual(condense(my_lst), [1, 2, 4, 5])

        ## if not in list
        my_lst = DLL()
        my_insert = [1, 2, 3, 4, 5, 6, 1, 1, 2, 4, 1, 9]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_value(8)
        self.assertEqual(condense(my_lst), [1, 2, 3, 4, 5, 6, 1, 1, 2, 4, 1, 9])

        ## empty list
        my_lst = DLL()
        my_lst.delete_value(8)
        self.assertEqual(my_lst.size, 0)

        ## Delete all
        ## no val
        my_lst = DLL()
        my_insert = [1, 2, 3, 4, 5]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_all(8)
        self.assertEqual(condense(my_lst), [1, 2, 3, 4, 5])

        ## right next to eachother vals
        my_lst = DLL()
        my_insert = [1, 2, 2, 4, 5]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_all(2)
        self.assertEqual(condense(my_lst), [1, 4, 5])

        ## val is head
        my_lst = DLL()
        my_insert = [1, 2, 2, 4, 5]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_all(1)
        self.assertEqual(condense(my_lst), [2, 2, 4, 5])

        ## val is tail
        my_lst = DLL()
        my_insert = [1, 2, 2, 4, 5]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_all(5)
        self.assertEqual(condense(my_lst), [1, 2, 2, 4])

        ## val is head and tail
        my_lst = DLL()
        my_insert = [1, 2, 2, 4, 1]
        for i in my_insert:
            my_lst.insert_back(i)
        my_lst.delete_all(1)
        self.assertEqual(condense(my_lst), [2, 2, 4])
        self.assertEqual(my_lst.head, 2)
        # lst.delete_all(1)
        # self.assertEqual(condense(lst), [2, 3, 4, 5, 6, 2, 4, 9])

    def test_finds(self):
        lst = DLL()
        inserts = [9, 16, 5, 58, 32, 1, 4, 58, 67, 2, 4]

        for i in inserts:
            lst.insert_back(i)

        first = lst.find_first(32)

        self.assertEqual(first.get_value(), 32)
        self.assertEqual(first.get_next().get_value(), 1)
        self.assertEqual(first.get_previous().get_value(), 58)

        # my tests
        inserts = [8, 9, 9, 9, 9]
        new_lst = DLL()
        for i in inserts:
            new_lst.insert_back(i)
        first = new_lst.find_first(0)

        self.assertEqual(first, None)
        # self.assertEqual(first.get_next().get_value(), None)
        # self.assertEqual(first.get_previous().get_value(), None)
        #

        last = lst.find_last(2)

        self.assertEqual(last.get_value(), 2)
        self.assertEqual(last.get_next().get_value(), 4)
        self.assertEqual(last.get_previous().get_value(), 67)

        list_of_58s = lst.find_all(58)

        self.assertEqual(len(list_of_58s), 2)
        for i in list_of_58s:
            self.assertEqual(i.get_value(), 58)

        first = list_of_58s[0]
        second = list_of_58s[1]

        self.assertEqual(first.get_next().get_value(), 32)
        self.assertEqual(first.get_previous().get_value(), 5)

        self.assertEqual(second.get_next().get_value(), 67)
        self.assertEqual(second.get_previous().get_value(), 4)

    # def test_count_sum(self):
    #     lst = DLL()
    #     inserts = [1, 3, 1, 4, 5, 6, 1, 3, 8]
    #
    #     for i in inserts:
    #         lst.insert_back(i)
    #
    #     self.assertEqual(lst.count(1), 3)
    #     self.assertEqual(lst.sum(), 32)
    #
    # def test_remove_middle(self):
    #     def condense(linkedlist):
    #         res = list()
    #         node = linkedlist.head
    #         while node is not None:
    #             res.append(node.get_value())
    #             node = node.get_next()
    #         return res
    #
    #     lst = DLL()
    #     inserts = [1, 2, 3, 4, 5]
    #
    #     for i in inserts:
    #         lst.insert_back(i)
    #
    #     new = remove_middle(lst)
    #
    #     self.assertEqual(condense(new), [1, 2, 4, 5])


if __name__ == "__main__":
    unittest.main()
