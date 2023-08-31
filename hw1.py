# import io.TextIO
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            
def encrypt(plaintext, key):
    ciphertext = ''
    for x in plaintext:
        if x in lowers:
            x = lowers[(lowers.index(x) + (key % 26))%26]
            ciphertext += x
        elif x in uppers:
            x = uppers[(uppers.index(x) + (key % 26))%26]
            ciphertext += x
        else:
            ciphertext += x
            continue
    # print("Your encrypted word is: " + ciphertext + ".")   
    return ciphertext
def decrypt(ciphertext, key):
    plaintext = ""
    for x in ciphertext:
        if x in lowers:
            x = lowers[(lowers.index(x) - (key % 26))%26]
            plaintext += x
        elif x in uppers:
            x = uppers[(uppers.index(x) - (key % 26))%26]
            plaintext += x
        else:
            plaintext += x
            continue
    return plaintext
def fileDecrypt(ciphertext, filename):
    thisFile = open(filename, 'r')

    # Saves each string as a list element
    wordsFromFile = thisFile.read().split()
    thisFile.close()
    
    # Cleans up all non-alphabetic characters from each string
    wordsFromFile = [word.strip() for word in wordsFromFile if word.isalpha()]
    # print(wordsFromFile)
    
    #Breaks up the input by each word and puts them in a list
    cipherWords = ciphertext.split(" ")

    # FINDING THE KEY
    matches = []
    keyFound = False
    for keyFind in range(26): #Iterate through all keys possible (0-25)
        decryptedWords = [decrypt(word, keyFind) for word in cipherWords]
        for each in decryptedWords:
            for every in wordsFromFile:
                if keyFound:
                    pass
                elif each == every: #Checks for matches between input and the file
                    matches.append(each)
                    key = keyFind
                    keyFound = True
                    # print(f"Found {each} using the key {keyFind}")
                    # break
    # print(decryptedWords)
    plaintext = ' '.join(matches)
    print(f"Output:\n\tKey: {key}\n\tPlaintext Message: {plaintext}")

        
#-----------------------Testing Each Function-------------------------------
# for each in range(26):
# print(encrypt('computer world science simulation', 15)) #sdgdzdq vlpxodwlrq
# # print(decrypt('jgnnq rcfcycp', 2))
# fileDecrypt('rdbejitg ldgas hrxtcrt hxbjapixdc', '../sample.txt')
# fileDecrypt('rdbejitg ldgas hrxtcrt hxbjapixdc', '../sample.txt')
# print(decrypt('hello padawan', 2)) #fcjjm n_b_u_l
#---------------------------------------------------------------------------
print('----------------------------------------------------------------------')
print('Welcome to CipherHelper! Please choose one of the following options:')
print('\t(1): Encrypt a Message')
print('\t(2): Decrypt a Message')
print('\t(3): Decrypt a Message, then find in a file')
print('\t(3): Exit CipherHelper')
print('----------------------------------------------------------------------')

menuInput = input()

if menuInput == '1':
    plainInput = input('Please type your message: ')
    keyInput = input('Please indicate the key: ')
    print("Your encrypted phrase is: " + encrypt(plainInput, int(keyInput)))
elif menuInput == '2':
    textInput = input('Please write the message to be decoded: ')
    keyInput = input('Please indicate the key: ')
    print(f"Your phrase using key = {keyInput} is: " + decrypt(textInput, int(keyInput)))
elif menuInput == '3':
    cipherInput = input("Please type the ciphertext: ")
    fileInput = input("Please enter the file to parse: ")
    fileDecrypt(cipherInput, fileInput)
elif menuInput == '0':
    quit()
else:
    print('Input was wrong.')
