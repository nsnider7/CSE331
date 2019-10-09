"""
PROJECT 3 - Quick/Insertion Sort
Name: Nicholas Snider
PID: A51766181
"""

from InsertionSort import insertion_sort
# from DoublyLinkedList import DLLNode
# from Project3.InsertionSort import *
# from Project3.DoublyLinkedList import *


def is_equal(first, second):
    """
    is_equal
    :param first: first node to compare
    :param second: second node to compare
    :return: a comparison of the first and second node
    """
    # if prev and next node are equal
    if first.get_previous() == second.get_previous() and first.get_next() == second.get_next() \
            and first == second:
        # to make sure they're equal test the next next and previous previous node
        if first.get_previous() is not None and second.get_previous() is not None \
                and first.get_next() is not None and second.get_next() is not None:
            if first.get_previous().get_previous() == second.get_previous().get_previous() \
                    and first.get_next().get_next() == second.get_next().get_next():
                return True
            else:
                return False
        return True
    else:
        return False


def quick_sort(dll, start, end, size, threshold):
    """
    quick_sort
    :param dll: the dll to sort
    :param start: start of dll to sort
    :param end: end of dll to sort
    :param size: size of dll
    :param threshold: size that if less than or equal to will send dll to insertion sort
    :return: sort dll
    """
    if threshold >= size > 1:  # could be one idk
        insertion_sort(dll, start, end)
        return
    else:
        if size < 2:
            return
        # returns (pivot node, size from start to pivot)
        tup = partition(start, end)

        if tup[0] is None:
            return

    # Get right hand size, start with 0 because of .get_next() call below
    rhand_size = 0
    val = tup[0]

    # Reset tail if needed
    while dll.get_tail().get_next() is not None and dll.get_tail() is not None:
        dll.set_tail(dll.get_tail().get_next())
        end = dll.get_tail()

    # while value is not end
    while not is_equal(val, end):
        rhand_size += 1
        val = val.get_next()

    quick_sort(dll, start, tup[0].get_previous(), tup[1], threshold)
    quick_sort(dll, tup[0].get_next(), end, rhand_size, threshold)


def partition(low, high):
    """
    partition
    :param low: first element in DLL
    :param high: last element in DLL
    :return: (tuple) pivot node and size from start to pivot
    """
    pivot = high
    curnode = low
    sizenode = low
    # get initial size to get accurate size at end
    count = 0
    while sizenode != high and sizenode.get_next() is not None:
        count += 1
        sizenode = sizenode.get_next()
        if sizenode == high:
            count += 1
            break
    if curnode.get_next() is None and curnode.get_previous() is None:
        return curnode, 0
    while curnode is not None and high is not None:
        # If curNode great than pivot value
        if curnode.get_value() >= high.get_value():
            if curnode.get_value() < low.get_value():
                low = curnode
            if is_equal(curnode, high):
                break
            # tempnode = DLLNode(curnode.get_value())
            # tempnode.set_next(high.get_next())
            # tempnode.set_previous(high)
            tempnode = curnode
            tempnode.set_next(high.get_next())
            tempnode.set_previous(high)

            # if first node to ad to end
            if high.get_next() is None:
                high.set_next(tempnode)
            # if second node to append, change the next values previous value
            else:
                high.get_next().set_previous(tempnode)
                high.set_next(tempnode)

            # # if last node
            if curnode.get_next() is None:
                curnode.get_previous().set_next(None)
                curnode = None
            # If first node
            elif curnode.get_previous() is None:
                if is_equal(curnode.get_next(), high):
                    high.set_previous(None)
                curnode.set_value(curnode.get_next().get_value())
                curnode.set_next(curnode.get_next().get_next())
                curnode.get_next().set_previous(curnode)
            # if middle node
            elif curnode.get_previous().get_value() is not None:
                curnode.get_previous().set_next(curnode.get_next())
                curnode.get_next().set_previous(curnode.get_previous())
                curnode = curnode.get_next()

        # if next value equals the pivot
        elif curnode.get_next() == high or curnode == high:
            break
        else:
            curnode = curnode.get_next()
    size = 1
    if pivot == low:
        return high, size
    pivot = pivot.get_previous()
    while pivot != low and size < count - 1 and pivot is not None:
        size += 1
        pivot = pivot.get_previous()
    # get the size from start to pivot
    return high, size
