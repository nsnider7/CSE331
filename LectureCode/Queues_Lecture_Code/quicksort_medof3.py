
import random
"""
This is a program which implements the quicksort algorithm
using median of 3: the first, last, and middle element of
the array and letting the pivot be the median of the three.
This program also calculates the number of
comparisons quicksort uses while sorting.

It is not perfect, it may be buggy...but you can modify and test it...
"""


no_of_comparison = 0


# A method to calculate the median of three numbers using two comparisons
def median(a, b, c):
    if (a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c


# A method to partition around the median
def partition_median(array, leftend, rightend):
    left = array[leftend]
    right = array[rightend - 1]
    length = rightend - leftend
    if length % 2 == 0:
        middle = array[int(leftend + length / 2 - 1)]
    else:
        middle = array[int(leftend + length / 2)]

    pivot = median(left, right, middle)

    pivotindex = array.index(pivot)  # only works if all values in array unique

    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i - 1]
    array[i - 1] = leftendval
    return i - 1



def quicksort_median(array, leftindex, rightindex):
    global no_of_comparison
    if leftindex < rightindex:
        newpivotindex = partition_median(array, leftindex, rightindex)

        no_of_comparison += (rightindex - leftindex - 1)
        quicksort_median(array, leftindex, newpivotindex)

        quicksort_median(array, newpivotindex + 1, rightindex)




test3 = [1, 11, 5, 15, 2, 12, 9, 99, 77, 0]
test4 = []
for i in range(1, 101):
    test4.append(i)

left=0
right=len(test3)

quicksort_median(test3, left, right)
print(test3)

left=0
right=len(test4)


quicksort_median(test4, left, right)
print(test4)

