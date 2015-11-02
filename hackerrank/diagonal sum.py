'''
Getting the sum of leading diagonal and the 'other' diagonal of an NxN matrix
while storing only N elements (each row) at a time
'''
mylist = [entry for entry in range(10)]
print(mylist)

lsum = 0
rsum = 0

for i in mylist:
    lsum = lsum + mylist[i]     #leading diagonal : left upper -> right lower
    rsum = rsum + mylist[-i]    #'other' diagonal : right upper -> left lower 

print('lsum = {} , rsum = {}'.format(lsum,rsum))
