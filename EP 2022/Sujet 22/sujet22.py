#EXERCICE 1

def reverse(chaine : str) -> str :
    """
    Prend une chaine de caractères et en renvoie l'inverse
    Exemple : >>> reverse("informatique")
              >>> "euqitamrofni"
    """
    assert type(chaine) == str, "Le paramètre en entrée doit être une chaine de carctères"

    inverse = ""
    for i in range(1, len(chaine) + 1) :
        inverse += chaine[-i]
    return inverse


def reverse_slice(chaine : str) -> str :
    """
    Prend une chaine de caractères et en renvoie l'inverse
    Exemple : >>> reverse_slice("informatique")
              >>> "euqitamrofni"
    """
    assert type(chaine) == str, "Le paramètre en entrée doit être une chaine de carctères"

    return chaine[::-1]


def autre_reverse(chaine : str) -> str :
    """
    Prend une chaine de caractères et en renvoie l'inverse
    Exemple : >>> autre_reverse("informatique")
              >>> "euqitamrofni"
    """
    assert type(chaine) == str, "Le paramètre en entrée doit être une chaine de carctères"

    inverse = ""
    for i in range(len(chaine)) :
        inverse = chaine[i] + inverse
    return inverse


def reverse_recursif_slice(chaine : str) -> str :
    """
    Prend une chaine de caractères et en renvoie l'inverse
    Exemple : >>> reverse_recursif_slice("informatique")
              >>> "euqitamrofni"
    """
    assert type(chaine) == str, "Le paramètre en entrée doit être une chaine de carctères"

    if len(chaine) == 0 :
        return ""
    else :
        return chaine[-1] + reverse_recursif_slice(chaine[:-1])


#EXERCICE 2

def crible(N : int) -> list :
    """
    Renvoie un tableau contenant tout les nombres premiers plus petits que N

    Exemple : >>> crible(40)
              >>> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    """
    assert type(N) == int, "L'entrée doit être de type int"

    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False

    for i in range(2, N) :
        if tab[i] == True :
            premiers.append(i)
            for multiples in range(2*i, N, i) :
                tab[multiples] = False
    return premiers



#TEST
if __name__ == '__main__' :
    assert reverse("informatique") == "euqitamrofni"
    assert reverse_slice("informatique") == "euqitamrofni"
    assert autre_reverse("informatique") == "euqitamrofni"
    assert reverse_recursif_slice("informatique") == "euqitamrofni"

    assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
