X = int(input()) + 1
Y = int(input()) + 1
Z = int(input()) + 1
N = int(input())


m = [[x,y,z] for x in range(X) for y in range(Y) for z in range(Z) if (x+y+z)!=N]
print(sorted(m))
