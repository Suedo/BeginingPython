# Enter your code here. Read input from STDIN. Print output to STDOUT
vowels = ['A', 'E', 'I', 'O', 'U']
s = raw_input()
a = 0
b = 0
for i, c in enumerate(s):
    if c in vowels:
        print('{}  : {} = {}'.format(i,c,len(s) - i))
        b += len(s) - i
    else:
        print('{}  : {} = {}'.format(i,c,len(s) - i))
        a += len(s) - i
        
if a == b:
    print "Draw"
    print('{} {}'.format(a,b))
elif a > b:
    print 'Stuart {}'.format(a)
else:
    print 'Kevin {}'.format(b)
