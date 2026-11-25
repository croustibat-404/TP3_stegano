import argparse
import PIL

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
    pass