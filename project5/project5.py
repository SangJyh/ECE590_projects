"""
Math 560
Project 5
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    # Initialize all costs to 1 and prev to null.
    #print(adjMat)
    for v in adjList:
        v.cost = math.inf
        v.prev = None
    # Pick an arbitrary start vertex and set cost to 0.
    rd = 0 #randomVertex() #need a function for random vertex  # or we chose the first element or last element
    start =  adjList[rd]   
    start.cost = 0
    
    # Make the priority queue using cost for sorting.
    Q = PriorityQueue(adjList)
    
    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it.
        v = Q.deleteMin()
        v.visited = True
        # For each edge out of v.
        for neighbor in v.neigh:
            # If the edge leads out, update.
            weight = adjMat[v.rank][neighbor.rank]#weight(v, neighbor)
            if not neighbor.visited:
                if neighbor.cost > weight:
                    neighbor.cost = weight
                    neighbor.prev = v
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    X = []# Initialize the empty MST.
    # Initialize all singleton sets for each vertex.
    for vertex in adjList:
        makeset(vertex)
    # Sort the edges by weight.
    edgeList.sort()
    # Loop through the edges in increasing order.
    for e in edgeList:
        # If the min edge crosses a cut, add it to our MST.
        u, v = e.vertices
        if find(u) != find(v):
            X.append(e)
            union(u,v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    ##### Your implementation goes here. #####
    v.pi = v #pi: the parent vertex in the disjoint set
    v.height =0 #height: the height in the disjoint set
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    ##### Your implementation goes here. #####
    while v != v.pi:
        v=v.pi
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    ##### Your implementation goes here. #####
    ru = find(u)
    rv = find(v)
    # If the sets are already the same, return.
    if ru == rv:
        return
    # Make shorter set point to taller set.
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Same height, break tie.
        ru.pi = rv
        # Tree got taller, increment rv.height.
        rv.height += 1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    tour = []#
    #DFS basic
    
    #triangle inequality
    
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
