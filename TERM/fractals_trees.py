# Dépendances
from ipycanvas import Canvas

# Définitions

# Création du canvas c
c = Canvas(widht=800, lenght=600)

# Une fonction pour effacer la scène et redessiner un background
def background(couleur : str = 'black') :
    '''
    Rafraichit la scène avec un fond de la couleur
    'couleur' passée en paramètre et fixée sur `black` par défaut
    Préconditions :
    - couleur (str) : une chaine de caractères définissant une couleur HTML valide
    '''
    
    c.fill_style = couleur
    c.fill_rect(0, 0, c.width, c.height)

# Tests
if __name__ == '__main__':
    display(c)
    background()

