"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: Sang-Jyh Lin (sl605)
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    ##### Your implementation goes here. #####
    elif alg == 'BFS':
        route = Queue() #create an empty queue object to process maze
        pass
    elif alg == 'DFS':
        route = Stack() #use stack object to process maze
        #initialize the route with a list of 3 "None" elements
        pass


        #initialize the maze
    #print("initialize all vertex in the adjList")
    #print(maze.adjList)
    for vertex in maze.adjList:
        vertex.visited = False
        vertex.prev = None
        vertex.dist = math.inf
    maze.path = []


    #implementing BFS/DFS
    maze.start.visited = True# set as visited
    maze.start.dist = 0
<<<<<<< HEAD
    route.push(maze.start) #push start to queue/stack
    
    #visit every possible vertices
=======
    route.push(maze.start) #push start to queue

>>>>>>> 29d7da8c80b5b8261c59b5a2b854c2652439fd9b
    while route.isEmpty() is False:
        current = route.pop()
        #print("current position",current)
        #print("neighbor for current",current.neigh)
        for neigh in current.neigh:
            if neigh.visited is False:
                if route.isFull():
                    route.resize()
                neigh.visited = True
                neigh.dist = current.dist +1
                route.push(neigh)
                neigh.prev = current
                #print("rank of neighbor",neigh.rank)
                #print("previous rank of this neighbor",neigh.prev)
        #print("end of this position", current)
        #print(" ")
    #
    #print("Now checking the path")
    #dist = maze.exit.dist
    
    #perform backward selection to find the start -> exit path!
    backward = maze.exit
    maze.path = [backward.rank] + maze.path
    while backward.dist !=0:
        maze.path = [backward.prev.rank]+maze.path#only put rank number to the list of our path
        backward = backward.prev
        #print(maze.path)
        #print(backward.rank)
        #print(backward.neigh)
        #print(backward.dist)
        #print(backward.visited)
        #print(backward.prev)
        #print(" ")

<<<<<<< HEAD
    #print(maze.path)#check if shortest path when using BFS
=======


>>>>>>> 29d7da8c80b5b8261c59b5a2b854c2652439fd9b
    return maze.path
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)
