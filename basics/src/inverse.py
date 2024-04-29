def inverse(chaine) : 
    if isinstance(chaine,int) : #teste le type de la réponse en étant pas un integer
        raise ValueError ("Vous devez passer une chaîne de caractères")
    
    for element in chaine : #teste que chaque élément soit un caractère
        if not isinstance(element, str):
            raise ValueError("Vous devez passer une chaîne de caractères")
        
    if len(chaine) == 4 and isinstance(chaine,list): #demande que la chaine soit = 4 éléments et soit une liste
        chaine.pop() #les chaines de caractères n'ont pas de méthode pop
        
    chaine = "".join(chaine)

    return chaine [::-1]

if __name__ == "__main__": #name = variable cachée de python #(s'execute si on importe le code directement) 
#(importer le fichier c'est l'éxécuter) si on l'exécute via un import, la variable prend le nom du fichier)
# permet d'exécuter le code que quand le fichier inverse est exécuté directement, s'il est importé, il ne s'exécute pas
    print (inverse(["a","b", "c", "d"]))
