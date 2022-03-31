import re

path = 'C:\\Users\\mansu\\PycharmProjects\\PageRank\\resources\\vector.txt'
s = ''
regex = '(?<=\[).+(?=\])'
with open(path, 'r') as file:
    s = file.read()

s = s[1:-1]
s = s.replace('][', ' ')
values = s[1:-1].split(sep=' ')
values[-1] = values[-1][:-1]
# path = 'C:\\Users\\mansu\\PycharmProjects\\PageRank\\resources\\junk.txt'
# with open(path, 'w') as file:
#     [print(val, file=file) for val in values]
map_ :dict= {}
max_value = max(map(lambda x: [x,float(x)], values), key=lambda t: t[1])
print(values.index(max_value[0]),'rank is', max_value)
