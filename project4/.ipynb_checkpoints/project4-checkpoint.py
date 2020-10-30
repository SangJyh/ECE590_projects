"""
Math 560
Project 4
Fall 2020

Partner 1:
Partner 2:
Date:
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
    #table[0][0] = 0
    #for i in range(1,n+1): table[i][0] = table[i-1][0] 
    #for j in range(1,m+1): table[0][j] = table[0][j-1]
        
    for i in range (n+1):#first to fill the dynamic table
        #print(table)
        for j in range (m+1):
        
            if i ==0:
                table[i][j] = j 
            elif j == 0:
                table[i][j] =i# initialization done
                
            elif i!=0 and j!=0 and src[i-1]==dest[j-1]:#match
                insert = table[i][j-1]+1
                match = table[i-1][j-1]
                delete = table[i-1][j]+1
                table[i][j] = min(insert,match, delete)
            else:
                insert = table[i][j-1]+1
                sub = table[i-1][j-1]+1
                delete = table[i-1][j]+1
                table[i][j] = min(insert,sub, delete)
                
    dist = table[i][j]#optimal edit number is at (n,m)
    #for row in table:
    #    print(row)

    #print(dist)
    ###### trace back to find each edit ######
    edits = [] # This is a placeholder, remove and implement!
    #edi = dist

        
    while i>0  and j >0:#edi >=0: 
        #print(edits)
        sub = table[i-1][j-1]#can also be a "match" need further check
        insert = table[i][j-1]
        delete = table[i-1][j]
        mini = min(insert,sub, delete)
        
        if mini == sub:
            if sub !=table[i][j]:#different value so there's an edit
                edits = edits + [("sub",dest[max(j-1,0)],i-1)]#+edits
                j-=1
                i-=1
                #edi-=1
            else:#we have a match
                edits = edits + [("match",src[max(i-1,0)],i-1)]#+edits
                i-=1
                j-=1
        elif mini == insert:
            edits = edits + [("insert",dest[max(j-1,0)],i)] 
            j-=1
            #edi-=1
        elif mini == delete:
            edits = edits + [("delete",src[max(i-1,0)],i-1)]# +edits#max(i-1,0)
            i-=1
            #edi-=1
    while j >=1:
        edits = edits + [("insert",dest[max(j-1,0)],i)] 
        j-=1
    while i >=1:
        edits = edits + [("delete",src[max(i-1,0)],i-1)]# +edits#max(i-1,0)
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
