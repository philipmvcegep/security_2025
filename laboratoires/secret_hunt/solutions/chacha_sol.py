# import modules for file navigation and encryption
from Crypto.Cipher import ChaCha20
import os

# locate where the files were deposited
base_dir = os.path.dirname(__file__)
root_path = os.path.dirname(base_dir)
file_path_cipher =  os.path.join(root_path, 'énoncé', 'ciphers', 'chacha.bin')
file_path_key = os.path.join(root_path, 'énoncé', 'utils', 'secrets', 'chacha_key.bin')
file_path_nonce = os.path.join(root_path, 'énoncé', 'utils', 'secrets', 'chacha_nonce.bin')

# read key, ciphertext and nonce from their binary file
with open(file_path_cipher, 'rb') as f:
    ciphertext = f.read()
with open(file_path_key, "rb") as f:
    key = f.read()
with open(file_path_nonce, "rb") as f:
    nonce = f.read()

# decryption
cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext).decode()
print(f'plaintext: {plaintext}')
