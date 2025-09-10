from Crypto.Cipher import ChaCha20
import os

# Ce ne sont pas les bonnes valeurs
plaintext = b"Bonjour les amis"
key = os.urandom(32)
nonce = os.urandom(12)

# Objet cipher
cipher = ChaCha20.new(key=key, nonce=nonce)
ciphertext = cipher.encrypt(plaintext)

# trouver le répertoire dans lequel écrire
base_dir = os.path.dirname(__file__)
root_path = os.path.dirname(base_dir)
file_path_key =  os.path.join(root_path, 'utils', 'secrets', 'chacha_key.bin')
file_path_nonce =  os.path.join(root_path, 'utils', 'secrets', 'chacha_nonce.bin')
file_path_cipher =  os.path.join(root_path, 'ciphers', 'chacha.bin')

with open(file_path_key, "wb") as f:
    f.write(key)

with open(file_path_nonce, "wb") as f:
    f.write(nonce)

with open(file_path_cipher, "wb") as f:
    f.write(ciphertext)

