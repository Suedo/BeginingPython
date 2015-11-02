N  = 4
entries = [(row,col) for row in range (1,N+1)
                       for col in range(1,N+1)]

print(entries)


for row,col in entries:
    print('{},{} == {: 2d}'.format(row,col,N*(int(row)-1) + int(col)))

