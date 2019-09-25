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
    '''
    :param node: Head node of single linked list
    :return: String version of the linked list
    '''
    if node == None:
        return ""
    elif node.next != None:
        return str(node.value) + ', ' + to_string(node.next)
    else:
        return str(node.value)

def remove(value, node):
    #if size of list is 1 and node.value != value
    # if list empty
    if node == None:
        return None
    elif node.value != value and node.next == None:
        return node
    # if only element is the one to be removed
    elif node.next == None and node.value == value:
        return None

    # base case
    if node.next == None and value != node.value:
        remove(value, None)
    # if value in the middle or end
    elif node.next.value == value:
        node.next = node.next.next
        remove(value, node)
    # if value is head and only element
    elif node.value == value and node.next == None:
        node.value = None
        node.next = None
        return None
    # removing head
    elif node.value == value:
        node.value = node.next.value
        node.next = node.next.next
        remove(value, node.next)
    # if just a normal middle element
    elif node.next != None and value != node.value:
        remove(value, node.next)
    if node.value == None:
        return None
    else:
        return node

def remove_all(value, node):
    #if size of list is 1 and node.value != value
    # if list empty
    if node == None:
        return None
    elif node.value != value and node.next == None:
        return node
    # if only element is the one to be removed
    elif node.next == None and node.value == value:
        node.value = None
        node = None
        return None

    # base case
    if node.next == None and value != node.value:
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
    elif node.value == value and node.next == None:
        node.value = None
        node.next = None
        return None
    # if just a normal middle element
    elif node.next != None and value != node.value:
        remove(value, node.next)

    if node.value == None:
        return None
    else:
        return node

def search(value, node):
    if node == None:
        return False
    if node.value == value:
        return True
    elif node.value != value:
        return search(value, node.next)

def length(node):
    if node == None:
        return 0
    elif node.next != None:
        return 1 + length(node.next)
    else:
        return 1 + length(node.next)

def sum_list(node):
    if node == None:
        return 0
    elif node.next != None:
        return node.value + sum_list(node.next)
    else:
        return node.value + sum_list(node.next)

def count(value, node):
    if node == None:
        return 0
    elif node.value == value:
        return 1 + count(value, node.next)
    else:
        return count(value, node.next)

def reverse(node):
    # if list is empty return None
    if node == None:
        return None

    # last node has to get returned to stack
    if node.next == None:
        return node
    # call until last node is return and assign to head_node
    new_head = reverse(node.next)
    node.next.next = node
    node.next = None
    return new_head

def remove_fake_requests(head):
    # if lsit is empty
    if head == None:
        return None
    # base case
    if head.next == None:
        return head

    # recursion
    if head.value == head.next.value:
        temp_head = head.value
        # while the duplicates still exist
        while head.value == temp_head:
            # if last element return None
            if head.next == None:
                head.value = None
                head = None
                return None
            # if two duplicates left
            if head.value == head.next.value:
                head.next = head.next.next
                if head.next == None:
                    head.value = None
                    head = None
                    return None
                head.value = head.next.value
                head.next = head.next.next
            # if one duplicate left
            else:
                head.value = head.next.value
                head.next = head.next.next
        remove_fake_requests(head)
    else:
        remove_fake_requests(head.next)

    # if list is empty return none
    if head.value == None:
        return None
    else:
        return head



