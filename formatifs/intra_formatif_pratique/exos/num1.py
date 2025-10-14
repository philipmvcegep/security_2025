'''
Exercice 1.

Pour cet exercice, vous devez inverser le chiffrement d'un algo comportant 3 transformations au texte.
Vous devez seulement changer main et decrypt_text pour y arriver.
L'exercice devrait prendre environ 25 minutes.
'''

import random

numbers = [str(i) for i in range(10)]
alphabet = [chr(ord('a') + i) for i in range(26)]
S_BOX = dict(zip(numbers, random.sample(alphabet, 10)))

# dictionnaire inverse
INV_S_BOX = {v: str(k) for k, v in S_BOX.items()}

def sub_values(text, dictio):
    '''
    Args:
        text (str): le texte à substituer
        dictio (dict): le dictionnaire sur lequel on se base

    Returns:
        subbed_text (str): le texte substitué
    '''
    subbed_text = ''
    for digit in text:
        subbed_text += dictio[digit]
    return subbed_text


def caesar(text, shift=2):
    out = ""
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            out += chr((ord(ch) - base + shift) % 26 + base)
        else:
            out += ch
    return out

def fake_chacha(text, key=7):
    return ''.join(chr(ord(c) ^ key) for c in text)

def encrypt_text(plainnumber):
    stage1 = sub_values(plainnumber, S_BOX)
    stage2 = caesar(stage1, 2)
    ciphertext = fake_chacha(stage2, 7)
    return ciphertext

def decrypt_text(ciphertext):
    # implémentez la fonction pour revenir au texte original
    # return plainnumber
    pass

def main():
    SSN = 145687234
    cipher = encrypt_text(str(SSN))
    print("Ciphertext:", cipher)
    
    # plain = decrypt_text(cipher)
    # print("Decrypted :", plain)

if __name__ == "__main__":
    main()



