import re
import collections


#player1 ==> vowel's guy
#player2 ==> consonant's guy
player = {1:0 , 2:0} #player:score
myset = set()

def overlappingCount(sub,text):
	pattern = '(?={})'.format(sub)	
	return sum(1 for _ in re.finditer(pattern,text))


def updateScore(sub,text):
	
	if len(sub) == 0:
		return
	
	c = sub[0]
	
	if c in 'AEIOU':
		#update vowel player score
		count = overlappingCount(sub,text)
		player[1] += count
		#print('\tVVV sub = {} , count = {} , tot = {},{}'.format(sub,count,player[1],player[2]))
	else:
		#update consonant player score
		count = overlappingCount(sub,text)
		player[2] += count
		#print('\tCCC sub = {} , count = {} , tot = {},{}'.format(sub,count,player[1],player[2]))

def go(ipstr):
	myDict = collections.defaultdict()
	startPos = 0
	endPos = len(ipstr)
	
	for outer in range(endPos + 1):
		for inner in range(outer,endPos + 1):
			substr = ipstr[outer:inner + 1]
			if substr in myset:
				continue
			else:
				myset.update([substr])
				updateScore(substr,ipstr)
			
go('BAAAAAAAAANAAAAAAANAAAANAAASSSSSSSSSNAAAAAAAAAASSSSSSSSS')
