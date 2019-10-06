"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""


# from Project3.InsertionSort import insertion_sort
from DoublyLinkedList import DLLNode


def quick_sort(dll, start, end, size, threshold):
    if start.get_value() < end.get_value():


    tup = partition(start, end)

    quick_sort(dll, dll.get_head(), tup[0], size, threshold)
    quick_sort(dll, tup[0].get_next(), dll.get_tail(), size, threshold)


def partition(low, high):
    pivot = high
    curNode = low
    while curNode != None:
        # If curNode great than pivot value
        if curNode.get_value() > high.get_value():
            tempNode = DLLNode(curNode.get_value())
            tempNode.set_next(high.get_next())
            tempNode.set_previous(high)
            # if first node to add to end
            if high.get_next() == None:
                high.set_next(tempNode)
            # if second node to append, change the next values previous value
            else:
                high.get_next().set_previous(tempNode)
                high.set_next(tempNode)
            # # if last node
            if curNode.get_next() == None:
                curNode.get_previous().set_next(None)
                curNode = None
            # If first node
            elif curNode.get_previous() == None:
                curNode.set_value(curNode.get_next().get_value())
                curNode.set_next(curNode.get_next().get_next())
                curNode.get_next().set_previous(curNode)
            # if middle node
            elif curNode.get_previous().get_value() != None:
                curNode.get_previous().set_next(curNode.get_next())
                curNode.get_next().set_previous(curNode.get_previous())
                curNode = curNode.get_next()
        # if next value equals the pivot
        elif curNode.get_next() == high:
            break
        else:
            curNode = curNode.get_next()
    # get the size from start to pivot
    size = 1
    while (low != pivot):
        size+=1
        low = low.get_next()
    return (high, size)
    # while (low != None):
    #     print(low)
    #     low = low.get_next()
