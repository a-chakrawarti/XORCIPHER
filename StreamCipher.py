from operator import xor
import string
from binary import bin as ibin
import base64
import random

key = list()
key_ascii = list()
key_bool = list()

cT_element = list()
pT_element = list()


def encrypt(plainText):
    """Enter the message to be encrypted."""
    key_binary = list()
    pT_binary = list()
    cipherT = []
    cipherText = []
    cT_binary = list()
    pT_len = len(plainText)

    key = ''.join(random.choice(string.ascii_lowercase) for n in range(pT_len))  # Generation of Key

    for i in plainText:
        pT_ascii = ord(i)
        pT_bool = ibin(pT_ascii)
        pT_binary.append(pT_bool)
    for i in key:
        key_ascii = ord(i)
        key_bool = ibin(key_ascii)
        key_binary.append(key_bool)

    for i in range(0, len(pT_binary)):
        cT_list = list()
        for j in range(0, len(pT_binary[i])):
            cT_element = xor(int(pT_binary[i][j]), int(key_binary[i][j]))
            cT_element = str(cT_element)
            cT_list.append(cT_element)
        cT_list = ''.join(cT_list)
        cT_binary.append(cT_list)
        del (cT_list)

    for i in cT_binary:
        val = int(i, 2)
        char = chr(val)
        cipherT.append(char)
        cipherText = ''.join(cipherT)

    cipherText = cipherText.encode()
    cipherText = base64.b64encode(cipherText)
    cipherText = cipherText.decode()

    #print('PlainTEXT :', plainText)
    print('Key :', key)
    print('Ciphertext :', cipherText)

    del (plainText, key, cipherText, pT_binary)


def decrypt(key, cipherText):
    """Enter key and encrypted message"""
    plainT = list()
    key_binary = list()
    cT_binary = list()
    pT_binary = list()

    for i in key:
        key_ascii = ord(i)
        key_bool = ibin(key_ascii)
        key_binary.append(key_bool)

    #Conversion
    cipherText = base64.b64decode(cipherText)
    cipherText = cipherText.decode()

    for i in cipherText:
        cT_ascii = ord(i)
        cT_bool = ibin(cT_ascii)
        cT_binary.append(cT_bool)

    for i in range(0, len(cT_binary)):
        pT_list = list()
        for j in range(0, len(cT_binary[i])):
            pT_element = xor(int(cT_binary[i][j]), int(key_binary[i][j]))
            pT_element = str(pT_element)
            pT_list.append(pT_element)
        pT_list = ''.join(pT_list)
        pT_binary.append(pT_list)
        del (pT_list)

    del cT_binary

    for i in pT_binary:
        val = int(i, 2)
        char = chr(val)
        plainT.append(char)
        plainText = ''.join(plainT)

    print('Plaintext : ', plainText)


# Calls

plainText = input("Enter the message : ")
encrypt(plainText)
while True:
    choice = input('\nWould you like to decrypt any messages ? (Y/N) ')
    if choice == 'N' or choice == 'n':
        break
    elif choice == 'Y' or choice == 'y':
        key = input("Enter key : ")
        cipherText = input("Enter Ciphertext : ")
        decrypt(key, cipherText)
        break
    else:
        print('Enter valid choice !\n')
