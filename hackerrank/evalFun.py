lines = ['12','insert 0 5','insert 1 10','insert 0 6','print ','remove 6','append 9','append 1','sort ','print','pop','reverse','print']

def processinput(line):
    command , *args = line.strip().split()
    newargs = ','.join(str(i) for i in args)
    if (newargs == ''):
        return special(command)
    else:
        return str('x.{}({})'.format(command,newargs))

def special(command):
    if(command=='print'):
        return str('{}(x)'.format(command))
    else:
        return str('x.{}()'.format(command))

def evaluate(s):
    #this link helped : http://lybniz2.sourceforge.net/safeeval.html
    #'__builtins__':{} instead of '__builtins__':None
    #we need __builtins__ here. Also, {'x':x} means use local variable x (only)
    eval(s,{},{'x':x})

x = []
for inputline in lines[1:]:
    evaluate(processinput(inputline))



'''
op:

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
