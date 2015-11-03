#Matrix Rotation
#This is for practice only. NumPy has these builtin


import re
import random

x = range(100)
N = 5

#method to print a 2D array
def printArr(arr,N):
    for eachrow in arr:
        for eachcol in eachrow:
            print('{:5d}'.format(eachcol),end='')
        print('')
    

def cw90(arr,numOfTurns):
    for i in range(numOfTurns):
        arr = list(zip(*arr[::-1]))

    return arr


def ccw90(arr,numOfTurns):
    for i in range(numOfTurns):
        arr = list(zip(*arr))[::-1]

    return arr



#creating sq array with random elements
arr = [[random.choice(x) for cols in range(N)] for rows in range(N)]

print('Created Array:\n')
printArr(arr,N)


print('\n\nrotate cw 1 times\n')
printArr(cw90(arr,1),N)


print('\n\nrotate ccw 1 times\n')
printArr(ccw90(arr,1),N)


    
