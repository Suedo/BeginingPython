from collections import deque

ip = input().split();
numrows = int(ip[0])
numcols = int(ip[1])
rotate = int(ip[2])

arr = [[int(col) for col in row] for row in (input().split() for i in range(numrows))]

#print('{} {} {}'.format(numrows,numcols,rotate))
#print(arr)
	


def less(a,b):
    if(a < b):
        return a
    else:
        return b

#constraint : lower value needs to be even
levels = less(numrows,numcols)//2
buffer = {level:deque() for level in range(levels)}

#creating sq array with random elements
#arr = [[random.choice(x) for cols in range(numcols)] for rows in range(numrows)]

myarr =[ 
            [1,   2,   3,   4,   5 ],
            [14,  15,  16,  17,  6 ],
            [13,  20,  19,  18,  7 ],
            [12,  11,  10,  9,   8 ]  
        ]


pos = {0:0 , 1:0} #level:value
flag = ('populate','retrieve') #to,from deque

def printarr(arr):
    for eachrow in arr:
        for eachcol in eachrow:
            print('{:5d}'.format(eachcol),end='')
        print('')

def left(arr,flag):
    #row fixed. level signifies row.
    for level in range(levels):
        for cols in range(level,numcols - level - 1): # (0,1,2,3),(1,2)
            if(flag == 'populate'):
                buffer[level].append(arr[level][cols])
            else: #retrieve
                arr[level][cols] = buffer[level][pos[level]]
                pos[level] += 1  #this behaves like a static


def down(arr,flag):
    #col fixed, level signifies col.
    for level in range(levels):
        for rows in range(level,numrows - level - 1): # (0,1,2),(1)
            if(flag == 'populate'):
                buffer[level].append(arr[rows][numcols - level - 1])
            else: #retrieve
                arr[rows][numcols - level - 1] = buffer[level][pos[level]]
                pos[level] += 1 


def right(arr,flag):
    #row fixed. level signifies row. col descending.
    for level in range(levels): #0,1
        for cols in reversed(range(level + 1,numcols - level)): # (4,3,2,1),(3,2)
            if(flag == 'populate'):
                buffer[level].append(arr[numrows - level - 1][cols])    
            else: #retrieve
                arr[numrows - level - 1][cols] = buffer[level][pos[level]]
                pos[level] += 1 

def up(arr,flag):
    #col fixed, level signifies col. row descending.
    for level in range(levels):
        for rows in reversed(range(level + 1,numrows - level)): # (3,2,1),(2)
            if(flag == 'populate'):
                buffer[level].append(arr[rows][level])
            else: #retrieve
                arr[rows][level] = buffer[level][pos[level]]
                pos[level] += 1


def buildlevels(arr,f):
    left(arr,f)
    down(arr,f)
    right(arr,f)
    up(arr,f)



buildlevels(arr,flag[0])    


for level in buffer:
	buffer[level].rotate(-rotate) 


buildlevels(arr,flag[1])
printarr(arr)
