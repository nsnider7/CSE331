"""
CSE 331 Project 1
Author: Nicholas Snider
"""


class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.__next = next
        self.__prev = prev
        self.__value = value

    def __repr__(self):
        return str(self.__value)

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        """
        Getter for value
        :return: the value of the node
        """
        return self.__value

    def set_value(self, value):
        """
        Setter for value
        :param value: the value to set
        """
        self.__value = value

    def get_next(self):
        """
        Getter for next node
        :return: the next node
        """
        return self.__next

    def set_next(self, node):
        """
        Setter for next node
        :param node: the node to set
        """
        self.__next = node

    def get_previous(self):
        """
        Getter for previous node
        :return: the previous node
        """
        return self.__prev

    def set_previous(self, node):
        """
        Setter for previous node
        :param node: the node to set
        """
        self.__prev = node


class DLL:
    """
    Class representing a doubly linked list.
    """

    def __init__(self):
        """
        Constructor
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        @attribute size: the size of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    def __str__(self):
        """
        iterates through the linked list to generate a string representation
        :return: string representation of the linked list
        """
        res = ""
        node = self.head
        while node:
            res += str(node)
            if node.get_next():
                res += " "
            node = node.get_next()
        return res

    ######### MODIFY BELOW ##########

    def get_size(self):
        """
        Gives the user the size of their linked list
        :return: [int] the size of the linked list
        """
        return int(self.size)

    def is_empty(self):
        """
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        if self.size == 0:
            return True
        else:
            return False

    def insert_front(self, value):
        """
        Inserts a value into the front of the list
        :param value: the value to insert
        """
        newNode = DLLNode(value)
        lst = DLL()
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.head.set_previous(newNode)
            newNode.set_next(self.head)
            self.head = newNode
            self.size += 1

    def insert_back(self, value):
        """
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        newNode = DLLNode(value)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.set_next(newNode)
            newNode.set_previous(self.tail)
            self.tail = newNode
            self.size += 1

    def delete_front(self):
        """
        Deletes the front node of the list
        """
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        if self.size != 0:
            sucNode = self.head.get_next()
            self.head = sucNode
            self.head.set_previous(None)
            self.size -= 1

    def delete_back(self):
        """
        Deletes the back node of the list
        """
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        if self.size != 0:
            prevNode = self.tail.get_previous()
            self.tail = prevNode
            self.tail.set_next(None)
            self.size -= 1

    def delete_value(self, value):
        """
        Deletes the first instance of the value in the list.
        :param value: The value to remove
        """
        # Define the node, prevNode, sucNode
        if self.size > 0:
            first_node = self.find_first(value)  # find the value
            if first_node != None:
                if first_node == self.head:
                    prevNode = None
                    sucNode = first_node.get_next()
                elif first_node == self.tail:
                    prevNode = first_node.get_previous()
                    sucNode = None
                else:
                    prevNode = first_node.get_previous()
                    sucNode = first_node.get_next()
                # Now Delete
                if first_node == self.head:
                    self.head = sucNode
                if first_node == self.tail:
                    self.tail = prevNode
                if sucNode is not None:
                    sucNode.set_previous(prevNode)
                if prevNode is not None:
                    prevNode.set_next(sucNode)
        self.size -= 1

    def delete_all(self, value):
        """
        Deletes all instances of the value in the list
        :param value: the value to remove
        """
        count = 0
        first_node = self.find_first(value)
        if first_node != None:
            while first_node != None:
                count += 1
                # Define the node, prevNode, sucNode
                first_node = self.find_first(value)
                if first_node == self.head:
                    prevNode = None
                    sucNode = first_node.get_next()
                elif first_node == self.tail:
                    prevNode = first_node.get_previous()
                    sucNode = None
                else:
                    prevNode = first_node.get_previous()
                    sucNode = first_node.get_next()
                # Now Delete
                if first_node == self.head:
                    self.head = sucNode
                if first_node == self.tail:
                    self.tail = prevNode
                if sucNode is not None:
                    sucNode.set_previous(prevNode)
                if prevNode is not None:
                    prevNode.set_next(sucNode)
                first_node = self.find_first(value)
        self.size = self.size - count

    def find_first(self, value):
        """
        Finds the first instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the first node containing the value
        """
        if self.head is not None:
            node = self.head
            sucNode = self.head.get_next()
            prevNode = None
            while node is not None:
                if value == node.get_value():
                    return node
                prevNode = node
                if node.get_next() == None:
                    node = None
                    sucNode = None
                else:
                    node = node.get_next()
                if sucNode is not None:
                    if node.get_next() == None:
                        sucNode = None
                    else:
                        sucNode = node.get_next()
        else:
            return None

    def find_last(self, value):
        """
        Finds the last instance of the value in the list
        :param value: the value to find
        :return: [DLLNode] the last node containing the value
        """
        if self.tail is not None:
            node = self.tail
            sucNode = self.head.get_previous()
            prevNode = None
            while node is not None:
                if value == node.get_value():
                    return node
                prevNode = node
                if node.get_previous() == None:
                    node = None
                    sucNode = None
                else:
                    node = node.get_previous()
                if sucNode is not None:
                    if node.get_previous() == None:
                        sucNode = None
                    else:
                        sucNode = node.get_previous()
        else:
            return None

    def find_all(self, value):
        """
        Finds all of the instances of the value in the list
        :param value: the value to find
        :return: [List] a list of the nodes containing the value
        """
        node_list = []
        if self.head is not None:
            node = self.head
            sucNode = self.head.get_next()
            prevNode = None
            while node is not None:
                if value == node.get_value():
                    node_list.append(node)
                prevNode = node
                if node.get_next() == None:
                    node = None
                    sucNode = None
                else:
                    node = node.get_next()
                if sucNode is not None:
                    if node.get_next() == None:
                        sucNode = None
                    else:
                        sucNode = node.get_next()
            if len(node_list) == 0:
                return []
            else:
                return node_list
        else:
            return []

    def count(self, value):
        """
        Finds the count of times that the value occurs in the list
        :param value: the value to count
        :return: [int] the count of nodes that contain the given value
        """
        node_list = self.find_all(value)
        return len(node_list)

    def sum(self):
        """
        Finds the sum of all nodes in the list
        :param start: the indicator of the contents of the list
        :return: the sum of all items in the list
        """
        try:
            if self.head is not None:
                curNode = self.head
                sum_list = []
<<<<<<< HEAD
                new_val = 0
=======
                new_sum = 0
>>>>>>> bb6ada78a0ce2e89df38ce8255c347aa7756f4ad
                while curNode is not None:
                    sum_list.append(curNode.get_value())
                    if curNode.get_next() == None:
                        curNode = None
                    else:
                        curNode = curNode.get_next()
<<<<<<< HEAD
                for i in sum_list:
                    new_val += i
                return new_val
                # print(type(sum_list[0]))
                # if type(sum_list[0]) != int or len(sum_list) == 0 or type(sum_list[0]) != float:
                #     return None
                # else:
                #     return sum(sum_list)
=======
                return_val = type(sum_list[0])()
                for i in sum_list:
                    return_val += i
                return return_val
>>>>>>> bb6ada78a0ce2e89df38ce8255c347aa7756f4a
            else:
                return None
        except TypeError:
            return None


def remove_middle(LL):
    """
    Removes the middle of a given doubly linked list.
    :param DLL: The doubly linked list that must be modified
    :return: The updated linked list
    """
    if LL.head is not None:
        # if odd
        if (LL.get_size() % 2) == 1:
            if LL.get_size() == 1:
                LL.delete_front()
                return LL
            else:
                mid_point = int((LL.get_size() / 2) + 0.5)
                curNode = LL.head
                count = 1
                while curNode is not None:
                    if count == mid_point:
                        LL.delete_value(curNode.get_value())
                        return LL
                    if curNode.get_next() == None:
                        curNode = None
                    else:
                        curNode = curNode.get_next()
                    count += 1
        # if even
        else:
            if LL.get_size() == 2:
                LL.delete_front()
                LL.delete_front()
                return LL
            else:
                mid_point = LL.get_size() / 2
                curNode = LL.head
                count = 1
                while curNode is not None:
                    if count == mid_point:
                        next_node = curNode.get_next()A
                        LL.delete_value(curNode.get_value())
                        LL.delete_value(next_node.get_value())
                        return LL
                    if curNode.get_next() == None:
                        curNode = None
                    else:
                        curNode = curNode.get_next()
                    count += 1
    else:
        return LL
