import csv
import hashlib
def load_user_data(filename: str = 'database.csv') -> dict:
    user_database = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Stocker dans le dictionnaire principal
                username = row['username']
                hashed_pwd = row['password']
                user_database[username] = hashed_pwd
                
        print(f"Chargement de la base de données réussi. {len(user_database)} utilisateurs chargés.")
        return user_database
            
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' est introuvable.")
        return {}
    except KeyError as e:
        print(f"Erreur : Le fichier CSV ne contient pas la colonne {e}. Vérifiez l'en-tête.")
        return {}
    except Exception as e:
        print(f"Une erreur inattendue s'est produite lors de la lecture : {e}")
        return {} 

def hash_password(password: str) -> str:
    """
    Hache un mot de passe en utilisant SHA-256 et retourne sa représentation hexadécimale.
    """
    password_bytes = password.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(password_bytes)
    return hasher.hexdigest()