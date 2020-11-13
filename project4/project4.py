"""
Math 560
Project 4
Fall 2020

Partner 1:Sang-Jyh Lin (sl605)
Partner 2:Roderick Whang (rjw34)
Date: 11/05/2020
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest):
    n = len(src)
    m = len(dest)

    table = [[999999 for i in range(m+1)] for j in range(n+1)] 
       
    for i in range (n+1):#first to fill the dynamic table
        #print(table)
        for j in range (m+1):
            if i ==0:
                table[i][j] = j#0#
            elif j == 0:
                table[i][j] =i # initialization done

            elif i!=0 and j!=0 and src[i-1]==dest[j-1]: # match
                insert = table[i][j-1]+1
                match = table[i-1][j-1]
                delete = table[i-1][j]+1
                table[i][j] = min(insert,match, delete)
            else:
                insert = table[i][j-1]+1
                sub = table[i-1][j-1]+1
                delete = table[i-1][j]+1
                table[i][j] = min(insert,sub, delete) # decides insert, sub, delete

    dist = table[i][j] # optimal edit number is at (n,m)

    ###### trace back to find each edit ######
    edits = [] # This is a placeholder, remove and implement!



    while i>0  and j >0:
        #print(edits)
        sub = table[i-1][j-1] #can be also a "match" need further check
        insert = table[i][j-1]
        delete = table[i-1][j]
        mini = min(insert,sub, delete)
        
        if mini == sub:
            if sub !=table[i][j]:#different value so there's an edit
                edits = edits + [("sub",dest[j-1],i-1)]#+edits
                j-=1
                i-=1
            else:#we have a match
                edits = edits + [("match",src[i-1],i-1)]#+edits
                i-=1
                j-=1
        elif mini == insert:
            edits = edits + [("insert",dest[j-1],i)] 
            j-=1
        elif mini == delete:
            edits = edits + [("delete",src[i-1],i-1)]
            i-=1

    dist = table[n][m] #+ j
    while j >=1:
        edits = edits + [("insert",dest[j-1],i)] 
        j-=1

    while i >=1:
        edits = edits + [("delete",src[i-1],i-1)]
        i-=1

    return dist, edits

################################################################################


"""
Main function.
"""
if __name__ == "__main__":
    edTests(True)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
