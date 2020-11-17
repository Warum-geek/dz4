from itertools import count
from sys import argv

script_name, start, end = argv

for el in count(int(start)):
    print(el)
    if el == end:
        break
