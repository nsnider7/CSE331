"""
PROJECT 3 - Quick/Insertion Sort
Name: Nicholas Snider
PID: A51766181
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
    """
    insertion_sort
    :param dll: dll to sort
    :param low: first node in dll
    :param high: last node in dll
    :return: sort dll
    """
    length = dll.get_size()
    if length == 0:
        return
    curnode = low.get_next()
    while curnode is not None:
        tempnode = curnode
        while tempnode.get_previous() is not None and tempnode.get_value() < tempnode.get_previous().get_value():
            tempvalue = tempnode.get_value()
            tempnode.set_value(tempnode.get_previous().get_value())
            tempnode.get_previous().set_value(tempvalue)
            tempnode = tempnode.get_previous()
        if curnode == high:
            break
        curnode = curnode.get_next()
