# -*- coding: utf-8 -*-

def recherche_dichotomique( element, liste_triee ):
    a = 0
    b = len(liste_triee)-1
    m = (a+b)//2
    while a < b :
        if liste_triee[m] == element :
            return m
        elif liste_triee[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a

def recherche_dichotomique_recursive( element, liste_triee, a = 0, b = -1 ):
    if a == b :
        return a
    if b == -1 :
        b = len(liste_triee)-1
    m = (a+b)//2
    if liste_triee[m] == element :
        return m
    elif liste_triee[m] > element :
        return recherche_dichotomique_recursive(element, liste_triee, a, m-1)
    else :
        return recherche_dichotomique_recursive(element, liste_triee, m+1, b)


def recherche_dichotomique_recursive2(element, liste_triee):
    if len(liste_triee)==1 :
        return 0
    m = len(liste_triee)//2
    if liste_triee[m] == element :
        return m
    elif liste_triee[m] > element :
        return recherche_dichotomique_recursive2(element, liste_triee[:m])
    else :
        return m + recherche_dichotomique_recursive2(element, liste_triee[m:])

