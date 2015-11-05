#Using Default Dictionary
#FLUENT PYTHON : Page 71

import collections

mylist = ['5',['Harry','37.21'],['Berry','37.21'],['Tina','37.2'],['Akriti','41'],['Harsh','39']]
N = int(mylist[0])

#If loop encounters a new key, create it with an empty list as value
#to which you can later .append(stuff)
mydict = collections.defaultdict(list)

for entry in mylist[1:]:
    name,marks = entry
    mydict[float(marks)].append(name)

#want to get the names of students with second lowest marks
newdict = dict(mydict)
anslist = sorted(newdict.items()) #list view of newdict, ascending order

#Our Advantage : keys in dict are hashable, aka unique.
#Thus if multiple students got same marks, they will be added as a list to one marks key
#Thus, students with second lowest marks :
print(','.join(anslist[1][1]))       # anslist[1] = (37.21, ['Harry', 'Berry'])
