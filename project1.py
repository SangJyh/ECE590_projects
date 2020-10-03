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
    if j == None:
        j = len(listToSort)
    pvalue = listToSort[j]
    idx = i-1
    for 
    
    
    #if i == j:#base case
    #    return listToSort    
    #print(listToSort)
#    if len(listToSort)<=2:#base case for under 2 elements
#        if listToSort[i] > listToSort[j]:
#            a = listToSort[i]
#            listToSort[i] = listToSort[j]
#            listToSort[j] = a
#        return listToSort
    

    
    #update p index

        QuickSort(listToSort[:p])# merge commands after partition
        QuickSort(listToSort[p:])
    

    
    #if len(listToSort)<=3:#base case for under 3 elements
    #    if listToSort[i] > listToSort[p]:
    #        a = listToSort[i]
    #        listToSort[i] = listToSort[p]
    #        listToSort[p] = a
    #    if listToSort[j] < listToSort[i]:
    #        a = listToSort[j]
    #        listToSort[j] = listToSort[i]
    #        listToSort[i] = a
    #    if listToSort[j] < listToSort[p]:
    #        a = listToSort[j]
    #        listToSort[j] = listToSort[p]
    #        listToSort[p] = a
    #    return listToSort
    
    #partition
    ##p_value = listToSort[p]#get compare value
    ##for idx in range(len(listToSort)):
    ##    if listToSort[idx]>p_value:
    ##        listToSort[p] = listToSort[idx]
    #p = 0
    
        
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
#    print()
#    print('Testing Bubble Sort')
#    print()
#    testingSuite(BubbleSort)
#    print()
#    print('Testing Merge Sort')
#    print(),
#    testingSuite(MergeSort)
#    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
#    print('DEFAULT measureTime')
#    print()
    measureTime()

    
    
    
    
    
    
    
    
    
    
    
    
    
#        else:
#        p = (i+j)//2
#        high = []
#        low = []
#        pvalue = listToSort[p]
#        print(listToSort)
#        print(pvalue)
#        for idx in range(i, j):
#            if listToSort[idx] <= pvalue:
#                low.append(listToSort[idx])
#            else:
#                high.append(listToSort[idx])
#        p = len(low)
#        print(p)
#        print(low)
#        print(high)
#        print("end")
#        listToSort[:p] = low
#        listToSort[p:] = high