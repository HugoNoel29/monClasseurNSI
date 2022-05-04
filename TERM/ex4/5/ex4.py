class Cellule():
   def __init__(self, valeur, suivante = None):
    self.valeur = valeur
    self.suivante = suivante # type Cellule, None par défaut

def cercle(n : int) -> Cellule :
    first = Cellule(n)
    last = first
    for i in range(n-1, 0, -1) :
        first = Cellule(i, first)
    last.suivante = first
    return first

def nieme(prem, n) :
    # prem = cellule n°1
    # n = nombre de cellules à décaler

    for _ in range(n-1) :
        prem = prem.suivante

    return prem

def eliminer(cell) :
    
    # Cellule suivante
    apresCell = cell.suivante
    
    #Cellule précédente
    avantCell = cell.suivante
    while True :
        avantCell = avantCell.suivante
        if avantCell.suivante.valeur == cell.valeur :
            break

    # Supprime la cellule
    avantCell.suivante = apresCell

    return apresCell.valeur

def josephus(cercle, m) :

    cercle = nieme(cercle,m)
    print(cercle.valeur)
    eliminer(cercle)

    while cercle.valeur != cercle.suivante.valeur :

        cercle = nieme(cercle,m+1)
        print(cercle.valeur)
        eliminer(cercle)

if __name__ == '__main__':
    c = cercle(7)
    josephus(c, 3)