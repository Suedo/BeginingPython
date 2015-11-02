'''
sum of two main diagonals of an NxN matrix
reads ip from stdin:

3
1 2 3
5 6 4
8 9 1


here, N = 3
followed by N lines of N elems each

'''


lsum = 0
rsum = 0

N = int(input())

for i in range(N):
    list = input().split()
    lsum = lsum + int(list[i])
    rsum = rsum + int(list[-(i+1)])   #the (i+1) is the trick

print(abs(lsum - rsum))
