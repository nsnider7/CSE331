"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""

# from InsertionSort import insertion_sort
# from DoublyLinkedList import DLLNode
from Project3.InsertionSort import *
from Project3.DoublyLinkedList import *

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
    if size <= threshold and size > 0: # could be one idk
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
    rhand_size = 0
    val = tup[0]


    # Reset tail if needed
    while dll.get_tail().get_next() != None and dll.get_tail() != None:
        dll.set_tail(dll.get_tail().get_next())
        end = dll.get_tail()

    while (is_equal(val,end) == False):
    # while val is not end:
        rhand_size += 1
        val = val.get_next()

    quick_sort(dll, start, tup[0].get_previous(), tup[1], threshold)
    quick_sort(dll, tup[0].get_next(), end, rhand_size, threshold)


def partition(low, high):
    pivot = high
    curNode = low
    sizeNode = low
    # get intial size to get accurate size at end
    count = 0
    while sizeNode != high and sizeNode.get_next() != None:
        count +=1
        sizeNode = sizeNode.get_next()
        if sizeNode == high:
            count+=1
            break
    if curNode.get_next() == None and curNode.get_previous() == None:
        return (curNode, 0)
    while curNode != None and high != None:
        # If curNode great than pivot value
        if curNode.get_value() >= high.get_value():
            if curNode.get_value() < low.get_value():
                low = curNode
            if is_equal(curNode, high):
                break

            # if curNode is pivot:
            #     break
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
                # if curNode.get_next() is high:
                    high.set_previous(None)
                curNode.set_value(curNode.get_next().get_value())
                # curNode = curNode.get_next()
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
    size = 1
    #
    # if pivot.get_previous() == None:
    #     size = 0
    # elif pivot.get_previous().get_value() < low.get_value() and pivot.get_previous().get_value() < high.get_value():
    #     return (high, 0)
    # pivot = pivot.get_previous()
    if pivot == low:
        return (high, size)
    pivot = pivot.get_previous()
    while pivot != low and size < count - 1 and pivot != None:
        size += 1
        pivot = pivot.get_previous()
    # print(size)


    # get the size from start to pivot
    return (high, size)
