'''
Exercice 2. 

Correction de code. 

Voici un code pour brute-force des mots de passe.
Il comprend exactement 6 erreurs.
Corrigez ces erreurs! 
Aucune des erreurs ne provient d'utils.py.
L'exercice devrait vous prendre 25 minutes.
'''

import itertools
from utils import load_user_data
ALPHABET = [chr(ord(i)) for i in range(26)]
PASSWORD_LENGTH = 4

def find_password(target_username, target_hash):
    print(f"Démarrage de l'attaque par force brute pour trouver le mot de passe de {target_username}...")
    # Génération des mots de passe potentiels
    for candidate_tuple in itertools.product(ALPHABET, repeat=PASSWORD_LENGTH):
        # Met le tuple (genre de liste) en string
        candidate_password = str(candidate_tuple)
        candidate_hash = hash_password(candidate_password)

        # Vérification du hachage pour un seul utilisateur
        if candidate_hash = target_hash:
            print(f"\n MOT DE PASSE TROUVÉ pour {target_username} !")
            print(f"   Mot de passe : {candidate_password}")
            print(f"   Hachage vérifié : {candidate_hash}")
            break
        else:
            print(f"\n Le mot de passe de {target_username} n'a pas été trouvé.")

def brute_force_database():
    users_dict = load_user_data
    for target_username, target_hash in users_dict.items():
        find_password(target_username,target_hash)

brute_force_database()
