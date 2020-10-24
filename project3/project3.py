"""
Math 560
Project 3
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    ##### Your implementation goes here. #####
    #bellmondford here
    v = len(adjList)#n = # of vertex
    adjList[0].dist = 0
    tol = 1e-15
    negcyc=None
    # Bellman-Ford method
    for i in range(v-1):#normal bellman ford (run v-1 loops)
        for vertex in adjList:#for every vertex
            for neighbor in vertex.neigh:#loop through all neighbor for this vertex
                if vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol < neighbor.dist: #vertex's cost + edge cost < neighbor's current cost -> update neighbor's "cost and prev"
                    neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                    neighbor.prev = vertex
    
    #Arbitrage detecting (run the v-th loop)
    for vertex in adjList:#for every vertex
        for neighbor in vertex.neigh:#loop through all neighbor for this vertex
            if vertex.dist + adjMat[vertex.rank][neighbor.rank] + tol < neighbor.dist: #if we have new update
                neighbor.dist = vertex.dist + adjMat[vertex.rank][neighbor.rank]
                neighbor.prev = vertex
                #print(neighbor)
                negcyc = neighbor #save start vertex
    # new approach to construct neg cycle
    if negcyc:#if there's negative cycle
        #searching backward to find the cycle
        backward = negcyc
        negCyc = [negcyc.rank]
        while (backward.prev.dist != negcyc.dist):
            negCyc = [backward.prev.rank] + negCyc
            backward = backward.prev

        negCyc = [negCyc[-1]] + negCyc
        return negCyc
    else: return []

    
    ### original approach    
#    if negcyc:#if there's negative cycle
#        #searching backward to find the cycle
#        #i = 0
#        while (negcyc[0].prev.rank != negcyc[-1].rank):
#            negcyc = [negcyc[0].prev] + negcyc
#            #i+=1
#        negcyc = [negcyc[-1]] + negcyc
#        negCyc = negcyc.copy()
#        for i in range(len(negcyc)):
#            negCyc[i] = negcyc[i].rank
#        return negCyc
#    else: return []
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    rtm = [[-math.log(R) for R in row] for row in rates]
    #print(rtm)
    return rtm
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
