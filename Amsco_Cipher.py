def calcCollumnNumber(keyLength, stringLength):
    colNum = [0] * keyLength
    charNum = 1
    indexCol = 0
    counter = stringLength
    while counter > 0:
        colNum[indexCol] += charNum
        counter -= charNum
        indexCol = (indexCol + 1) % keyLength
        if charNum == 1:
            charNum = 2
        else:
            charNum = 1
        if counter == 1 and charNum == 2: #if true we are at the last letter
            charNum = 1 #so only add one to the count
    return colNum

def encrypt(textToEncrypt, key):
    #setup: get the number of characters in each column
    keyLength = len(str(key)) #length of key determines number of columns
    stringLength = len(textToEncrypt)
    colNum = calcCollumnNumber(keyLength, stringLength)

    for i, digit in enumerate(key):
        print(digit, colNum[i])

    #order columns and match with the number of characters
    digitsWithChars = [(digit, colNum[i]) for i, digit in enumerate(key)]
    print(digitsWithChars)

    #chop up text
    chopped = [''] * keyLength
    counter = stringLength
    keyCounter = 0
    charNum = 1
    while counter > 0: #works just like calc colNumber except with chars 
        number, colNumber = digitsWithChars[keyCounter]
        chopped[int(number) - 1] += textToEncrypt[:charNum]
        textToEncrypt = textToEncrypt[charNum:]
        counter -= charNum
        keyCounter = (keyCounter + 1) % keyLength
        if charNum == 1:
            charNum = 2
        else:
            charNum = 1
        if charNum == 2 and counter == 1:
            charNum = 1
    print(chopped)

    #put ciphter text together
    cipherText = ''
    for i in range(keyLength):
        cipherText += chopped[i]

    return cipherText
    
    

def decrypt(cipherText, key):
    #setup
    keyLength = len(key)
    stringLength = len(cipherText)
    colNum = calcCollumnNumber(keyLength, stringLength)

    for i, digit in enumerate(key):
        print(digit, colNum[i])

    #order columns and match with the number of letters in each 
    digitsWithChars = [(digit, colNum[i]) for i, digit in enumerate(key)]
    digitsWithChars = sorted(digitsWithChars)
    print(digitsWithChars)

    #chop up text
    chopped = [''] * keyLength
    for i in range(keyLength):
        digit, colNumber = digitsWithChars[i]
        chopped[i] = cipherText[:colNumber]
        cipherText = cipherText[colNumber:]
    print(chopped)

    #put decrypted message together
    keyCounter = 0
    charNum = 1
    counter = stringLength
    decrytedMessage = ''
    while counter > 0:
        indexColumn = int(key[keyCounter]) - 1
        decrytedMessage += chopped[indexColumn][:charNum]
        chopped[indexColumn] = chopped[indexColumn][charNum:]
        counter -= charNum
        keyCounter = (keyCounter + 1) % keyLength
        if charNum == 1:
            charNum = 2
        else:
            charNum = 1
        if charNum == 2 and counter == 1:
            charNum = 1

    return decrytedMessage

    

def main():
    print('Enter text to encrypt: ')
    text = input()
    print('Please enter a key: ')
    key = input()

    text = encrypt(text, key)

    print('Encrypted Message:', text)

    print('Decrypt Message? ')
    answer = input()
    if answer == 'yes' or answer == 'y':
        print('Decrypted message: ', decrypt(text, key))

if __name__ == '__main__':
    main()
