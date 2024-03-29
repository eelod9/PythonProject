import random
word_list = ["aardvark", "baboon", "camel"]

#user input a-z
#if wrong, pop letter and decrease counter
#else correct pop letter and fill in word
# in while loop until right answer
randomWord = random.choice(word_list)

print("Hello, Welcome to Hanman. Let's start")
#name = input("What is you name?")
#print(f'Hello {name}. Prepare to lose!')

def printHangman(tries):
    match tries:
        case 0:
            print('''
                      ____
                     |    |
           DEAD      O    |
                    /|\   |
                    / \  _|_ 
                     
                     ''')
        case 1:
            print(''' 
                      ____
                     |    |
                     O    |
                    /|    |
                    / \  _|_ 
                     
                     ''')
        case 2:
            print(''' 
                      ____
                     |    |
                     O    |
                     |    |
                    / \  _|_ 
                     
                     ''')
        case 3:
            print(''' 
                      ____
                     |    |
                     O    |
                     |    |
                    /    _|_ 
                     
                     ''')
        case 4:
            print('''
                      ____
                     |    |
                     O    |
                     |    |
                         _|_ 
                     
                     ''')
        case 5:
            print('''
                      ____
                     |    |
                     O    |
                          |
                         _|_ 
                     
                     ''')
        case 6:
            print('''
                      ____
                     |    |
                          |
                          |
                         _|_ 
                     
                     ''')


tries = 6 #o
         #/|\
         #/ \
statusArray = ["-"] * len(randomWord)
done = 0
map={}
#print(randomWord)
while tries > 0:
    
    print(statusArray)
    printHangman(tries)
    guessedLetter= input("Guess: ").lower()

    found = False
    existsInMap = False
    
    if guessedLetter.isalpha():
        try:
             val = map[guessedLetter]
             existsInMap = True
        except:
            #print("does not exist in map")
            pass
        #if guessedLetter not in map:
        if not existsInMap:
            for k, letter in enumerate(randomWord):
                if guessedLetter == letter:
                    #print(f"{guessedLetter} and letter {letter}")
                    map[letter] = True
                    found = True
                    statusArray[k] = letter
                    done += 1
                    #print(f"yes ---{guessedLetter}--- is correct")
                    #break
                elif not found:
                    map[guessedLetter] = False
            if not found:
                tries -=1 
                print(f"WRONG!! {guessedLetter} not in word")
                
        else:
            print(f"You've already tried {guessedLetter}")
                    
    else:
        print("please try entering an alphabet") 

    if tries ==0:
        print("Game Over")
        printHangman(tries)
    elif done == len(randomWord):
        print("You have guess all alphabets correctly before man hanged. Congrats")
        break
    elif found:
        print(statusArray)
        guessedWord = input("Wanna guess the word?")
        if guessedWord == randomWord:
            print("You did it!!!")
            break
        else:
            print("Wrong word")
    else:
        print(f"{tries} left!")


    


