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

def xoring(xt_binary,key_binary):       # XOR of cipher/plain text with key during encryption/decryption
    final_binary=[]
    xt=[]
    for i in range(0, len(xt_binary)):
        xt_list=list()
        for j in range(0, len(xt_binary[i])):
            xt_element = xor(int(xt_binary[i][j]), int(key_binary[i][j]))
            xt_element = str(xt_element)
            xt_list.append(xt_element)
        xt_list = ''.join(xt_list)
        final_binary.append(xt_list)
        del xt_list

    for i in final_binary:
        val = int(i, 2)
        char = chr(val)
        xt.append(char)
        text = ''.join(xt)
    return text

def encrypt(plaintext):
    """Enter the message to be encrypted."""
    key_binary = list()
    pt_binary = list()
    ciphertext = []
    pt_len = len(plaintext)

    key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(pt_len))  # Generation of Key

    pt_binary = stringtobinary(plaintext)
    key_binary = stringtobinary(key)
    
    ciphertext = xoring(pt_binary,key_binary)

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

    plaintext = xoring(ct_binary,key_binary)

    print('Plaintext :', plaintext)



method = argv[1]

if method == '-encrypt':
    plaintext = input("Enter the message : ")
    encrypt(plaintext)

elif method == '-decrypt':
    key = input("Enter Key : ")
    ciphertext = input("Enter Ciphertext : ")
    decrypt(key, ciphertext)

elif (method != '-encrypt') or (method != '-decrypt'):
    _help_ = '''
    > Enter valid argument :
    \t-encrypt : To encrypt plaintext.
    \t-decrypt : To decrypt ciphertext provided correct key.
    '''
    print(_help_)
