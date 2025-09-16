import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import math

# Find the right filepath to extract e and n from
def extract_e_n():
    base_dir = os.path.dirname(__file__)
    root_path = os.path.dirname(base_dir)
    file_path_public =  os.path.join(root_path, 'énoncé', 'utils', 'public_key.pem') 

    # Extract e and n from the public key
    public_key = RSA.import_key(open(file_path_public, 'r').read())
    e, n  = public_key.e, public_key.n
    return e, n

# Extract the phi we stored in secrets
def recover_phi():
    base_dir = os.path.dirname(__file__)
    root_path = os.path.dirname(base_dir)
    file_path_phi =  os.path.join(root_path, 'énoncé', 'utils', 'secrets', 'rsa_phi.txt')
    with open(file_path_phi, "r") as f:
        phi = f.read()
    return int(phi)

def recover_p_q(n, phi):
    s = n - phi + 1
    discriminant = s*s - 4*n
    sqrt_disc = math.isqrt(discriminant)
    if sqrt_disc*sqrt_disc != discriminant:
        raise ValueError("Discriminant is not a perfect square – check phi or n")
    p = (s + sqrt_disc) // 2
    q = (s - sqrt_disc) // 2
    if p <= 0 or q <= 0:
        raise ValueError("Computed primes are invalid")
    return p, q

def recover_cybertext():
    base_dir = os.path.dirname(__file__)
    root_path = os.path.dirname(base_dir)
    file_path_ct =  os.path.join(root_path, 'énoncé', 'ciphers', 'rsa.txt')
    with open(file_path_ct, "rb") as f:
        ciphertext = f.read()
    return ciphertext


# Extended euclidian algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

def main():
    e, n = extract_e_n()
    e = int(e)
    print(f'e: {e}, \nn: {n},')
    phi = recover_phi()
    d = modinv(e, phi)
    print(f'phi: {phi}, \nd: {d}')

    # safe method to find p,q from n and phi
    p, q = recover_p_q(n, phi)    
    key = RSA.construct((n, e, d, p, q))

    #lazy me I'm tired of making paths
    ciphertext = recover_cybertext()
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext)
    print(f"Le message codé est {plaintext.decode('utf-8')}")

main()