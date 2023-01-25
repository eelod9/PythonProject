import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player1 = []
computer = []
p_num = random.choice(cards)
p_num1 = random.choice(cards)
c_num = random.choice(cards)
c_num1 = random.choice(cards)
player1.append(p_num)
player1.append(p_num1)
computer.append(c_num)
computer.append(c_num1)

def totalScore(myArray):
    score = 0
    for val in myArray:
        score += val
    return score

def evaluateScore(myScore):
    if(myScore == 21):
        print(f"You win! score: {myScore}")
        return 1
    elif(myScore >21):
        print(f"BUST You lose! score: {myScore}")
        return 0
    else:
        print(f" score: {myScore}")
        return 2

p_score = totalScore(player1)
c_score = totalScore(computer)

print(f"Your cards: {player1}, your score: {p_score}")
print(f"Your computer: {computer}, computer score: {c_score}")
print(f"Computer's first card: {computer[1]}")
computer.append(random.choice(cards))
winner = 2
while(winner == 2):
    hit = input("Type 'y' to hit, type 'n' to pass: ")
    if(hit == 'y'):
        player1.append(random.choice(cards))
        p_score= totalScore(player1)
        print(f"your cards {player1} and score is {p_score} ")
        winner = evaluateScore(p_score)
    else:#do not hit
        p_score = totalScore(player1)
        winner = evaluateScore(p_score)
        if(winner==2):
            if(c_score>p_score):
                print(f"computer wins! your score: {p_score}, comp score: {c_score}")
            elif(c_score ==p_score):
                print(f"TIE")
            else:
                print(f"You Win with {p_score}")
                winner = 1
        break
                

