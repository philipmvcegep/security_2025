import random

numbers = [str(i) for i in range(10)]
alphabet = [chr(ord('a') + i) for i in range(26)]
S_BOX = dict(zip(numbers, random.sample(alphabet, 10)))

# dictionnaire inverse
INV_S_BOX = {v: str(k) for k, v in S_BOX.items()}

def sub_values(text, dictio):
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
    stage2 = fake_chacha(ciphertext, 7)
    stage1 = caesar(stage2, -2)
    plainnumber = sub_values(stage1, INV_S_BOX)
    return plainnumber

def main():
    SSN = 145687234
    cipher = encrypt_text(str(SSN))
    print("Ciphertext:", cipher)
    plain = decrypt_text(cipher)
    print("Decrypted :", plain)

if __name__ == "__main__":
    main()