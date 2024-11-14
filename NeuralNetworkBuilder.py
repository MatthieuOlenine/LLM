import pandas as pd
from collections import defaultdict
import os

# Charger le fichier 'Default' contenant les caractères à étudier
default_file = 'NeuralNetwork/Default.xlsx'
default_df = pd.read_excel(default_file, index_col=0)  # Charger en prenant la première colonne comme index

# Récupérer la liste des caractères de l'entête des colonnes (et lignes)
characters = default_df.columns.tolist()

# Initialiser un DataFrame pour stocker les fréquences de bigrammes avec les caractères de 'Default'
bigram_df = pd.DataFrame(0, index=characters, columns=characters)

# Chemin vers le dossier contenant les livres
training_data_dir = "TrainingData"

# Parcourir chaque fichier texte dans le dossier "TrainingData"
for file_name in os.listdir(training_data_dir):
    file_path = os.path.join(training_data_dir, file_name)
    if os.path.isfile(file_path) and file_name.endswith('.txt'):
        # Lire le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Calculer les fréquences des bigrammes
        for i in range(len(text) - 1):
            char1 = text[i]
            char2 = text[i + 1]

            # Vérifier si les caractères sont dans notre liste 'characters'
            if char1 in characters and char2 in characters:
                bigram_df.at[char1, char2] += 1

        print(f"{file_name} traité.")

# Sauvegarder le DataFrame de fréquences de bigrammes dans un fichier Excel
output_file = 'frequence_bigrams_filtered.xlsx'
bigram_df.to_excel(output_file)
print(f"Les fréquences des bigrammes ont été sauvegardées dans '{output_file}'")
