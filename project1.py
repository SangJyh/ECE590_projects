"""
Math 560
Project 1
Fall 2020

Partner 1:
Partner 2:
Date:
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    a = "no_sort"
    for i in range(len(listToSort)-1):
        if listToSort[i]>listToSort[i+1]:
            a = listToSort[i]
            listToSort[i] = listToSort[i+1]
            listToSort[i+1] = a
    if a == "no_sort":
        return listToSort
    else: 
        BubbleSort(listToSort)

"""
MergeSort
"""
def MergeSort(listToSort):
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None. 
    #print(listToSort)
    if j == None:
        j = len(listToSort)
    #partition
    if i < j:
        a = i#move from left
        r = i#move from left
        b = (j-1)#move from right
        pivot = listToSort[b] # initial pivot value
        #timer = 0
        while a <= b:
            #timer+=1
            if listToSort[a] < pivot:#if element a < pivot we are good and we swap a and r
                listToSort[r], listToSort[a] = listToSort[a], listToSort[r]#swap r and a
                a+=1
                r+=1
                
            elif listToSort[a] > pivot:
                listToSort[a], listToSort[b] = listToSort[b], listToSort[a]#swap a and b
                b-=1
            elif listToSort[a] == pivot: # a = pivot a move right
                a+=1
                
            #if timer >100:
            #    print("run-out-of-time")
            #    break
       
        QuickSort(listToSort,i = i, j = r)# merge commands after partition
        QuickSort(listToSort,i = a, j = j)
#testingSuite(QuickSort)                
        
#def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None. 
    #print(listToSort)
#    if j == None:
#        j = len(listToSort)
    #partition
#    if i < j:
#        pivot = listToSort[j-1]#set pivot
#        low = []
#        high = []
#        for r in range(i,j):
#            if listToSort[r] < pivot:
#                low.append(listToSort[r])
#            if listToSort[r] >= pivot:
#                high.append(listToSort[r])
#        QuickSort(low)# merge commands after partition
#        QuickSort(high)
#        low.append(high)
#        listToSort = low.copy()


"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
#    print('Testing Selection Sort')
#    print()
#    testingSuite(SelectionSort)
#    print()
#    print('Testing Insertion Sort')
#    print()
#    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
#    print('Testing Merge Sort')
#    print(),
#    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
#    print('DEFAULT measureTime')
#    print()
    measureTime()