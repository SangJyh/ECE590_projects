"""
Math 560
Project 1
Fall 2020

Partner 1: Sang-Jyh Lin
Partner 2: Roderick Whang
Date: 10/02/2020
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    for i in range(len(listToSort)):

    # Find the minimum element
        min_index = i
        for j in range(i+1, len(listToSort)):
            if listToSort[min_index] > listToSort[j]:
                min_index = j
    # Swap minimum element with the first element
        listToSort[i], listToSort[min_index] = listToSort[min_index], listToSort[i]
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for i in range(1, len(listToSort)):
        k = listToSort[i] #set key element
        j = i-1
        # move element of listToSort[0..i-1]  if greater than key element
        while j >=0 and listToSort[j] > k :
            listToSort[j+1] = listToSort[j]
            j -= 1
        listToSort[j+1] = k
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    a = "start"
    while a != "no_sort":
        a = "no_sort"
        for i in range(len(listToSort)-1):
            if listToSort[i]>listToSort[i+1]:
                a = listToSort[i]
                listToSort[i] = listToSort[i+1]
                listToSort[i+1] = a
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):

    if len(listToSort) > 1:
        mid = len(listToSort) // 2
        left = listToSort[:mid]
        right = listToSort[mid:]
        #recursive call
        MergeSort(left)
        MergeSort(right)

        i = 0 #left index
        j = 0 #right index
        k = 0 #listtosort index

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              #value from the left half has been used
              listToSort[k] = left[i]
              #move to the next slot
              i += 1
            else:
                listToSort[k] = right[j]
                #move to the next slot
                j += 1
            #move to the next slot
            k += 1

        #all the remaining values
        while i < len(left):
            listToSort[k] = left[i]
            i += 1 #move to the next slot
            k += 1 #move to the next slot

        while j < len(right):
            listToSort[k]=right[j]
            j += 1 #move to the next slot
            k += 1 #move to the next slot
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print(),
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime()
