# Dépendances
from ipycanvas import Canvas
from IPython.display import display
from math import pi



# Définitions

# Création du canvas c
c = Canvas(widht=800, lenght=600)

# Une fonction pour effacer le canvas et redessiner un background
def background(couleur : str = 'black') :
    '''
    Rafraichit la scène avec un fond de la couleur
    'couleur' passée en paramètre et fixée sur `black` par défaut
    Préconditions :
    - couleur (str) : une chaine de caractères définissant une couleur HTML valide
    '''
    
    c.fill_style = couleur
    c.fill_rect(0, 0, c.width, c.height)
    
    
    
    
# Une fonction pour dessiner une branche
def branche(longueur : float) :
    '''
    dessine un trait de la longueur passée en paramètre
    et translate l'origine du dessin au bout de cette branche
    Préconditions :
    - longueur (float) : un flottant représentant la longueur de la branche    
    '''
    
    c.line_width = 3
    c.stroke_style = 'red'

    c.stroke_line(0, 0, 0, -longueur)
    c.translate(0, -longueur)
    
    
    
# Tests
if __name__ == '__main__':
    display(c)
    background()
    
    # Changement d'origine au milieu de la base du canvas
    
    c.translate(c.width/2, c.height)
    
    # Réglage de l'épaisseur et de la couleur du trait
        
    c.line_width = 3
    c.stroke_style = 'red'
    
    branche(150) # Tronc

    c.save()
    c.rotate(pi/4)
    branche(150*0.75) # Branche de droite
    c.restore()

    c.save()
    c.rotate(-pi/4)
    branche(150*0.75) # Branche de gauche
    c.restore()
    