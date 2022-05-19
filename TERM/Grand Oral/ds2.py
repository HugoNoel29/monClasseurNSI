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


def sommet(pile):
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    if pile.est_vide():
        raise IndexError('pile vide')
    else:
        valeur = pile.depiler()
        pile.empiler(valeur)
    return valeur


def mettre_disques(pile, n):
    for i in range(n, 0, -1):
        pile.empiler(i)


def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    p0 = Pile()
    p1 = Pile()
    p2 = Pile()
    mettre_disques(p0, n)
    return [p0, p1, p2]


def deplacer(tours, origine, cible):
    p0 = tours[origine]
    p1 = tours[cible]
    if not p0.est_vide():
        if p1.est_vide() or sommet(p1) > sommet(p0):
            p1.empiler(p0.depiler())


def resoudre(tours, n, origine, cible, interm):
    if n == 1:
        deplacer(tours, origine, cible)
    else:
        resoudre(tours, n-1, origine, interm, cible)
        deplacer(tours, origine, cible)
        resoudre(tours, n-1, interm, cible, origine)


def nb_etapes(n):
    if n == 1:
        return 1
    else:
        return 2*nb_etapes(n-1) + 1