import unittest
from PriorityHeap import Node, PriorityHeap, heap_sort, merge_lists
from string import ascii_lowercase


class TestProject6(unittest.TestCase):
    def test_push(self):
        '''
        simple push cases, requires functioning top
        '''

        heap = PriorityHeap()
        heap.push(5, 'c')
        # test = heap.top()
        # assert test == Node(5, 'c')
        heap.push(4, 'y')
        # test = heap.top()
        # assert test == Node(4, 'y')
        heap.push(3, 'n')
        # test = heap.top()
        # assert test == Node(3, 'n')
        heap.push(2, 'd')
        # test = heap.top()
        # assert test == Node(2, 'd')
        heap.push(5, 'y')
        assert len(heap._data) == 5
        assert min(heap._data[:5]) == heap._data[0]
        assert heap._data[1] < heap._data[3]
        assert heap._data[1] < heap._data[4]
        heap.push(6, 'y')
        assert heap._data[2] < heap._data[5]
        print(heap)
        heap = PriorityHeap()
        test = heap.top()
        assert test == None

        heap = PriorityHeap()
        heap.push(5, 'c')
        # test = heap.top()
        # assert test == Node(5, 'c')
        heap.push(4, 'y')
        test = heap.top()
        # assert test == Node(4, 'y')
        heap.push(3, 'n')
        test = heap.top()
        # assert test == Node(3, 'n')
        heap.push(2, 'd')
        test = heap.top()
        # assert test == Node(2, 'd')
        heap.push(1, 'e')
        test = heap.top()
        # assert test == Node(1, 'e')

    def test_pop(self):
        '''
        simple pop cases, requires functioning top, push, empty
        '''
        # test 1: tests pop returns the root
        heap = PriorityHeap()
        heap.push(5, 'c')
        heap.push(4, 'y')
        heap.push(3, 'n')
        heap.push(2, 'd')
        heap.push(5, 'y')

        assert heap.pop() == Node(2, 'd')

        # test 2: checks for length and not empty
        heap = PriorityHeap()
        heap.push(4, 'y')
        heap.push(3, 'n')

        assert len(heap._data) == 2
        assert heap.pop() == Node(3, 'n')
        assert len(heap._data) == 1
        assert not heap.empty()

    def test_min_child(self):
        '''
        simple min child test, requires push
        '''
        def check_min(pheap, idx, lhs=None, rhs=None):
            '''
            function helper for validating the min method
            '''
            min_child = lhs if pheap._data[lhs] < pheap._data[rhs] else rhs
            assert min_child == pheap.min_child(idx)
        heap = PriorityHeap()
        for child in ascii_lowercase:
            heap.push(ord(child), child)
        assert len(heap._data) == 26

        check_min(heap, 0, 1, 2)
        check_min(heap, 2, 5, 6)
        check_min(heap, 3, 7, 8)

    def test_change_priority(self):
        '''
        tests change_priority, requires working percolates
        '''
        heap = PriorityHeap()
        heap2 = PriorityHeap()
        i = 1
        while i < 6:
            heap.push(i, 5)
            heap2.push(i, 5)
            i += 1
        heap.change_priority(1, 6)
        assert heap._data == [Node(1, 5), Node(4, 5), Node(3, 5), Node(6, 5), Node(5, 5)]
        heap2.change_priority(1, 0)
        assert heap2._data == [Node(0, 5), Node(1, 5), Node(3, 5), Node(4, 5), Node(5, 5)]

    def test_heap_sort(self):
        """
        heap sort test
        """
        array = [5, 4, 3, 2, 1]
        heap = heap_sort(array)
        assert heap == [1, 2, 3, 4, 5]
        array = [1,9,2,8,3,7,6,4,5]
        heap = heap_sort(array)
        assert heap == [1,2,3,4,5,6,7,8,9]


    def test_merge_lists(self):
        """
        merges two basic lists
        """
        lists = [[1, 2, 5], [3, 5, 4]]
        merged = merge_lists(lists)
        assert merged == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    unittest.main()