from collections import Counter
import re
import string

def kasiski_examination(ciphertext, min_seq_len=3, max_seq_len=5):
    """
    Perform Kasiski Examination to guess probable key lengths.
    Returns a Counter of distances between repeated sequences.
    """
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())  # keep only letters
    seq_spacings = []

    # Check sequences of length min_seq_len to max_seq_len
    for seq_len in range(min_seq_len, max_seq_len + 1):
        sequences = {}
        for i in range(len(ciphertext) - seq_len):
            seq = ciphertext[i:i + seq_len]
            if seq in sequences:
                prev_index = sequences[seq]
                seq_spacings.append(i - prev_index)
                sequences[seq] = i
            else:
                sequences[seq] = i

    if not seq_spacings:
        return Counter()
    
    # Count divisors of distances
    factor_counts = Counter()
    for spacing in seq_spacings:
        for i in range(2, spacing + 1):
            if spacing % i == 0:
                factor_counts[i] += 1

    return factor_counts.most_common(5)  # top 5 probable key lengths

def split_columns(ciphertext, key_length):
    columns = ['' for _ in range(key_length)]
    for i, c in enumerate(ciphertext):
        columns[i % key_length] += c
    return columns

# --- English letter frequencies ---
english_freq = {
    'A': 0.08167,'B': 0.01492,'C': 0.02782,'D': 0.04253,'E': 0.12702,'F': 0.02228,'G': 0.02015,
    'H': 0.06094,'I': 0.06966,'J': 0.00153,'K': 0.00772,'L': 0.04025,'M': 0.02406,'N': 0.06749,
    'O': 0.07507,'P': 0.01929,'Q': 0.00095,'R': 0.05987,'S': 0.06327,'T': 0.09056,'U': 0.02758,
    'V': 0.00978,'W': 0.02360,'X': 0.00150,'Y': 0.01974,'Z': 0.00074
}

def chi_squared(text):
    text_len = len(text)
    counts = {c: text.count(c) for c in string.ascii_uppercase}
    return sum(((counts[c]/text_len - english_freq[c])**2)/english_freq[c] for c in string.ascii_uppercase)

def find_caesar_shift(column):
    min_chi = float('inf')
    best_shift = 0
    for shift in range(26):
        decrypted = ''.join(chr((ord(c)-65 - shift) % 26 + 65) for c in column)
        score = chi_squared(decrypted)
        if score < min_chi:
            min_chi = score
            best_shift = shift
    return best_shift

# --- Vigenère decryption ---
def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_index = 0
    key_length = len(key)
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            c_val = ord(char) - ord('A')
            k_val = ord(key[key_index % key_length]) - ord('A')
            p_val = (c_val - k_val) % 26
            decrypted_text += chr(p_val + 65)
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text