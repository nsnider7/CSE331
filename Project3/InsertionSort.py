"""
PROJECT 3 - Quick/Insertion Sort
Name:
PID:
"""


def _insertion_wrapper(insertion_sort):
    """
    DO NOT EDIT
    :return:
    """
    def insertion_counter(*args, **kwargs):
        if args[0].size > 1:
            args[0].c += 1
        insertion_sort(*args, **kwargs)
    return insertion_counter

# ------------------------Complete function below---------------------------
@_insertion_wrapper
def insertion_sort(dll, low, high):
    length = dll.get_size()
    if length == 0:
        return
    curNode = low.get_next()
    while curNode != None:
        tempNode = curNode
        while tempNode.get_previous() != None and tempNode.get_value() < tempNode.get_previous().get_value():
            tempValue = tempNode.get_value()
            tempNode.set_value(tempNode.get_previous().get_value())
            tempNode.get_previous().set_value(tempValue)
            tempNode = tempNode.get_previous()
        if curNode == high:
            break
        curNode = curNode.get_next()





