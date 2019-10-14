"""
PROJECT 3 - Quick/Insertion Sort
Name: Nicholas Snider
PID: A51766181
"""

from Project3.InsertionSort import *


def quick_sort(dll, start, end, size, threshold):
    """
    Uses the quick sort algorithm to sort the DLL
    :param dll: [DLL] the dll to sort
    :param start: [DLLNode] start of dll to sort
    :param end: [DLLNode] end of dll to sort
    :param size: [int] size of dll
    :param threshold: [int] size that if less than or equal to will send dll to insertion sort
    :return: [DLL] sort dll
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
    while val is not end:
        rhand_size += 1
        val = val.get_next()

    quick_sort(dll, start, tup[0].get_previous(), tup[1], threshold)
    quick_sort(dll, tup[0].get_next(), end, rhand_size, threshold)


def partition(low, high):
    """
    partitions the DLL so that the last element is pivot and puts everything
    less than the pivot to the less and everything greater to the right
    :param low: [DLLNode] first element in DLL
    :param high: [DLLNode] last element in DLL
    :return: (tuple) pivot node and size from start to pivot
    """
    leftnode = low
    rightnode = high.get_previous()
    pivot = high
    count = 0
    sizenode = low
    # get the original size
    while sizenode is not high and sizenode.get_next() is not None:
        count += 1
        sizenode = sizenode.get_next()
        if sizenode is high:
            count += 1
            break
    # if 1 return size 0
    if leftnode.get_next() is None and leftnode.get_previous() is None:
        return leftnode, 0
    while leftnode is not rightnode and leftnode.get_previous() is not rightnode:
        # if left is bigger than right swap
        if leftnode.get_value() >= pivot.get_value() and rightnode.get_value() < pivot.get_value():
            tempval = leftnode.get_value()
            leftnode.set_value(rightnode.get_value())
            rightnode.set_value(tempval)
            rightnode = rightnode.get_previous()
            leftnode = leftnode.get_next()
        # if they're both bigger than pivot
        elif leftnode.get_value() >= pivot.get_value() and rightnode.get_value() >= pivot.get_value():
            rightnode = rightnode.get_previous()
        # if they're both smaller than pivot
        elif leftnode.get_value() <= pivot.get_value() and rightnode.get_value() <= pivot.get_value():
            leftnode = leftnode.get_next()
        else:
            rightnode = rightnode.get_previous()
            leftnode = leftnode.get_next()

    if rightnode is leftnode:
        # if stops on element that is larger than pivot
        if pivot.get_value() < leftnode.get_value():
            tempval = leftnode.get_value()
            leftnode.set_value(pivot.get_value())
            pivot.set_value(tempval)
            pivot = leftnode
        # if stops on element that is still smaller than pivot
        elif pivot.get_value() < leftnode.get_next().get_value():
            leftnode = leftnode.get_next()
            tempval = leftnode.get_value()
            leftnode.set_value(pivot.get_value())
            pivot.set_value(tempval)
            pivot = leftnode
    elif rightnode.get_next() is leftnode:
        if pivot.get_value() < leftnode.get_value():
            tempval = leftnode.get_value()
            leftnode.set_value(pivot.get_value())
            pivot.set_value(tempval)
            pivot = leftnode
    testpiv = pivot
    if testpiv is low:
        return pivot, 0
    size = 1
    testpiv = testpiv.get_previous()
    # get size of left hand side
    while testpiv != low and size < count - 1 and testpiv is not None:
        size += 1
        testpiv = testpiv.get_previous()
    # get the size from start to pivot
    return pivot, size
