from itertools import cycle

my_list = [i for i in input("Введите элементы через пробел: ").split()]
c = cycle(my_list)
q = None
while q != "-":
    q = input("Если хотите прекратить введите '-', иначе нажмите 'Enter': ")
    print(next(c))