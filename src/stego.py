import argparse
from PIL import Image
import os

def text_to_bits(text):
    bits = []
    for octet in text.encode("utf-8"):
        chaine = format(octet, '08b')
        for c in chaine:
            bits.append(int(c))
    return bits

def bits_to_text(bits):
    resultat = bytearray()
    for i in range(len(bits)//8):
        lettre = ''
        for j in range(8):
            lettre += str(bits[i*8 + j])
        resultat.append(int(lettre,2))
    return resultat.decode('utf-8')

def hide(input_path, output_path, secret):
    bits = []
    octets = secret.encode('utf-8')
    n = len(octets)
    longueur = format(n, '032b')
    for c in longueur : 
        bits.append(int(c))
    bits.extend(text_to_bits(secret))
    img = Image.open(input_path).convert('RGB')
    pixels = list(img.getdata())
    capacite = len(pixels) * 3
    if len(bits) > capacite : 
        raise ValueError(r"/!\ The secret string exceeds the maximum length supported by the image.")
    nouveaux = []
    k = 0
    for (r, g, b) in pixels:
        if k < len(bits):
            r = (r & 0xFE) | bits[k]
            k += 1
        if k < len(bits):
            g = (g & 0xFE) | bits[k]
            k += 1
        if k < len(bits):
            b = (b & 0xFE) | bits[k]
            k += 1
        nouveaux.append((r, g, b))
    dossier = os.path.dirname(output_path)
    if dossier != "":
        os.makedirs(dossier, exist_ok=True)
    new_image = Image.new(mode='RGB', size=img.size)
    new_image.putdata(nouveaux)
    new_image.save(output_path, 'PNG')
    
def reveal(file_path):
    bits = []
    entete = []
    img = Image.open(file_path).convert('RGB')
    pixels = list(img.getdata())
    k = 0
    for (r, g ,b) in pixels:
        if k < 32:
            r = (r & 1)
            