from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def rsa_encrypt(plaintext, public_key):
    """
    Parameters:
    plaintext (str): message to be encoded
    public_key (RSA.RsaKey): A valid RSA public key 

    Returns:
    ciphertext (binary): encoded message 
    """
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext

# Création des clés RSA 
key = RSA.generate(1024)
public_key_obj = key.publickey()  
phi_n = (key.p - 1) * (key.q - 1)

# Sauvegarde des paramètres
base_dir = os.path.dirname(__file__)
root_path = os.path.dirname(base_dir)
file_path_phi =  os.path.join(root_path, 'utils', 'secrets', 'rsa_phi.txt')
file_path_pem = os.path.join(root_path, 'utils', 'public_key.pem')

# Écriture du pem file et du phi
with open(file_path_phi, "w") as f:
    f.write(str(phi_n))

with open(file_path_pem, 'wb') as f:
    f.write(public_key_obj.export_key())



# Le message doit être très court
plaintext_message = 'o'
encrypted_data = rsa_encrypt(plaintext_message, public_key_obj)


print(f'encrypted_text: {encrypted_data}')
print(f'phi: {phi_n}')