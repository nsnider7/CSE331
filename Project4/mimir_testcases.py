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
        # if item to add is None don't increase size
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
        assert queue.data == [10,20,30,None]
        assert queue.size == 3
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.capacity == 4
        # mixture of last two tests
        queue = CircularQueue()
        queue.enqueue(10)
        queue.enqueue(None)
        queue.enqueue(30)
        assert queue.data == [10,30, None,None]
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
        #smaller test
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
        assert queue.data == [1,2,3,4,5, None, None, None, None, None]
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
        queue.dequeue()
        assert queue.data == [None, None, None, None, None, None, None]
        assert queue.size == 0
        assert queue.capacity == 7
        assert queue.head == 0
        assert queue.tail == 0
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
        print(queue.data)
        assert queue.data == [0, 1, 2, None, None, None, None, None, None]
        assert queue.size == 3
        assert queue.capacity == 9
        assert queue.head == 0
        assert queue.tail == 3
        queue.dequeue()
        assert queue.data == [1,2,None,None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2
        # shrink from 9 to 4
        queue = CircularQueue(5)
        queue.enqueue(None)
        queue.enqueue(None)
        queue.enqueue(5)

        print(queue.data)

        assert queue.data == [None, None, 5, None, None]
        assert queue.size == 1
        assert queue.capacity == 5
        assert queue.head == 2
        assert queue.tail == 3
        # queue.dequeue()
        # queue.data = [None, None, None, None, None]
        # assert queue.size == 0
        # assert queue.capacity == 5
        # assert queue.head == 0
        # assert queue.tail == 0

    # def test_threshold_sum(self):
    #     assert threshold_sum([1, 2, 3, 4], 4) == (4, 1)
    #     assert threshold_sum([1, 3, 2, 4], 4) == (4, 2)
    #     assert threshold_sum([1, 2, 3, 4], 8) == (7, 2)


if __name__ == "__main__":
    unittest.main()
