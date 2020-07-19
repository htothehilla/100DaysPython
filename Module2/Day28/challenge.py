#Create a program to encrypt and decrypt messages using a substitution cipher.
import random
import logging
import os
import sys
from sys import exit

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day28_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()

# The user provides a word that does not have any duplicate letters and no numbers or special characters.
word = input("provide a word that does not have any duplicate letters and no numbers or special characters")

def test(word):
    if word.islower() and not word.isnumeric() :
        return
    else:
        print("{} is not an acceptable entry, please provide a lowercase message, "
          "with no number, no space or special charcters.".format(word))
    logging.error("didn't work")
    exit(0)
test(word)

choice = input("Would you like to encrypt or decrypt your message ?, answer [encrypt/decrypt]")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'nuuiyvxqflfbcjrodhkaewhspzgm'

def makeKey(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def encrypt(word, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in word]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

cipher = encrypt(word, key, alphabet)

if choice == 'encrypt':
    print(f"Your encrypted word is {cipher}")
    logger.info('working')


def decrypt(cipher, key, alphabet):
    keyIndices = [key.index(k) for k in cipher]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)

if choice == 'decrypt':
    print(f"Your encrypted word is {decrypt(cipher, key, alphabet)}")
    logger.info('working')




# The user then provides the instruction to either encrypt or decrypt the message.
# Finally, the user then provides the message to be encrypted or decrypted.
# Create a function to check if the transposition word is valid, another function to encrypt the message, and a third function to decrypt the message.
# When encrypting the message, only letters should be provided; do not return any spaces, numbers, or special character.
# Additionally, the program should not be case sensitive and all output should be in lowercase.
# Finally, add robust logging to collect insights about the effectiveness of the application





