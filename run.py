from operator import xor
import string
from binary import dec2bin
import base64
import random
from sys import argv

key = list()
key_ascii = list()
key_bool = list()
ct_element = list()
pt_element = list()

def stringtobinary(xt):
    xt_binary = []
    for i in xt:
        xt_ascii = ord(i)
        xt_bool = dec2bin(xt_ascii)
        xt_binary.append(xt_bool)
    return xt_binary

def encrypt(plaintext):
    """Enter the message to be encrypted."""
    key_binary = list()
    pt_binary = list()
    ciphert = []
    ciphertext = []
    ct_binary = list()
    pt_len = len(plaintext)

    key = ''.join(random.choice(string.ascii_lowercase) for n in range(pt_len))  # Generation of Key

    pt_binary = stringtobinary(plaintext)
    key_binary = stringtobinary(key)

    for i in range(0, len(pt_binary)):
        ct_list = list()
        for j in range(0, len(pt_binary[i])):
            ct_element = xor(int(pt_binary[i][j]), int(key_binary[i][j]))
            ct_element = str(ct_element)
            ct_list.append(ct_element)
        ct_list = ''.join(ct_list)
        ct_binary.append(ct_list)
        del (ct_list)

    for i in ct_binary:
        val = int(i, 2)
        char = chr(val)
        ciphert.append(char)
        ciphertext = ''.join(ciphert)

    ciphertext = ciphertext.encode()
    ciphertext = base64.b64encode(ciphertext)
    ciphertext = ciphertext.decode()

    print('Key :', key)
    print('Ciphertext :', ciphertext)

    del (plaintext, key, ciphertext, pt_binary)


def decrypt(key, ciphertext):
    """Enter key and encrypted message"""
    plaint = list()
    key_binary = list()
    ct_binary = list()
    pt_binary = list()

    # Conversion of base64 into String
    ciphertext = base64.b64decode(ciphertext)
    ciphertext = ciphertext.decode()

    ct_binary = stringtobinary(ciphertext)
    key_binary = stringtobinary(key)


    for i in range(0, len(ct_binary)):
        pt_list = list()
        for j in range(0, len(ct_binary[i])):
            pt_element = xor(int(ct_binary[i][j]), int(key_binary[i][j]))
            pt_element = str(pt_element)
            pt_list.append(pt_element)
        pt_list = ''.join(pt_list)
        pt_binary.append(pt_list)
        del pt_list

    del ct_binary

    for i in pt_binary:
        val = int(i, 2)
        char = chr(val)
        plaint.append(char)
        plaintext = ''.join(plaint)

    print('Plaintext :', plaintext)

script, method = argv

if method == '-encrypt':
    plaintext = input("Enter the message : ")
    encrypt(plaintext)

elif method == '-decrypt':
    key = input("Enter Key : ")
    ciphertext = input("Enter Ciphertext : ")
    decrypt(key, ciphertext)

elif (method != '-encrypt') or (method != '-decrypt'):
    help = '''
    > Enter valid argument :
    \t-encrypt : To encrypt plaintext.
    \t-decrypt : To decrypt ciphertext provided correct key.
    '''
    print(help)