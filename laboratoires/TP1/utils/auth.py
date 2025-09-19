import csv
import hashlib
import os

# Charger les mots de passe depuis un fichier CSV
def load_csv(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # strip des clés et des valeurs
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            data.append(clean_row)
    return data

# Hash avec sel
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    return hashed, salt

# Vérification login
# Utiliser mode = 'password_only' et users_db = load_csv('../data/passwords_plain.csv')).
# Vous pouvez modifier cette fonction pour vos nouveaux csv au besoin.
def check_login(username, password, users_db, mode):
    user_record = next((u for u in users_db if u['username'] == username), None)
    if not user_record:
        return False
    # Cas mot de passe en clair
    if mode == 'password_only':
        return password == user_record['password']
    
    # Cas mot de passe hashé sans sel
    elif mode == 'hash_mode':
        return hashlib.sha256(password.encode()).hexdigest() == user_record['hash']
    
    # Cas mot de passe hashé avec sel
    elif mode == 'salty_hash':
        salt = bytes.fromhex(user_record['salt'])
        hashed = hashlib.sha256(salt + password.encode()).hexdigest()
        return hashed == user_record['hash']
    return False