def gen(l):
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            yield l[i + 1]

l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_l = [el for el in gen(l)]
print(new_l)

