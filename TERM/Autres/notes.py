def demander_entier_V2(message : str) -> int :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur un nombre correspondant à la question du message et renvoie le résultat au format entier ;
                > avec une gestion de vérification de la validité de la saisie utilisateur.
                        
        * Exemple :
            >>> demander_entier("Combien de notes sont à saisir ? ")
            Combien de notes sont à saisir ? 5
            5
                                           
        * Préconditions :
            message (str) : question définissant le nombre à saisir ;
                    
        * Postconditions :
            (int) : la valeur saisie convertie en entier.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(message) == str  , "L'argument message doit être une chaine de caractères."
            
    # bloc d'instructions :
    try :
        nombre = int(input(message))
        return nombre
    except ValueError :
        print("La valeur saisie doit être convertible en un nombre entier exprimé en base 10 : \n    -> la saisie ne doit pas contenir d'autres caractères que 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")



def saisir_note() -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur une note comprise entre 0.0 et 20.0 et renvoie le résultat au format flottant ;
                > avec une gestion de vérification de la validité de la saisie utilisateur.
                        
        * Exemple :
            >>> saisir_note()
            Saisir une note comprise entre 0.0 et 20.0 : 5
            5.0
                                           
        * Préconditions :
            
                    
        * Postconditions :
            (float) : la valeur de la note saisie convertie en float.       
        
        ==================================================================================================================
    """
    
    # bloc d'instructions :
    try :
        saisie = input(f"Saisir une note comprise entre 0.0 et 20.0 : ")
        saisie.replace(',','.') # prévoir de remplacer le séparateur décimal au cas où ...
        note = float(saisie)
        if note <= 0.0 or note >= 20.0 :
            raise ValueError
        return note
    
    except ValueError :
        print(f"La valeur saisie doit être un nombre entier ou décimal suppérieur ou égal à 0.0 et inférieur ou égal à 20.0.")
saisir_note()




def minimum_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je recherche et renvoie la valeur min d'un tableau de valeurs.
        
        * Exemple :
            >>> minimum_table([5.0, 19.0, 11.0, -1.1])
            -1.1
                                           
        * Préconditions :
            valeurs (list) : tableau des valeurs à traiter ;
                    
        * Postconditions :
            (float) : la valeur mini de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(valeurs) == list,"l'argument valeurs doit être de type list"
    
    # bloc d'instructions :
    min = valeurs[0]
    for k in valeurs :
        if k < min :
            min = k
    return min

if __name__ == '__main__' :
    minimum_table([5.0, 19.0, 11.0, -1.1])



def maximum_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je recherche et renvoie la valeur max d'un tableau de valeurs.
        
        * Exemple :
            >>> maximum_table([5.0, 19.0, 11.0, -1.1])
            19.0
                                           
        * Préconditions :
            valeurs (list) : tableau des valeurs à traiter ;
                    
        * Postconditions :
            (float) : la valeur maxi de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(valeurs) == list,"l'argument valeurs doit être de type list"    
    
    # bloc d'instructions :
    max = valeurs[0]
    for j in valeurs :
        if j > max :
            max = j
    return max

if __name__ == '__main__' :
    maximum_table([5.0, 19.0, 11.0, -1.1])




def moyenne_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description : 
            Je calcule et renvoie la valeur moyenne d'un tableau de valeurs.
        
        * Exemple :
            >>> moyenne_table([5.0, 19.0, 11.0, -1.1])
            8.475
        
        * Préconditions :
            valeurs (list) : tableau des valeurs à traiter ;        
                    
        * Postconditions :
            (float) : la valeur moyenne de la liste d'entrée.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(valeurs) == list,"l'argument valeurs doit être de type list"
    
    # Instructions
    total = 0
    for v in valeurs :
        total += v
    return total/len(valeurs)

if __name__ == '__main__' :
    moyenne_table([5.0, 19.0, 11.0, -1.1])