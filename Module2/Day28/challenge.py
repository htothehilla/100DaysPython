#Create a program to encrypt and decrypt messages using a substitution cipher.

import logging

# The user provides a word that does not have any duplicate letters and no numbers or special characters.
word = input("Would you like to encrypt or decrypt your message ?, answer [encrypt/decrypt]")

def test():
    if word.islower():
        print("next question")
    elif word.isspace():
        print("can't continue")
    elif word.isnumeric():
        print("can't continue")
    else:
        print("{} is not an acceptable entry, please provide a lowercase message, "
          "with no number, no space or special charcters.".format(word))
test()








# The user then provides the instruction to either encrypt or decrypt the message.
# Finally, the user then provides the message to be encrypted or decrypted.
# Create a function to check if the transposition word is valid, another function to encrypt the message, and a third function to decrypt the message.
# When encrypting the message, only letters should be provided; do not return any spaces, numbers, or special character.
# Additionally, the program should not be case sensitive and all output should be in lowercase.
# Finally, add robust logging to collect insights about the effectiveness of the application



# os.chdir(".\\Module2\\Day28")

