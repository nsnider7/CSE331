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
        sum_total = 0
        node = self.head
        while node is not self.tail:
            sum_total += self.data[node]
            node+=1
        return sum_total

    def head_element(self):
        return self.data[self.head]

    def tail_element(self):
        if self.tail == 0:
            return self.data[self.tail]
        else:
            return self.data[self.tail - 1]

    def enqueue(self, val):
        # if val is None:
        #     return None
        # gets index of next open index
        emptyIndex = (self.head + self.size) % self.capacity
        self.data[emptyIndex] = val
        if val is not None:
            self.size += 1
        self.tail = emptyIndex + 1
        # if queue needs more size
        if self.size == self.capacity:
            self.grow()
        return None

    def dequeue(self):
        # if list is empty
        if self.size is 0:
            return None
        return_val = self.data[self.head]
        self.data[self.head] = None
        # if only one element set both head and tail to 0
        if self.size is 1:
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head + 1) % self.capacity
        self.size -= 1
        if (self.capacity // 2 >= 4) and (self.size <= (self.capacity * 0.25)):
            self.shrink()
        return return_val


    def grow(self):
        # gets the index of start of new list
        next_index = self.capacity
        self.capacity = self.capacity * 2
        while next_index != self.capacity:
            self.data.append(None)
            next_index+=1


    def shrink(self):
        # calculates the number of "None"s to delete
        delete_num = self.head - 0
        # capacity never goes lower than 2
        if self.capacity < 8:
            self.capacity = 4
        else:
            self.capacity = self.capacity // 2
        # delete all the "None"s in front
        if delete_num is not 0:
            while delete_num != 0:
                self.data.pop(delete_num - 1)
                delete_num-=1
        self.data = self.data[0:self.capacity]
        self.head = 0
        self.tail = self.data.index(None)



def threshold_sum(nums, threshold):
    pass
