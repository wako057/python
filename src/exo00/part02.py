# coding=utf-8
import random, math
import locale

locale.setlocale(locale.LC_ALL, '')

print("############## Part 2 ##############")

print("============== Exo 3 ==============")
max = 1000000
print("Tableau de 0 a ")
print("{0:n}".format(max).rjust(18))
l = list(range(0, max))

for k in range(0, 10):
    x = random.randint(0, l[-1])

    iter = 0
    a = 0
    b = len(l) - 1
    while a <= b:
        iter += 1
        m = (a + b) // 2
        if l[m] == x:
            position = m
            break
        elif l[m] < x:
            a = m + 1
        else:
            b = m - 1

    print("k=", k, "x=", "{0:n}".format(x).rjust(10, " "), "itération=", iter, " log2(len(l))=", math.log(len(l)) / math.log(2))
