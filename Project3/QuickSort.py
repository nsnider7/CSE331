"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""

from InsertionSort import insertion_sort
from DoublyLinkedList import DLLNode


def is_equal(Anode, Bnode):
    # if prev and next node are equal
    if Anode.get_previous() == Bnode.get_previous() and Anode.get_next() == Bnode.get_next() and Anode == Bnode:
        # to make sure they're equal test the next next and previous previous node
        if Anode.get_previous() != None and Bnode.get_previous() != None and Anode.get_next() != None and Bnode.get_next() != None:
            if Anode.get_previous().get_previous() == Bnode.get_previous().get_previous() \
                    and Anode.get_next().get_next() == Bnode.get_next().get_next():
                return True
            else:
                return False
        return True
    else:
        return False


def quick_sort(dll, start, end, size, threshold):
    # print(dll)
    if size <= threshold and size > 1:
        insertion_sort(dll, start, end)
        return
    else:
        if size < 2:
            return
        # returns (pivot node, size from start to pivot)
        tup = partition(start, end)
        if tup[0] == None:
            return

    # Get right hand size, start with 0 because of .get_next() call below
    rhand_size = 1
    val = tup[0].get_next()


    # Reset head and tail
    # head = dll.get_head()
    # tail =
    # while head.get_previous() != None or head != None:
    #     dll.set_head(head.get_previous())
    while dll.get_tail().get_next() != None and dll.get_tail() != None:
        dll.set_tail(dll.get_tail().get_next())
        end = dll.get_tail()

    while (is_equal(val,end) == False):
        rhand_size += 1
        val = val.get_next()

    quick_sort(dll, start, tup[0].get_previous(), tup[1], threshold)
    quick_sort(dll, tup[0].get_next(), end, rhand_size, threshold)


def partition(low, high):
    pivot = high
    curNode = low
    if curNode.get_next() == None and curNode.get_previous() == None:
        return (curNode, 0)
    while curNode != None and high != None:
        # If curNode great than pivot value
        if curNode.get_value() >= high.get_value():
            if is_equal(curNode, high):
                break
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
                if is_equal(curNode.get_next(), high):
                    high.set_previous(None)
                curNode.set_value(curNode.get_next().get_value())
                curNode.set_next(curNode.get_next().get_next())
                curNode.get_next().set_previous(curNode)
            # if middle node
            elif curNode.get_previous().get_value() != None:
                curNode.get_previous().set_next(curNode.get_next())
                curNode.get_next().set_previous(curNode.get_previous())
                curNode = curNode.get_next()
        # if next value equals the pivot
        elif curNode.get_next() == high or curNode == high:
            break
        else:
            curNode = curNode.get_next()
    size = -1
    while high != low:
        size += 1
        high = high.get_previous()

    # get the size from start to pivot
    return (pivot, size)
