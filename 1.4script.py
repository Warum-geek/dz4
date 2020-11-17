from sys import argv

script_name, production, rate, prize = argv

result = (int(production) * int(rate)) + int(prize)
print("Заработная плата сотрудника составила: {0}".format(result))