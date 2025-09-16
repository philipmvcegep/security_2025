import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'énoncé', 'utils')))

from utils import (
    kasiski_examination,
    split_columns,
    find_caesar_shift,
    vigenere_decrypt
)


# Etape 1: definir le chemin vers le ciphertext
base_dir = os.path.dirname(__file__)
root_path = os.path.dirname(base_dir)
ciphertext_file_path =  os.path.join(root_path, 'énoncé', 'ciphers', 'vigenere.txt')

with open(ciphertext_file_path, "r") as f:
    ciphertext = f.read()


# Etape 2: transformer en majuscules et enlever les caracteres speciaux
import re
ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())  


# Etape 3: trouver la longueur de la cle avec l'examination de Kasiki
probable_key_lengths = kasiski_examination(ciphertext)
print("Longueurs de cle probables (top 5):", probable_key_lengths)
if not probable_key_lengths:
    raise ValueError("La longueur de la cle ne peut pas etre trouvee avec Kasiki.")

key_length_guess = probable_key_lengths[0][0]


# Etape 4: Utiliser l'analyse de frequence pour trouver la cle
columns = split_columns(ciphertext, key_length_guess)
key = ''
for i, column in enumerate(columns):
    shift = find_caesar_shift(column)
    key += chr(65 + shift) 

print(f"Cle trouve (longueur {key_length_guess}): {key}")


# Etape 5: dechiffrement avec vigenere avec la cle trouvee
plaintext = vigenere_decrypt(ciphertext, key)


# Etape 6: Montrer le header du wiki 
print("\n Voici le message dechiffre: ")
print(plaintext[:1000])
