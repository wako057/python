# coding=utf-8
print("############## Part 1 ##############")
print("============== Exo 1 ==============")
i = 3                    # entier = type numérique (type int)
r = 3.3                  # réel   = type numérique (type float)
s = "exemple"            # chaîne de caractères = type str (exemple n'est pas une variable)
s = 'exemple'            # " et ' peuvent être utilisées pour définir une chaîne de caractères
sl = """ exemple sur
plusieurs lignes"""      # on peut définir une chaîne sur plusieurs lignes avec """ ou '''
n = None                 # None signifie que la variable existe mais qu'elle ne contient rien
# elle est souvent utilisée pour signifier qu'il n'y a pas de résultat
# car... une erreur s'est produite, il n'y a pas de résultat
# (racine carrée de -1 par exemple)
i,r,s,n, sl              # avec les notebooks, le dernier print n'est pas nécessaire, il suffit d'écrire
# i,r,s,n
v = "anything"       # affectation
print ( v )          # affichage
v1, v2 = 5, 6        # double affectation
print (v1,v2)
x,y = 4,5
s = "addition"
print("{3} de {0} et {1} donne : {0} + {1} = {2}".format (x,y,x+y,s))

for prenom in [ "xavier", "sloane"] :
    print ("Monsieur {0}, vous avez gagné...".format(prenom))

print( type ( v ) )           # affiche le type d'une variable
print( isinstance (v, str) )  # pour déterminer si v est de type str

print("Liste / Tableau")
c  = (4,5)                # couple de valeurs (ou tuple)
l  = [ 4, 5, 6.5]         # listes de valeurs ou tableaux
x  = l [0]                # obtention du premier élément de la liste l
y  = c [1]                # obtention du second élément
le = [ ]                  # un tableau vide
print(c,l,x,y,le)

l  = [ 4, 5 ]
l += [ 6 ]      # ajouter un élément
l.append ( 7 )  # ajouter un élément
l.insert (1, 8) # insérer un élément en seconde position
print(l)
del l [0]       # supprimer un élément
del l [0:2]     # supprimer les deux premiers éléments
print(l)
