"""
PROJECT 2 - Linked List Recursion
Name: Nicholas Snider
PID: A51766181
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next'

    def __init__(self, value, next=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next: pointer to the next node in the LinkedList, default is None
        """
        self.value = value  # element at the node
        self.next = next  # reference to next node in the LinkedList

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


# IMPLEMENT THESE FUNCTIONS - DO NOT MODIFY FUNCTION SIGNATURES #


def insert(value, node=None):
    '''
    :param value: value to insert
    :param node: head node
    :return: the head node of the LinkedList
    '''
    if node == None:
        return LinkedNode(value)
    elif node.next != None:
        insert(value, node.next)
    else:
        node.next = LinkedNode(value)
    return node


def to_string(node):



def remove(value, node):
    pass


def remove_all(value, node):
    pass


def search(value, node):
    pass


def length(node):
    pass


def sum_list(node):
    pass


def count(value, node):
    pass


def reverse(node):
    pass


def remove_fake_requests(head):
    pass
