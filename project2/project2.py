"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: Roderick Whang (rjw34)
Partner 2: Sang-Jyh Lin (sl605)
Date: 10/19/2020
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
        route = Queue() # create an empty queue object to process maze
        pass
    elif alg == 'DFS':
        route = Stack() # use stack object to process maze
        #initialize the route with a list of 3 "None" elements
        pass

    #print("initialize all vertex in the adjList")
    #print(maze.adjList)

    #initialize the maze
    for vertex in maze.adjList:
        vertex.visited = False
        vertex.prev = None
        vertex.dist = math.inf
    maze.path = []


    #implementing BFS/DFS
    maze.start.visited = True# set as visited
    maze.start.dist = 0

    route.push(maze.start) #push start to queue/stack

    #visit every possible vertices

    while route.isEmpty() is False:
        current = route.pop() # pop from queus/stack
        #print("current position",current)
        #print("neighbor for current",current.neigh)
        for neigh in current.neigh:
            if neigh.visited is False:
                if route.isFull(): # checking queue/stack is full
                    route.resize() # resize queue/stack if it is full
                neigh.visited = True
                neigh.dist = current.dist +1
                route.push(neigh)
                neigh.prev = current

                #print("rank of neighbor",neigh.rank)
                #print("previous rank of this neighbor",neigh.prev)
        #print("end of this position", current)
        #print(" ")

    #print("Now checking the path")
    #dist = maze.exit.dist

    # perform backward selection to find the start->exit path!
    backward = maze.exit
    maze.path = [backward.rank] + maze.path
    while backward.dist !=0:
        maze.path = [backward.prev.rank]+maze.path #only put rank number to the list of our path
        backward = backward.prev

        #print(maze.path)
        #print(backward.rank)
        #print(backward.neigh)
        #print(backward.dist)
        #print(backward.visited)
        #print(backward.prev)
        #print(" ")

    return maze.path


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)
