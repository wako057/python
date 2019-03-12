# coding=utf-8
print("############## Part 1 ##############")

print("============== Exo 3 ==============")
a = 0
for i in range(0, 10):
    a = a + i
print(a)

i = 0
while i < 10:
    print(i)
    i += 1

l = [5, 3, 5, 7]
for v in l:
    print("élément ", v)

for i in range(0, 10):
    if i == 2:
        continue  # on passe directement au suivant
    print (i)
    if i > 5:
        break  # interruption définitive

print("============== Exo 4 ==============")
l = []
for i in range(10):
    l.append(i * 2 + 1)
print(l)

print("============== Exo 5 ==============")
l = [i * 2 + 1 for i in range(10)]
print(l)

print("============== Exo 6 ==============")
l = [i * 2 for i in range(0, 10)]
print(l)

print("============== Exo 7 ==============")
l = [i * 2 for i in range(0, 10) if i % 2 == 0]
print(l)

print("============== Exo 8 ==============")
l = ["a", "b", "c", "a", 9, 4, 5, 6, 7, 4, 5, 9.0]
s = set(l)
print(s)

print("============== Exo 9 ==============")
l = [3, 6, 2, 7, 9]
x = 7

position = l.index(x)
print(l);
print(position)

print("============== Exo 10 ==============")
unsortedList = [4, 7, -1, 3, 9, 5, -5]
print("Unsorted list", unsortedList)
l = sorted(unsortedList)
print("Sorted List: ", l)
def recherche_dichotomique(element, liste_triee):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element:
            return m
        elif liste_triee[m] > element:
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

print("On recherche le 5: ", recherche_dichotomique(5, l))


print("============== Exo 11 ==============")
li = [0, 4, 5, 19, 100, 200, 450, 999]
print("Sorted List: ", li)
def recherche_dichotomique_recursive( element, liste_triee, a = 0, b = -1 ):
    if a == b :
        return a
    if b == -1 :
        b = len(liste_triee)-1
    m = (a+b)//2
    if liste_triee[m] == element:
        return m
    elif liste_triee[m] > element:
        return recherche_dichotomique_recursive(element, liste_triee, a, m-1)
    else:
        return recherche_dichotomique_recursive(element, liste_triee, m+1, b)
# recherche_dichotomique(20, li)
print("On recherche le 0: ", recherche_dichotomique(0, li))
print("On recherche le 1: ", recherche_dichotomique(1, li))
print("On recherche le 2: ", recherche_dichotomique(2, li))
print("On recherche le 3: ", recherche_dichotomique(3, li))
print("On recherche le 4: ", recherche_dichotomique(4, li))
print("On recherche le 5: ", recherche_dichotomique(5, li))
print("On recherche le 19: ", recherche_dichotomique(19, li))
print("On recherche le 20: ", recherche_dichotomique(20, li))
print("On recherche le 100: ", recherche_dichotomique(100, li))
print("On recherche le 300: ", recherche_dichotomique(300, li))
print("On recherche le 400: ", recherche_dichotomique(400, li))
print("On recherche le 450: ", recherche_dichotomique(450, li))
print("On recherche le 451: ", recherche_dichotomique(451, li))
print("On recherche le 998: ", recherche_dichotomique(998, li))
print("On recherche le 999: ", recherche_dichotomique(999, li))
print("On recherche le 1000: ", recherche_dichotomique(1000, li))

# a = 10
# if a > 0:
#     print(a)
# else:
#     a -= 1
#     print(a)
#
# print("============== Exo 5 ==============")
# a = 10
# print(a)
# print("a")
# s = "texte"
# s += "c"
# print(s)
#
# print("2" + "3")
# print(2 + 3)
