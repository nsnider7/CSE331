"""
Project 4- Solution
"""


class CircularQueue:
    """
    Circular Queue Class.
    """

    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.total = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size and self.total == other.get_total()

    def __str__(self):
        """
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i) % self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    # -----------MODIFY BELOW--------------

    def is_empty(self):
        if self.head is 0 and self.tail is 0:
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def get_total(self):
        pass

    def head_element(self):
        return self.data[self.head]

    def tail_element(self):
        if self.tail == 0:
            return self.data[self.tail]
        else:
            return self.data[self.tail - 1]

    def enqueue(self, val):
        if self.size + 1 >= self.capacity:
            self.grow()
        queueBack = (self.head + self.size) % self.capacity
        self.data[queueBack] = val
        self.size += 1
        self.tail = queueBack + 1





    def dequeue(self):
        pass

    def grow(self):
        self.capacity = self.capacity * 2

    def shrink(self):
        pass


def threshold_sum(nums, threshold):
    pass
