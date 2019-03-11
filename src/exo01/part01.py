# coding=utf-8
print("############## Part 1 ##############")
print("============== Exo 1 ==============")

x = 5
y = 10
z = x + y
print(z)  # affiche z
# print("\n\n")

print("============== Exo 2 ==============")

x = 2
y = x + 1
print(y)
x += 5
print(x)

print("============== Exo 3 ==============")
a = 0
for i in range(0, 10):
    a = a + i
print(a)

i = 0
while i < 10:
    print (i)
    i += 1

l = [5, 3, 5, 7]
for v in l:
    print("élément ", v)

print("============== Exo 4 ==============")
a = 10
if a > 0:
    print(a)
else:
    a -= 1
    print(a)

print("============== Exo 5 ==============")
a = 10
print(a)
print("a")
s = "texte"
s += "c"
print(s)

print("2" + "3")
print(2 + 3)
