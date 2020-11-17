from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]
c = reduce(lambda a, b: a * b, my_list)
print(c)