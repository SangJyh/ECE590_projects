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
    dist = 0 # This is a placeholder, remove and implement!

    for i in range (n+1): # first to fill the dynamic table

        for j in range (m+1):

            if i ==0:
                table[i][j] = j
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

        if mini == sub: # we have sub or match
            if sub !=table[i][j]: # different value so there's an edit
                edits = edits + [("sub",dest[max(j-1,0)],i-1)] #+edits
                j-=1
                i-=1

            else: # we have a match
                edits = edits + [("match",src[max(i-1,0)],i-1)] #+edits
                i-=1
                j-=1
        elif mini == insert: # we have a insert
            edits = edits + [("insert",dest[max(j-1,0)],i)]
            j-=1

        elif mini == delete: # we have a delete
            edits = edits + [("delete",src[max(i-1,0)],i-1)] # +edits#max(i-1,0)
            i-=1

    while j >=1: # i = 0
        edits = edits + [("insert",dest[max(j-1,0)],i)]
        j-=1
    while i >=1: # j = 0
        edits = edits + [("delete",src[max(i-1,0)],i-1)] # +edits#max(i-1,0)
        i-=1


    #print(edits)
    return dist, edits

################################################################################









"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
