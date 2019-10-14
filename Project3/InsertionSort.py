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
<<<<<<< HEAD
    insertion_sort
    :param dll: dll to sort
    :param low: first node in dll
    :param high: last node in dll
    :return: sort dll
=======
    Sort the dll using the insertion sort algorithm
    :param dll: [DLL] dll to sort
    :param low: [DLLNode] first node in dll
    :param high: [DLLNode] last node in dll
    :return: [DLL] sorted dll
>>>>>>> f39e3b14ac55bc1f92fc152e7e5a0672b52e0cc7
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
