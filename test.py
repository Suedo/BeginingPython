import re
s = 'qA2'

alnum = re.compile('{}'.format('\\w'))
alpha = re.compile('{}'.format('[a-zA-Z]'))
digit = re.compile('{}'.format('\\d'))
lower = re.compile('{}'.format('[a-z]'))
upper = re.compile('{}'.format('[A-Z]'))

print(bool(re.search(alnum,s)))
print(bool(re.search(alpha,s)))
print(bool(re.search(digit,s)))
print(bool(re.search(lower,s)))
print(bool(re.search(upper,s)))
