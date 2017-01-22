#Substitution Cipher Program written by Caleb Barnwell
#Computer Science, 12-6-15

import string

def substitutionCipher (message,cipherString):
    alphabet = string.ascii_lowercase
    encryptedMessage = ""
    message = message.lower()
    for letter in range(len(message)):
        found = False
        for alphaLetter in range(len(alphabet)): 
            if(message[letter] == alphabet[alphaLetter]):
                encryptedMessage += cipherString[alphaLetter]
                found=True
        if found == False:
            encryptedMessage += message[letter]
    return encryptedMessage 

userMessage = input("Please input message: ")
mappingString = input("Please input cipher string: ")
print("The encrypted message = " +substitutionCipher(userMessage, mappingString))
