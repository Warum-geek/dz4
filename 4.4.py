def gen(l):
    for j in range(len(l) - 1):
        i = 0
        while True:
            if i != j:
                if l[j] == l[i]:
                    break
            if i == int(len(l)) - 1:
                yield l[j]
                break
            i += 1

my_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_l = [el for el in gen(my_l)]
print(new_l)