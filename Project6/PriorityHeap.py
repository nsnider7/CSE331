class Node:
    """
    Node definition should not be changed in any way
    """
    __slots__ = ['_key', '_value']

    def __init__(self, k, v):
        """
        Initializes node
        :param k: key to be stored in the node
        :param v: value to be stored in the node
        """
        self._key = k
        self._value = v

    def __lt__(self, other):
        """
        Less than comparator
        :param other: second node to be compared to
        :return: True if the node is less than other, False if otherwise
        """
        return self._key < other.get_key() or (self._key == other.get_key() and self._value < other.get_value())

    def __gt__(self, other):
        """
        Greater than comparator
        :param other: second node to be compared to
        :return: True if the node is greater than other, False if otherwise
        """
        return self._key > other.get_key() or (self._key == other.get_key() and self._value > other.get_value())

    def __eq__(self, other):
        """
        Equality comparator
        :param other: second node to be compared to
        :return: True if the nodes are equal, False if otherwise
        """
        return self._key == other.get_key() and self._value == other.get_value()

    def __str__(self):
        """
        Converts node to a string
        :return: string representation of node
        """
        return '({0},{1})'.format(self._key, self._value)

    __repr__ = __str__

    def get_key(self):
        """
        Key getter function
        :return: key value of the node
        """
        return self._key

    def set_key(self, new_key):
        """
        Key setter function
        :param new_key: the value the key is to be changed to
        """
        self._key = new_key

    def get_value(self):
        """
        Value getter function
        :return: value of the node
        """
        return self._value


class PriorityHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = '_data'

    def __init__(self):
        """
        Initializes the priority heap
        """
        self._data = []

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self._data)

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self._data)

    __repr__ = __str__

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def parent(self, j):
        """
        Finds the parent index of the node that is passed it
        :param j: [int] index of node to find parent of
        :return: [int] parent index
        """
        return (j - 1) // 2

    def left(self, j):
        """
        Finds the index of the node's left child
        :param j: [int] index of node
        :return: [int] index of left child
        """
        return 2 * j + 1

    def right(self, j):
        """
        Finds the index of the node's right child
        :param j: [int] index of node
        :return: [int] index of right child
        """
        return 2 * j + 2

    def has_left(self, j):
        """
        Determines if node has a left child
        :param j: [int] index of node
        :return: [bool] if child exists return True, if not return False
        """
        # determine if index is beyond list
        return self.left(j) < len(self._data)

    def has_right(self, j):
        """
        Determines if node has a right child
        :param j: [int] index of node
        :return: [bool] if child exists return True, if not return False
        """
        # determine if index is beyond list
        return self.right(j) < len(self._data)  # index beyond end of list?

    def swap(self, i, j):
        """
        Swap the elements at indices i and j of array
        :param i: [int] index of first node to swap
        :param j: [int] index of second node to swap
        :return: no return, but nodes have been swapped in array
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def empty(self):
        """
        determines if heap is empty
        :return: [bool] True if empty, False otherwise
        """
        if len(self._data) == 0:
            return True
        else:
            return False

    def top(self):
        """
        Returns the root value
        :return: [type of node value] Node's value, [None] if heap is empty
        """
        if not self.empty():
            return self._data[0].get_value()
        else:
            return None

    def push(self, key, val):
        """
        Adds a node to the heap
        :param key: [anything comparable] priority of the node
        :param val: value of the node
        :return: no return, heap contains new element
        """
        # add element and then place in correct position using percolate
        self._data.append(Node(key, val))
        self.percolate_up(len(self._data) - 1)

    def pop(self):
        """
        Removes and returns the smallest element of the priority queue
        :return: [Node] smallest node ih the priority queue
        """
        if self.empty():
            return None
        # swap with last element to pop off self._data
        self.swap(0, len(self._data) - 1)
        min_item = self._data.pop()
        # find position of new root
        self.percolate_down(0)
        return min_item

    def min_child(self, index):
        """
        Finds the smallest child of node at index given
        :param index: [int] index of Node to find min child of
        :return: [int] index of smallest child, [None] if no children
        """
        # if no children
        if self.has_left(index) is False and self.has_right(index) is False:
            return None
        elif self.has_left(index) is False:  # if only right child
            return self.right(index)
        elif self.has_right(index) is False:  # if only left child
            return self.left(index)
        elif self._data[self.right(index)] < self._data[self.left(index)]:
            return self.right(index)
        else:
            return self.left(index)

    def percolate_up(self, index):
        """
        Percolates up min heap and finds appropriate spot for the Node
        :param index: [int] index of Node to percolate up
        :return: no return, Node is in correct position
        """
        parent = self.parent(index)
        # determine if index is in range
        if index > 0 and self._data[index] < self._data[parent]:
            self.swap(index, parent)  # swap with parent
            self.percolate_up(parent)  # recur at position of parent

    def percolate_down(self, index):
        """
        Percolates down min heap and finds appropriate spot for the Node
        :param index: [int] index of Node to percolate down
        :return: no return, Node is in correct position
        """
        small_child = self.min_child(index)
        # if smallest child exists, see if percolation needs to happen
        if small_child is not None:
            if self._data[small_child] < self._data[index]:
                self.swap(index, small_child)
                self.percolate_down(small_child)  # recur at position of small child

    def change_priority(self, index, new_key):
        """
        Changes the priority of the node at the index passed in
        :param index: [int] index of node to change
        :param new_key: [any type that is comparable] key to replace node with
        :return: [None] if index was out of range, otherwise node is changed with no return
        """
        # if index out of range
        if index > len(self._data) - 1:
            return None
        # change the priority
        else:
            self._data[index].set_key(new_key)
            # check both percolations
            self.percolate_up(index)
            self.percolate_down(index)


def heap_sort(array):
    """
    Sorts a list using a min heap
    :param array: [list] list containing ints to sort
    :return: [list] sorted list of ints
    """
    # push original list to heap
    heap = PriorityHeap()
    for i in array:
        heap.push(i, 'x')  # random value
    n = len(array)
    temp = []
    # pop off top element and append to temp list to return
    for j in range(n):
        temp.append(heap.pop().get_key())
    return temp


def merge_lists(array_list):
    """
    Takes in a list of lists and merges them into one sorted list
    :param array_list: [list] List containing lists to merge together and sort
    :return: [list] sorted list
    """
    heap = PriorityHeap()
    for lst in array_list:
        if len(lst) != 0:
            # have list be key and also value for access
            heap.push(heap_sort(lst), heap_sort(lst))
    return_lst = []
    # create variable for duplicates
    prev = 'x'
    # while heap is not empty
    while heap.empty() is False:
        # since min heap empty lists can be min, pop if they are
        if len(heap.top()) == 0:
            heap.pop()
            continue
        # get first element in root list, this is smallest element
        temp_val = (heap.top()).pop(0)
        # if value isn't already in return_lst
        if prev != temp_val:
            return_lst.append(temp_val)
        prev = temp_val
        # change the key to the value with popped value
        heap.change_priority(0, heap.top())
    return return_lst
