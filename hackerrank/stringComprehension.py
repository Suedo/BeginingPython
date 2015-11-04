lines = ['12','insert 0 5','insert 1 10','insert 0 6','print ','remove 6','append 9','append 1','sort ','print','pop','reverse','print']

def processinput(line):
    command , *args = line.strip().split()
    newargs = ','.join(str(i) for i in args)
    return str('{}({})'.format(command,newargs))

for inputline in lines:
    print(processinput(inputline))



'''
op:

12()
insert(0,5)
insert(1,10)
insert(0,6)
print()
remove(6)
append(9)
append(1)
sort()
print()
pop()
reverse()
print()
'''
