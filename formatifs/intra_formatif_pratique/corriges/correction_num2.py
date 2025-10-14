import itertools
from utils import load_user_data, hash_password ## erreur 1: il faut importer hash_password
ALPHABET = [chr(ord('a')+ i) for i in range(26)] ## erreur 2: on bâtit les minuscules à partir de 'a'
PASSWORD_LENGTH = 4

def find_password(target_username, target_hash):
    print(f"Démarrage de l'attaque par force brute pour trouver le mot de passe de {target_username}...")
    for candidate_tuple in itertools.product(ALPHABET, repeat=PASSWORD_LENGTH):
        candidate_password = "".join(candidate_tuple) ## erreur 6 - la plus difficile. ''.join() au lieu de str() comme c'est un tuple.
        candidate_hash = hash_password(candidate_password)

        if candidate_hash == target_hash: ## erreur 3: == 
            print(f"\n MOT DE PASSE TROUVÉ pour {target_username} !")
            print(f"   Mot de passe : {candidate_password}")
            print(f"   Hachage vérifié : {candidate_hash}")
            break
    else: ## erreur 4: seulement print à la fin de la boucle
        print(f"\n Le mot de passe de {target_username} n'a pas été trouvé.")

def brute_force_database():
    users_dict = load_user_data() ## erreur 5: il faut toujours appeller les fonctions avec des parenthèses.
    for target_username, target_hash in users_dict.items():
        find_password(target_username,target_hash)

brute_force_database()
