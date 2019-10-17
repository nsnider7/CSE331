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
        """
        checks to see if queue is empty
        :return: [bool] True if empty, false otherwise
        """
        if self.head is 0 and self.tail is 0:
            return True
        else:
            return False

    def __len__(self):
        """
        gets length of queue
        :return: [int] returns the size of queue
        """
        return self.size

    def get_total(self):
        """
        gets the sum of every element in the queue
        :return: [int] sum of every element
        """
        return self.total

    def head_element(self):
        """
        gets the head element of the queue
        :return: [int] the value of head
        """
        return self.data[self.head]

    def tail_element(self):
        """
        gets the value of the tail
        :return: [int] value of tail
        """
        if self.tail == 0:
            return self.data[self.tail]
        else:
            return self.data[self.tail - 1]

    def enqueue(self, val):
        """
        adds an element to the back of the queue
        :param val: [int] value to add to queue
        :return: None
        """
        if val is None:
            return None
        # add to total
        self.total += val
        # gets index of next open index
        emptyIndex = (self.head + self.size) % self.capacity
        self.data[emptyIndex] = val
        self.size += 1
        self.tail = emptyIndex + 1
        # if queue needs more size
        if self.size == self.capacity:
            self.grow()
        return None

    def dequeue(self):
        """
        removes the first element in the queue and returns it
        :return: [int] head of the queue
        """
        # if list is empty
        if self.size is 0:
            return None
        # functions as pop method, so return the front index
        return_val = self.data[self.head]
        # subtract from total
        self.total -= return_val
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
        """
        if capacity is reached, double the size of the queue
        :return: No return, queue is doubled in capacity
        """
        # gets the index of start of new list
        next_index = self.capacity
        self.capacity = self.capacity * 2
        while next_index != self.capacity:
            self.data.append(None)
            next_index += 1

    def shrink(self):
        """
        if size is 1/4 or less of capcity shrink the size by half
        :return:no return, shrinks the size in half but no less than 4
        """
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
                delete_num -= 1
        # if capacity isn't full
        if len(self.data) < self.capacity:
            while len(self.data) < self.capacity:
                self.data.append(None)
                if len(self.data) == self.capacity:
                    break
        # if size of data has more elements than capacity
        elif len(self.data) > self.capacity:
            while len(self.data) > self.capacity:
                self.data.remove(None)
                if len(self.data) == self.capacity:
                    break
        self.head = 0
        self.tail = self.data.index(None)


def threshold_sum(nums, threshold):  # [1,2,3,None,None]
    """
    find the sequence of consecutive numbers with the highest possible
    sum that is less than or equal to the threshold
    :param nums: [list] 
    :param threshold:
    :return: [tuple] (sum of elements in sequence, length of sequence)
    """
    if threshold < 0:
        return 0, 0
    queue = CircularQueue()
    largest_sum = 0
    largest_seq = 0
    for i in nums:
        if queue.get_total() <= threshold:
            queue.enqueue(i)
        while queue.get_total() > threshold:
            queue.dequeue()
        if largest_sum < queue.get_total() <= threshold:
            largest_sum = queue.get_total()
            largest_seq = len(queue)
        if largest_sum == queue.get_total():
            if largest_seq < len(queue):
                largest_seq = len(queue)

    if largest_sum == 0:
        if sum(nums) == 0:
            return 0, len(nums)
        else:
            return 0, len(queue)
    else:
        return largest_sum, largest_seq
