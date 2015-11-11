#find all subsets of a set of 4 entries
#let set be of single character strings : (a,b,c,d)


import itertools as itools
import re
import collections

givenstring = 'BANANANAAAS'
pointschart = collections.defaultdict()
player = {'Stuart':0, 'Kevin':0}
vowels = re.compile(r'[AEIOU]')

def getCountOf(sub,text):
    #counts number of subset in string
    useoverlapping = False
    

    if(useoverlapping):
    
        #non-overlapping matches : this would count only one 'ANA' in 'BANANA'
        return sum(1 for _ in re.finditer(sub,text))

    else:
        
        #overlapping matches : this would count two 'ANA's in 'BANANA'
        return len(re.findall('(?={0})'.format(re.escape(sub)), text))



def updatescore():
    mydict = dict(pointschart)
    for string, score in mydict.items():
        #read re.search vs re.match here : https://docs.python.org/3/library/re.html#search-vs-match
        if(vowels.match(string)):
            player['Kevin'] += score 
        else:
            player['Stuart'] += score
    



#Find Power Set (minus null set) of the set formed by characters of givenstring
for subset_length in range(1, len(givenstring) + 1):

    for eachTuple in itools.combinations(givenstring,subset_length):

        subset = ''.join([each_str_in for each_str_in in eachTuple])
        score = getCountOf(subset,givenstring)
        pointschart[subset] = score

updatescore()


'''
#print out pointschart sorted based on key-length, and then alphabetical order
for eachtuple in sorted(mydict.items(), key = lambda x : (len(x[0]),x[0])):
    subset , score = eachtuple
    print('{} : {}'.format(subset,score))

    
print(player.items())
'''
WinnerName , WinningScore = sorted(player.items(), key = lambda x : x[1])[1] #only two players

print('{} {}'.format(WinnerName , WinningScore))

for eachtuple in sorted(dict(pointschart).items(), key = lambda x : (len(x[0]),x[0])):
    subset , score = eachtuple
    if(score > 0): print('{} : {}'.format(subset,score))
