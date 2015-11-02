'''
Referemce : https://docs.python.org/3/library/string.html#formatexamples
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
'''
num = 5
print('\noutput 1 :\n')
#experiment 1
for i in reversed(range(num)):
	print('{:{fill}{align}{width}s}'.
              format('#',fill='-',align='>',width=i+1))

print('\noutput 2 :\n')

#experiment 2
for i in range(num):
	print('{:{fill}{align}{width}0}'.    #0 after {width} makes effective width = {width}*10
              format('#'*(i+1),fill='-',align='>',width=num))
    
'''
output 1 :

----#
---#
--#
-#
#

output 2 :

-------------------------------------------------#
------------------------------------------------##
-----------------------------------------------###
----------------------------------------------####
---------------------------------------------#####
'''
