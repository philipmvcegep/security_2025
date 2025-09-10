import requests
from bs4 import BeautifulSoup

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_index = 0
    plaintext = plaintext.upper()
    key = key.upper()
    key_length = len(key)

    for char in plaintext:
        if 'A' <= char <= 'Z':
            p_val = ord(char) - ord('A')
            k_val = ord(key[key_index % key_length]) - ord('A')
            c_val = (p_val + k_val) % 26
            encrypted_text += chr(c_val + ord('A'))
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

url = "https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    raise Exception(f"Failed to fetch page: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
# Extract the main content text
content = soup.find("div", {"class": "mw-parser-output"})
text = ""
for paragraph in content.find_all("p"):
    text += paragraph.get_text() + " "

import re
text = re.sub(r'[^A-Za-z ]', '', text)


key = "EXEMPLE"
ciphertext = vigenere_encrypt(text, key)
print(f"Encrypted text (first 500 chars):\n{ciphertext[:500]}")