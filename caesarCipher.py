import caesarCipherLogo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
't', 'u', 'v', 'w', 'x', 'y', 'z']
'''
def encrypt(word, num):
    newText = ""
    encrpytedChar =""
    lengthArray = len(alphabet)
    for char in word:
        position = alphabet.index(char)
        newPosition = position + num
        print(f"what is newPosition {newPosition}")
        #print(f"what is the length {lengthArray}")
        
        if newPosition > lengthArray:
            shiftPosition = newPosition - lengthArray
            #print(f"what is the shiftPosition {shiftPosition}")
            encrpytedChar = alphabet[shiftPosition]
        else:
            encrpytedChar = alphabet[newPosition]
        newText += encrpytedChar
    
    print(f"Your message has been encrypted => {newText}")
    
def decrypt(word, num):
    newText = ""
    encrpytedChar =""
    lengthArray = len(alphabet)
    for char in word:
        position = alphabet.index(char)
        newPosition = position - num
        #print(f"what is newPosition {newPosition}")
        #print(f"what is the length {lengthArray}")
        
        if newPosition > lengthArray:
            shiftPosition = newPosition + lengthArray
            #print(f"what is the shiftPosition {shiftPosition}")
            encrpytedChar = alphabet[shiftPosition]
        else:
            encrpytedChar = alphabet[newPosition]
        newText += encrpytedChar
    
    print(f"Your message has been encrypted => {newText}")
'''
def caesar(word,num,operation):
    newText = ""
    encrpytedChar =""
    lengthArray = len(alphabet)
    if operation == 'encode':
        for char in word:
            if not char.isalpha():
                newText += char
                continue

            position = alphabet.index(char)
            newPosition = position + num
            print(f"what is newPosition {newPosition}")
            #print(f"what is the length {lengthArray}")
            
            if newPosition > lengthArray:
                shiftPosition = newPosition - lengthArray
                #print(f"what is the shiftPosition {shiftPosition}")
                encrpytedChar = alphabet[shiftPosition]
            else:
                encrpytedChar = alphabet[newPosition]
            newText += encrpytedChar
    else:
        for char in word:
            if not char.isalpha():
                newText += char
                continue
            position = alphabet.index(char)
            newPosition = position - num
            #print(f"what is newPosition {newPosition}")
            #print(f"what is the length {lengthArray}")
            
            if newPosition > lengthArray:
                shiftPosition = newPosition + lengthArray
                #print(f"what is the shiftPosition {shiftPosition}")
                encrpytedChar = alphabet[shiftPosition]
            else:
                encrpytedChar = alphabet[newPosition]
            newText += encrpytedChar
    print(f"Your message has been encrypted => {newText}")

print(caesarCipherLogo.logo)
result = 'y'
while result =='y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(text,shift,direction)
    result = input("Again? y or n")