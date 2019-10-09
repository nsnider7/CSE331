import unittest
from QuickSort import *
from DoublyLinkedList import DLL
from InsertionSort import insertion_sort


class TestProject1(unittest.TestCase):

    def test_accessors(self):
        dll = DLL([])

        assert dll.get_size() == 0
        assert dll.get_head() is None
        assert dll.get_tail() is None

        orig = [3,2,1]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)

        # print(dll)
        # print(DLL(sorted(orig)))
        # assert dll == DLL(sorted(orig))
        assert dll.get_size() == 3
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 3
        #
        orig = [9,2,7,1,3,6,4,5]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 4)

        # print(dll)
        assert dll == DLL(sorted(orig))
        assert dll.get_size() == 8
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 9

        orig = [1, 1, 1, 0, 1, 1, 1]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 4)

        # print(dll)
        assert dll == DLL(sorted(orig))
        assert dll.get_size() == 7
        assert dll.get_head().get_value() == 0
        assert dll.get_tail().get_value() == 1

        orig = [-1,4,5,-2,0]
        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)
        # print(dll)
        # print(dll.c)
        assert dll == DLL(sorted(orig))
        assert dll.c == 0



    def test_insertion(self):
        dll = DLL([])

        assert dll.get_size() == 0
        assert dll.get_head() is None
        assert dll.get_tail() is None

        # normal
        orig = [6, 1, 4, 7, 3, 5, 10, 8, 9, 2]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # size 1
        orig = [6]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # acending
        orig = [6,5,4,3,2,1]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # scattered
        orig = [1,8,2,7,3,6,4,6]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # size 2
        orig = [-4,-3,-2,-1]
        dll = DLL(orig)
        insertion_sort(dll, dll.get_head(), dll.get_tail())
        assert dll == DLL(sorted(orig))

        # # parameter flopped
        # orig = [4,3,2,1]
        # dll = DLL(orig)
        # print(dll)
        # insertion_sort(dll, dll.get_tail(), dll.get_head())
        # assert dll == DLL(sorted(orig))


    def test_quick_sort(self):
        orig = [9, 2, 7, 1, 3, 6, 4, 5]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 0)


        assert dll == DLL(sorted(orig))
        assert dll.c == 0

    def test_guick_insertion(self):
        orig = [20, 18, 4, 2, 5, 7, 13, 10, 11, 3, 1, 17, 16, 9, 6, 8, 15, 12, 14, 19]

        dll = DLL(orig)
        quick_sort(dll, dll.head, dll.tail, dll.size, 15)

        assert dll == DLL(sorted(orig))
        assert dll.c == 2

    def test_application(self):
        dll = DLL([2,1,1])
        dll.count_unique()
        assert dll == DLL([2,1,2])


        dll = DLL([1,3,3,4,4,4])
        dll.count_unique()
        assert dll == DLL([1,3,2,4,3])
        assert dll.get_head().get_value() == 1
        assert dll.get_tail().get_value() == 3
        assert dll.get_size() == 5

    def test_partition(self):
        # 1 ele check
        dll = DLL([2])
        test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)

        # 2 ele unsorted check
        dll = DLL([2,1])
        test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)
        # decending list of 4 check
        dll = DLL([4,3,2,1])
        test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)

        # random unordered list of 4
        dll = DLL([4,1,2,3])
        test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)
        # duplicate list
        dll = DLL([1,1,1,1,0,1,1,1])
        test = partition(dll.get_head(), dll.get_tail())
        # print(dll)
        # print(test)

        dll = DLL([3,6,5,4])
        test = partition(dll.get_head().get_next(), dll.get_tail())
        # print(dll)
        # print(test)
        # dll = DLL([2,1])
        # quick_sort(dll, dll.get_head(), dll.get_tail(), dll.get_size(), 2)
        # insertion_sort(dll, dll.get_head(), dll.get_tail())


if __name__ == "__main__":
    unittest.main()
