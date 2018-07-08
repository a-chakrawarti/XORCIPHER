from operator import xor
import string
from binary import dec2bin
import base64
import random

key = list()
key_ascii = list()
key_bool = list()
ct_element = list()
pt_element = list()

def encrypt(plaintext):
    """Enter the message to be encrypted."""
    key_binary = list()
    pt_binary = list()
    ciphert = []
    ciphertext = []
    ct_binary = list()
    pt_len = len(plaintext)

    key = ''.join(random.choice(string.ascii_lowercase) for n in range(pt_len))  # Generation of Key

    for i in plaintext:
        pt_ascii = ord(i)
        pt_bool = dec2bin(pt_ascii)
        pt_binary.append(pt_bool)
    for i in key:
        key_ascii = ord(i)
        key_bool = dec2bin(key_ascii)
        key_binary.append(key_bool)

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

    for i in key:
        key_ascii = ord(i)
        key_bool = dec2bin(key_ascii)
        key_binary.append(key_bool)

    # Conversion of base64 into String
    ciphertext = base64.b64decode(ciphertext)
    ciphertext = ciphertext.decode()

    for i in ciphertext:
        ct_ascii = ord(i)
        ct_bool = dec2bin(ct_ascii)
        ct_binary.append(ct_bool)

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

# Calls

plaintext = input("Enter the message : ")
encrypt(plaintext)
while True:
    choice = input('\nWould you like to decrypt any messages ? (Y/N) ')
    if choice == 'N' or choice == 'n':
        break
    elif choice == 'Y' or choice == 'y':
        key = input("Enter Key : ")
        ciphertext = input("Enter Ciphertext : ")
        decrypt(key, ciphertext)
        break
    else:
        print('Enter valid choice !\n')
