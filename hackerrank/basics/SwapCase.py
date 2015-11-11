for i in input():
	if ord(i) >= ord('A') and ord(i) <= ord('Z'):
		print('{:c}'.format(ord(i) + 32),end='')
	elif ord(i) >= ord('a') and ord(i) <= ord('z'):
		print('{:c}'.format(ord(i) - 32),end='')
	else:
		print(i,end='')
