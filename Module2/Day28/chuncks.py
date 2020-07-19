choice = input("Would you like to encrypt or decrypt your message ?, answer [encrypt/decrypt]")
if choice == "encrypt":
    tocreate
if choice == "decrpyt":
    tocreate


#removes duplicates in a messgae
def remove_repeats(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            while string[i:j] == string[j:j + j - i]:
                string = string[:j] + string[j + j - i:]
    return string
cleanmessage = print(remove_repeats(message))