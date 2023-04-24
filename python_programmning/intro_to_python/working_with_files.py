# Working with files
try:
    handle = open('mbox.txt','r')
except:
    print(f'Cant open {handle}')
    quit()

for lines in handle:
    lines = lines.rstrip().upper()
    print(lines)

# input = handle.read()
# print(input)
 
purse = dict()
purse['money'] = 12
purse['owner'] = 'pree'

names = ['proboda','alfonso','alfonso','pierre','proboda','alfonso','pierre','proboda','alfonso','pierre']

name_dict = dict()
for name in names:
    name_dict[name] = name_dict.get(name,0)+1


print(name_dict)
counter = dict()

paragraph = 'My name is proboda and I am a Mechanical Engineer.\nI live in California.\nI work at applied intuition'
paragraph = paragraph.split('\n')
for sentence in paragraph:
    sentence = sentence.split()
    for word in sentence:
        counter[word] = counter.get(word,0) + 1

max_key, max_value = None, None
for key, value in counter.items():
    print(key, value)
    if(max_key is None or max_value < value):
        max_key = key
        max_value = value

max_key, max_value = None, None
for key in counter:
    key = key
    value = counter[key]
    if(max_key is None or max_value < value):
        max_key = key
        max_value = value

print(counter)
temp = list()

for key, value in counter.items():
    temp.append((value,key))

for value, key in sorted(temp, reverse = True)[:10]:
    print(key, value)
