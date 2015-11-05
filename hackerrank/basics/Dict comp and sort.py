#Dict Comprehension basics

my_dict = {key:val for key, val in zip('pqcde',[5,4,3,2,1])}

print(my_dict) # {'d': 2, 'e': 1, 'c': 3, 'p': 5, 'q': 4} - No order


#Default Sorting on keys
d1 = sorted(my_dict.items())
print(d1)    # [('c', 3), ('d', 2), ('e', 1), ('p', 5), ('q', 4)]


#Sort based on values
#http://stackoverflow.com/a/2258273/2715083
d2 = sorted(my_dict.items(), key = lambda x: x[1])
print(d2)    # [('e', 1), ('d', 2), ('c', 3), ('q', 4), ('p', 5)]


#Sort on values, desc. 
d3 = sorted(my_dict.items(), key = lambda x: x[1] , reverse = True)
print(d3)    # [('p', 5), ('q', 4), ('c', 3), ('d', 2), ('e', 1)]
