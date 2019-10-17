import unittest
from CircularQueue import CircularQueue, threshold_sum


class TestProject1(unittest.TestCase):

    def test_accessors(self):
        queue = CircularQueue()
        #
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        # print(queue)
        assert not queue.is_empty()
        # print(len(queue))
        assert len(queue) == 4
        assert queue.get_total() == 10
        assert queue.head_element() == 1
        assert queue.tail_element() == 4

    #
    def test_enqueue(self):
        # if item to add is None don't increase size`
        queue = CircularQueue()
        queue.enqueue(None)
        assert queue.data == [None, None, None, None]
        assert queue.size == 0
        assert queue.head == 0
        assert queue.tail == 0
        assert queue.capacity == 4
        # Normal enqueue
        queue = CircularQueue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        assert queue.data == [10, 20, 30, None]
        assert queue.size == 3
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.capacity == 4
        # mixture of last two tests
        queue = CircularQueue()
        queue.enqueue(10)
        queue.enqueue(None)
        queue.enqueue(30)
        assert queue.data == [10, 30, None, None]
        assert queue.size == 2
        assert queue.head == 0
        assert queue.tail == 2
        assert queue.capacity == 4
        # simple grow test
        queue = CircularQueue(5)
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)
        queue.enqueue(40)
        queue.enqueue(50)

        assert queue.data == [10, 20, 30, 40, 50, None, None, None, None, None]
        assert queue.size == 5
        assert queue.head == 0
        assert queue.tail == 5
        assert queue.capacity == 10
        #

    def test_dequeue(self):
        # mimir test copied
        queue = CircularQueue(6)
        for i in range(0, 5):
            queue.enqueue(i * 5)
        assert queue.data == [0, 5, 10, 15, 20, None]
        assert queue.size == 5
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 5
        queue.dequeue()
        assert queue.data == [None, 5, 10, 15, 20, None]
        assert queue.size == 4
        assert queue.capacity == 6
        assert queue.head == 1
        assert queue.tail == 5
        # smaller test
        queue = CircularQueue(4)
        for i in range(0, 3):
            queue.enqueue(i * 5)
        assert queue.data == [0, 5, 10, None]
        assert queue.size == 3
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 3
        queue.dequeue()
        assert queue.data == [None, 5, 10, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 1
        assert queue.tail == 3
        # make sure capacity is never < 4
        queue = CircularQueue(6)
        queue.enqueue(5)
        assert queue.data == [5, None, None, None, None, None]
        assert queue.size == 1
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 1
        queue.dequeue()
        assert queue.data == [None, None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 0
        # normal shrinkage
        queue = CircularQueue(10)
        queue.enqueue(5)
        queue.enqueue(6)
        assert queue.data == [5, 6, None, None, None, None, None, None, None, None]
        assert queue.size == 2
        assert queue.capacity == 10
        assert queue.head == 0
        assert queue.tail == 2
        queue.dequeue()
        assert queue.data == [6, None, None, None, None]
        assert queue.size == 1
        assert queue.capacity == 5
        assert queue.head == 0
        assert queue.tail == 1
        queue.dequeue()
        assert queue.data == [None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 5
        assert queue.head == 0
        assert queue.tail == 0
        # make sure it doesn't shrink
        queue = CircularQueue(10)
        for i in range(1, 6):
            queue.enqueue(i)
        assert queue.data == [1, 2, 3, 4, 5, None, None, None, None, None]
        assert queue.size == 5
        assert queue.capacity == 10
        assert queue.head == 0
        assert queue.tail == 5
        queue.dequeue()
        queue.dequeue()
        assert queue.data == [None, None, 3, 4, 5, None, None, None, None, None]
        assert queue.size == 3
        assert queue.capacity == 10
        assert queue.head == 2
        assert queue.tail == 5

    def test_grow(self):
        # mimir test
        queue = CircularQueue(5)
        for i in range(0, 8):
            queue.enqueue(i * 2)
        assert queue.data == [0, 2, 4, 6, 8, 10, 12, 14, None, None]
        assert queue.capacity == 10
        assert queue.size == 8
        assert queue.head == 0
        assert queue.tail == 8
        # small grow
        queue = CircularQueue(5)
        for i in range(0, 8):
            queue.enqueue(i * 2)
        assert queue.data == [0, 2, 4, 6, 8, 10, 12, 14, None, None]
        assert queue.capacity == 10
        assert queue.size == 8
        assert queue.head == 0
        assert queue.tail == 8

    #
    def test_shrink(self):
        queue = CircularQueue()

        for i in range(0, 5):
            queue.enqueue(i)
        assert queue.data == [0, 1, 2, 3, 4, None, None, None]
        assert queue.size == 5
        assert queue.capacity == 8
        assert queue.head == 0
        assert queue.tail == 5
        for _ in range(3):
            queue.dequeue()
        assert queue.data == [3, 4, None, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2
        # empty list that shouldnt shrink
        queue = CircularQueue(7)
        assert queue.data == [None, None, None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 7
        assert queue.head == 0
        assert queue.tail == 0
        queue.dequeue()
        test = queue.dequeue()
        assert test == None
        assert queue.data == [None, None, None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 7
        assert queue.head == 0
        assert queue.tail == 0
        assert queue.total == 0
        # empty list that has the ability to shrink but shouldn't
        queue = CircularQueue(8)
        assert queue.data == [None, None, None, None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 8
        assert queue.head == 0
        assert queue.tail == 0
        test = queue.dequeue()
        queue.dequeue()
        assert test == None
        assert queue.data == [None, None, None, None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 8
        assert queue.head == 0
        assert queue.tail == 0
        # shrink from 9 to 4
        queue = CircularQueue(9)
        for i in range(0, 3):
            queue.enqueue(i)
        assert queue.data == [0, 1, 2, None, None, None, None, None, None]
        assert queue.size == 3
        assert queue.capacity == 9
        assert queue.head == 0
        assert queue.tail == 3
        queue.dequeue()
        assert queue.data == [1, 2, None, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2
        assert queue.total == 3
        # test #3 from piazza student
        queue = CircularQueue(5)
        queue.enqueue(5)
        queue.enqueue(5)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        # [None. None, 5, None, None]
        queue.dequeue()
        assert queue.data == [None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 5
        assert queue.head == 0
        assert queue.tail == 0
        assert queue.total == 0
        # test #1 from piazza student
        queue = CircularQueue(13)
        for i in range(0, 7):
            queue.enqueue(i)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        # [None, None, None, 3, 4, 5, 6, None, None, None, None, None, None]
        assert queue.data == [None, None, None, 3, 4, 5, 6, None, None, None, None, None, None]
        assert queue.size == 4
        assert queue.capacity == 13
        assert queue.head == 3
        assert queue.tail == 7
        assert queue.total == 18
        queue.dequeue()
        assert queue.data == [4, 5, 6, None, None, None]
        assert queue.size == 3
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.total == 15
        queue.dequeue()
        assert queue.data == [None, 5, 6, None, None, None]
        assert queue.size == 2
        assert queue.capacity == 6
        assert queue.head == 1
        assert queue.tail == 3
        assert queue.total == 11
        queue.dequeue()
        assert queue.data == [None, None, 6, None, None, None]
        assert queue.size == 1
        assert queue.capacity == 6
        assert queue.head == 2
        assert queue.tail == 3
        assert queue.total == 6
        # one item in large list, dequeue and then shrink
        queue = CircularQueue(8)
        queue.enqueue(1)
        assert queue.data == [1, None, None, None, None, None, None, None]
        assert queue.size == 1
        assert queue.capacity == 8
        assert queue.head == 0
        assert queue.tail == 1
        test = queue.dequeue()
        assert test == 1
        assert queue.data == [None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 0
        assert queue.total == 0
        # possibility of adding None's to end
        queue = CircularQueue(10)
        for i in range(0, 9):
            queue.enqueue(i)
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

    def test_threshold_sum(self):
        assert threshold_sum([1, 2, 3, 4], 4) == (4, 1)  # [4, 1]
        assert threshold_sum([1, 3, 2, 4], 4) == (4, 2)  # [1, 3]
        assert threshold_sum([1, 2, 3, 4], 8) == (7, 2)  # [3, 4]

        #
        # assert threshold_sum([1, 2, 3, 4], 4) == (4, 1)
        # assert threshold_sum([1, 3, 2, 4], 4) == (4, 2)
        # assert threshold_sum([1, 2, 3, 4], 8) == (7, 2)
        # assert threshold_sum([2], 4) == (2, 1)
        # print("Jeez this kid next to me smells like a cheese puff!")
        # assert threshold_sum([1, 2, 7, 3], 4) == (3, 2)
        # assert threshold_sum([1, 2, 2, 3], 6) == (5, 3)
        # assert threshold_sum([4, 5, 6, 7], 3) == (0, 0)
        # assert threshold_sum([2, 2, 4, 1, 1], 4) == (4, 2)
        # assert threshold_sum([2, 3, 4, 5], 2) == (2, 1)
        # assert threshold_sum([1, 2, 4, 3], 7) == (7, 3)
        # assert threshold_sum([], 1) == (0, 0)
        # assert threshold_sum([1, 2, 7, 3, 324, 54, 6, 7, 87, 8, 8, 9, 9, 9, 9, 99, 9, 9], 40) == (36, 4)
        # assert threshold_sum([8, 7, 6, 5], 4) == (0, 0)
        # assert threshold_sum([1, 4, 2, 4], 3) == (2, 1)
        # assert threshold_sum([2, 2, 4, 1, 1], 4) == (4, 2)
        # assert threshold_sum([1, 3, 2, 4], 4) == (4, 2)
        # assert threshold_sum([1, 2, 3, 4], 8) == (7, 2)
        # assert threshold_sum([2, 2, 4, 1, 1], 4) == (4, 2)
        # assert threshold_sum([1, 2, 2, 3], 6) == (5, 3)
        # assert threshold_sum([1, 2, 4, 3], -7) == (0, 0)
        # assert threshold_sum([], 0) == (0, 0)
        # assert threshold_sum([1, 2, 7, 3, 324, 54, 6, 7, 87, 8, 8, 9, 9, 9, 9, 99, 9, 9], 40) == (36, 4)
        # assert threshold_sum([8, 7, 6, 5], 4) == (0, 0)
        # assert threshold_sum([1], 4) == (1, 1)
        # assert threshold_sum([8, 7, 6, 5, 8, 9, 5, 3, 6, 8, 6], 4) == (3, 1)
        # assert threshold_sum([4, 1, 2, 1], 4) == (4, 3)
        # assert threshold_sum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0) == (0, 12)
        # assert threshold_sum([1, 1, 2, 1, 1, 2], 4) == (4, 3)
        # assert threshold_sum([1, 2, 2, 3, 4], 6) == (5, 3)
        # assert threshold_sum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2) == (0, 12)
        # assert threshold_sum([1, 0, 2, 4], 3) == (3, 3)
        # assert threshold_sum([2, 0, 0, 1, 0, 2, 4], 3) == (3, 5)
        # assert threshold_sum([2, 0, 0, 0, 1, 0, 0, 2, 4], 3) == (3, 7)
        #
        #
        # assert threshold_sum([4,3,2,1], 4) == (4, 1)
        # assert threshold_sum([4,2,3,1], 4) == (4, 1)
        # assert threshold_sum([1, 2, 3, 4], 8) == (7, 2)
        # assert threshold_sum([2], 4) == (2, 1)
        # assert threshold_sum([1, 2, 7, 3], 4) == (3, 2)
        # assert threshold_sum([1, 2, 2, 3], 6) == (5, 3)
        # assert threshold_sum([4, 5, 6, 7], 3) == (0, 0)
        # assert threshold_sum([2, 2, 4, 1, 1], 4) == (4, 2)
        # assert threshold_sum([2,3, 4,5], 2) == (2, 1)
        # assert threshold_sum([1, 2, 4, 3], 7) == (7, 3)
        # assert threshold_sum([], 1) == (0, 0)
        # assert threshold_sum([1, 2, 7, 3, 324, 54, 6, 7, 87, 8, 8, 9, 9, 9, 9, 99, 9, 9], 40) == (36, 4)
        # assert threshold_sum([8, 7, 6, 5], 4) == (0, 0)
        # assert threshold_sum([1, 4, 2, 4], 3) == (2, 1)


if __name__ == "__main__":
    unittest.main()
