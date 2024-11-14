import pandas as pd
import random

#df = pd.read_excel('NeuralNetwork/Default.xlsx', index_col=0)
df = pd.read_excel('NeuralNetwork/Corrected.xlsx', index_col=0)
caracteres_valides = df.columns.tolist()

def generer_texte(depart, longueur):
    texte = depart
    if depart not in caracteres_valides:
        raise ValueError(f"Le caractère de départ '{depart}' n'est pas valide.")
    
    for _ in range(longueur - 1):
        dernier_char = texte[-1]
        if dernier_char not in df.index:
            break
        
        frequences_suivantes = df.loc[dernier_char]
        frequences_suivantes = frequences_suivantes[frequences_suivantes > 0]
        
        if frequences_suivantes.empty:
            break
        
        suivant = random.choices(
            population=frequences_suivantes.index,
            weights=frequences_suivantes.values,
            k=1
        )[0]
        
        texte += suivant
    
    print("Texte généré :", texte)

# Générer le texte
generer_texte('c', 1000)
