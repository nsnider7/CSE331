"""
PROJECT 2 - Linked List Recursion
Name: Nicholas Snider
PID: A51766181
"""


class LinkedNode:
    # DO NOT MODIFY THIS CLASS #h
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
    Inserts the given value at the back of the list
    :param value: value to insert
    :param node: [LinkedNode] head node
    :return: [LinkedNode] the head node of the LinkedList
    '''
    if node is None:
        return LinkedNode(value)
    elif node.next is not None:
        insert(value, node.next)
    else:
        node.next = LinkedNode(value)
    return node


def to_string(node):
    '''
    Turns the linked into a string
    :param node: [LinkedNode] Head node of single linked list
    :return: [str] String version of the linked list
    '''
    if node is None:
        return ""
    elif node.next is not None:
        return str(node.value) + ', ' + to_string(node.next)
    else:
        return str(node.value)


def remove(value, node):
    '''
    Removes the given value from the list
    :param value: value to remove
    :param node: [LinkedNode] Head node of linked list
    :return: [LinkedNode] Head of list with value removed
    '''
    # if size of list is 1 and node.value != value
    # if list empty
    if node is None:
        return None
    elif node.value != value and node.next is None:
        return node
    # if only element is the one to be removed
    elif node.next is None and node.value == value:
        return None

    # base case
    if node.next is None and value != node.value:
        remove(value, None)
    # if value in the middle or end
    elif node.next.value == value:
        node.next = node.next.next
        remove(value, node)
    # if value is head and only element
    elif node.value == value and node.next is None:
        node.value = None
        node.next = None
        return None
    # removing head
    elif node.value == value:
        node.value = node.next.value
        node.next = node.next.next
        remove(value, node.next)
    # if just a normal middle element
    elif node.next is not None and value != node.value:
        remove(value, node.next)
    if node.value is None:
        return None
    else:
        return node


def remove_all(value, node):
    '''
    Removes all nodes that have a value equal to param value
    :param value: value to remove
    :param node: [LinkedNode] Head node of list
    :return: [LinkedNode] Head node of list with all values removed
    '''
    # if size of list is 1 and node.value != value
    # if list empty
    if node is None:
        return None
    elif node.value != value and node.next is None:
        return node
    # if only element is the one to be removed
    elif node.next is None and node.value == value:
        node.value = None
        node = None
        return None

    # base case
    if node.next is None and value != node.value:
        remove_all(value, None)
    # removing head
    elif node.value == value:
        node.value = node.next.value
        node.next = node.next.next
        remove_all(value, node)
    # if value in the middle or end
    elif node.next.value == value:
        node.next = node.next.next
        remove_all(value, node)
    # if value is head and only element
    elif node.value == value and node.next is None:
        node.value = None
        node.next = None
        return None
    # if just a normal middle element
    elif node.next is not None and value != node.value:
        remove(value, node.next)

    if node.value is None:
        return None
    else:
        return node


def search(value, node):
    '''
    Searches to see if value is in the linked list
    :param value: value to search for
    :param node: [LinkedNode] head node of list
    :return: [boolean] returns True/False depending on if value was found
    '''
    if node is None:
        return False
    if node.value == value:
        return True
    elif node.value != value:
        return search(value, node.next)


def length(node):
    '''
    Finds length of the linked list
    :param node: [LinkedNode] head node of list
    :return: [int] length of list
    '''
    if node is None:
        return 0
    elif node.next is not None:
        return 1 + length(node.next)
    else:
        return 1 + length(node.next)


def sum_list(node):
    '''
    Finds the sum of every element in the list
    :param node: [LinkedNode] head node of list
    :return: [int] sum of elements in list
    '''
    if node is None:
        return 0
    elif node.next is not None:
        return node.value + sum_list(node.next)
    else:
        return node.value + sum_list(node.next)


def count(value, node):
    '''
    Determines how many times value appears in list
    :param value: value to count
    :param node: [LinkedNode] head node of list
    :return: [int] count of how many times value was in list
    '''
    if node is None:
        return 0
    elif node.value == value:
        return 1 + count(value, node.next)
    else:
        return count(value, node.next)


def reverse(node):
    '''
    Completely reverses the list
    :param node: [LinkedNode] head node of list
    :return: [LinkedNode] new head node of reversed list
    '''
    # if list is empty return None
    if node is None:
        return None

    # last node has to get returned to stack
    if node.next is None:
        return node
    # call until last node is return and assign to head_node
    new_head = reverse(node.next)
    node.next.next = node
    node.next = None
    return new_head


def remove_fake_requests(head):
    '''
    Removes all duplicates from sorted list
    :param head: [LinkedNode] head node of list
    :return: [LinkedNode] head node of list with duplicate values removed
    '''
    # if list is empty
    if head is None:
        return None
    # base case
    if head.next is None:
        return head

    # recursion
    if head.next.next is not None:
        if head.next.next.value == head.next.value:
            temp_head = head.next
            # loop on duplcate values
            while head.next.value == temp_head.value:
                # if two ele in list and both need removal
                if head.next.next is None and head.value == head.next.value:
                    head.value = None
                    head.next.value = None
                    return None
                elif head.next.next is None:
                    head.next = None
                    return head
                # if elements in middle of list need removal
                elif head.next.value == head.value and head.value != head.next.next.value:
                    head.next = head.next.next
                    head.value = head.next.value
                    head.next = head.next.next
                # if in middle of list just remove
                else:
                    head.next = head.next.next
                # check if ele is last in list
                if head.next is None:
                    return head
        # if only two elements in list need removal
        elif head.value == head.next.value:
            head.next = head.next.next
            head.value = head.next.value
            head.next = head.next.next
        # if goes from deleting to more duplcates, it must recur of same element
        if head.value == head.next.value:
            remove_fake_requests(head)
        # if not duplicates then go to next ele
        else:
            remove_fake_requests(head.next)
    elif head.value == head.next.value and head.next.next is None:
        head.next = head.next.next
        head.value = None
    else:
        remove_fake_requests(head.next)
    # if only None in list, return None
    if head is None:
        return None
    # if actual value was assigned None, return None
    elif head.value is None:
        return None
    # otherwise return head
    else:
        return head
