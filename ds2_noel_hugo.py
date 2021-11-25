#METHODE POO

#CLASSE PILE

class Pile:

    '''classe Pile création d’une instance Pile avec une liste'''
    
    def __init__(self):
        '''Initialise une pile vide'''
        self.liste = []
        
    def est_vide(self):
        '''Renvoie un booléen, True si la pile est vide et False sinon'''
        return len(self.liste) == 0

    def empiler(self, element):
        '''Empile element au sommet de pile'''
        self.liste.append(element)

    def depiler(self):
        '''Renvoie et enlève la valeur du sommet de pile'''
        return self.liste.pop()

    def __repr__(self):
        return repr(self.liste)



# EXERCICE 1 : FONCTION SOMMET

def sommet(pile):
    
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    
    sommet = ""
    if not pile.est_vide() :
        sommet = pile.depiler()
        pile.empiler(sommet)
        return sommet
    else :
        raise IndexError('pile vide')   



# IMPLEMENTATION POUR L'EXERCICE 1

p = Pile()
sommet(p)
p.empiler(4)
p.empiler(2)
sommet(p)



# EXERCICE 2 : FONCTION METTRE_DISQUES()

def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for i in range(n, 0, -1) :
        pile.empiler(i)  



# IMPLEMENTATION POUR L'EXERCICE 2

p1 = Pile()
mettre_disques(p1,5)
print(p1)



# EXERCICE 3 : FONCTION CREATION_TOURS() :

def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''

    liste = [Pile() , Pile(), Pile()]

    mettre_disques(liste[0], n)

    return liste



# IMPLEMENTATION POUR L'EXERCICE 3

tours = creation_tours(5)
print(tours)







# AUTRE METHODE 

def creer_pile():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie un booléen, True si la pile est vide et False sinon'''
    return p == []

def empiler(pile, element):
    '''Empile element au sommet de pile'''
    pile.append(element)
    
def depiler(pile):
    '''Renvoie et enlève la valeur du sommet de pile'''
    assert not est_vide(pile), "Pile vide"
    return pile.pop()
