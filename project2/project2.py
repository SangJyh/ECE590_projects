"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1:
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
    elif alg == 'BFS':
        route = Queue() #create an empty queue object to process maze
        pass
    elif alg == 'DFS':
        route = Stack() #use stack object to process maze
        #initialize the route with a list of 3 "None" elements
        pass
    ##### Your implementation goes here. #####
    #implementing BFS/DFS
    maze.start.visited = True# set as visited
    maze.start.dist = 0
    route.push(maze.start) #push start to queue
    
    while route.isEmpty() is False:
        current = route.pop()
        print(current)
        print(current.neigh)
        for neigh in current.neigh:
            if neigh.visited is False:
                if route.isFull():
                    route.resize()
                neigh.visited = True
                neigh.dist = current.dist +1
                route.push(neigh)
                route.prev = current
    #
    print("Now checking the path")
    dist = maze.exit.dist
    backward = maze.exit
    maze.path = [backward] + maze.path
    while backward.dist !=0:
        print(backward.rank)
        print(backward.neigh)
        print(backward.dist)
        print(backward.visited)
        print(backward.prev)
        print(" ")
        maze.path = [backward.prev]+maze.path
        backward = backward.prev
        
        
        
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
