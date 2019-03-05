import math

print("############## Part 2 ##############")
print("============== Exo 1 ==============")
total = 0
for cpt in range(1, 11):
    square = cpt * cpt
    total += square
    print("Carre de {0}={1}".format (cpt , square))
print("Resultat de la somme {}".format(total))

print("============== Exo 2 ==============")
total = 0
for cpt in range (1, 10):
    if cpt % 2 == 1:
        square = cpt * cpt
        total += square
        print("Carre de {0}: {1}".format(cpt, square))
print("Resultat de la somme {}".format(total))

print("============== Exo 2 ==============")
total = 0
for cpt in range (1, 10):
    factoriel = math.factorial(cpt)
    total += factoriel
    print("Factorielle de {}: {}".format(cpt, factoriel))

print("Resultat de la somme {}".format(total))
