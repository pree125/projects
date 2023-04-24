import re

para = 'this is the start.\nFrom: pree From'

para = para.split('\n')
for line in para:
    if (re.search('^From',line)):
        print(line)
    if (line.startswith('From')):
        print(line)
